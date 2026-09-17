"""Reloop Terminal Mix 8 -> virtual Pioneer MIDI bridge for rekordbox 6/7.

Windows setup: Terminal Mix 8 is the input, loopMIDI port named
"PIONEER DDJ-SX" is the output selected by rekordbox.

This bridge forwards all normal MIDI messages, records jog traffic, and
translates the TM8 relative jog encoder into the 7-bit jog values expected by
Pioneer-style rekordbox mappings. Exact jog note/CC numbers can be adjusted in
config.json after running --dump.
"""
from __future__ import annotations
import argparse, json, sys, time
from pathlib import Path
import mido

DEFAULTS = {
    "input_contains": "Terminal Mix 8",
    "output_contains": "PIONEER DDJ-SX",
    "dump_file": "tm8_midi_dump.jsonl",
    "jog": {
        "enabled": True,
        "cc_by_deck": {"0": 7, "1": 7, "2": 7, "3": 7},
        "touch_note_by_deck": {"0": 7, "1": 7, "2": 7, "3": 7},
        "rekordbox_jog_cc": 34,
        "rekordbox_touch_note": 54,
        "output_channel_by_input": {"0": 0, "1": 1, "2": 2, "3": 3},
        "vinyl_note_by_deck": {"0": 1, "1": 1, "2": 1, "3": 1},
        "jog_mode": "centered_relative",
        "neutral": 64,
        "scale": 1,
        "reverse": False
    },
    "filter": {"drop_sysex": False, "jog_only_test": False}
}


def load_config(path: Path) -> dict:
    if not path.exists():
        path.write_text(json.dumps(DEFAULTS, indent=2), encoding="utf-8")
        return DEFAULTS
    data = json.loads(path.read_text(encoding="utf-8"))
    # shallow recursive merge so new fields survive upgrades
    def merge(a, b):
        for k, v in b.items():
            if isinstance(v, dict) and isinstance(a.get(k), dict): merge(a[k], v)
            else: a[k] = v
    result = json.loads(json.dumps(DEFAULTS)); merge(result, data); return result


def choose_port(kind: str, wanted: str) -> str:
    ports = mido.get_input_names() if kind == "in" else mido.get_output_names()
    if not ports:
        raise RuntimeError(f"Keine MIDI-{kind}-Ports gefunden.")
    for p in ports:
        if wanted.lower() in p.lower(): return p
    print(f"Kein Treffer für '{wanted}'. Verfügbare {kind}-Ports:")
    for i, p in enumerate(ports): print(f"  [{i}] {p}")
    raise RuntimeError("Bitte input_contains/output_contains in config.json anpassen.")


def dump_message(fp, msg):
    rec = {"time": time.time(), "type": msg.type}
    rec.update({k: getattr(msg, k) for k in ("channel", "note", "control", "value", "velocity", "pitch") if hasattr(msg, k)})
    fp.write(json.dumps(rec) + "\n"); fp.flush()


def deck_from_channel(channel: int) -> int:
    # TM8 main decks are MIDI channels 1-4, represented by mido 0-3.
    return max(0, min(3, channel))


def translate_jog(msg, cfg):
    """Translate only TM8 jog rotation/touch to the DDJ-SX JogScratch input.

    Deliberately does NOT create or forward WheelPitchBend. Pitch bend is a
    separate control and must not be added to the jogwheel.
    """
    jog = cfg["jog"]
    if not jog.get("enabled"): return None
    deck = deck_from_channel(msg.channel)
    out_channel = jog.get("output_channel_by_input", {}).get(str(deck), msg.channel)
    if msg.type == "control_change":
        cc = jog["cc_by_deck"].get(str(deck))
        if cc is None or msg.control != cc: return None
        # TM8 dump shows centered relative values (63/65). Preserve the
        # centered value and change only the CC to DDJ-SX JogScratch (0x0A).
        value = max(0, min(127, int(msg.value)))
        if jog.get("reverse"):
            value = 128 - value if value else 127
        return mido.Message("control_change", channel=out_channel,
                            control=int(jog.get("rekordbox_jog_cc", 10)), value=value)
    if msg.type in ("note_on", "note_off"):
        touch = jog["touch_note_by_deck"].get(str(deck))
        if touch is None or msg.note != touch: return None
        return mido.Message(msg.type, channel=out_channel,
                            note=int(jog.get("rekordbox_touch_note", 8)),
                            velocity=msg.velocity)
    return None


def translate_transport(msg, cfg):
    """Translate TM8 transport notes to Pioneer DDJ-SX notes."""
    if msg.type not in ("note_on", "note_off"):
        return None
    # Optional press-only mode is available, but the safe default is to
    # preserve the physical press/release pair and avoid feedback in CSV.
    if cfg.get("transport", {}).get("press_only", False):
        if msg.type == "note_off" or (msg.type == "note_on" and msg.velocity == 0):
            return None
    channel = msg.channel
    mapping = cfg.get("transport", {}).get("notes", {})
    spec = mapping.get(str(msg.note))
    if spec is None:
        return None
    if isinstance(spec, dict) and "by_channel" in spec:
        spec = spec["by_channel"].get(str(channel))
        if spec is None:
            return None
    if isinstance(spec, dict):
        target = int(spec["note"])
        out_channel = int(spec.get("channel", channel))
    else:
        target = int(spec)
        out_channel = channel
    if cfg.get("transport", {}).get("press_only", False):
        return mido.Message("note_on", channel=out_channel, note=target, velocity=127)
    return mido.Message(msg.type, channel=out_channel, note=target, velocity=msg.velocity)


def translate_loop(msg, cfg, last_loop_cc):
    """Translate the TM8 loop encoder and loop-on buttons."""
    loop = cfg.get("loop", {})
    if msg.type == "control_change":
        cc = loop.get("encoder_cc_by_channel", {}).get(str(msg.channel))
        if cc is None or msg.control != int(cc):
            return None
        # The TM8 emits the same relative value repeatedly until the encoder
        # stops. Trigger one Pioneer loop-size action per value transition.
        key = str(msg.channel)
        if last_loop_cc.get(key) == msg.value:
            return None
        last_loop_cc[key] = msg.value
        target = loop.get("encoder_values", {}).get(str(msg.value))
        if target is None:
            return None
        # LoopHalf/LoopDouble are Pioneer button actions. Emit a complete
        # press/release pulse, not a latched Note-On.
        out_channel = int(loop.get("encoder_output_channel", msg.channel))
        return [
            mido.Message("note_on", channel=out_channel, note=int(target), velocity=127),
            mido.Message("note_off", channel=out_channel, note=int(target), velocity=0),
        ]
    if msg.type in ("note_on", "note_off"):
        target = loop.get("note_map", {}).get(str(msg.note))
        if target is None:
            return None
        if loop.get("note_press_only", False):
            if msg.type == "note_off" or (msg.type == "note_on" and msg.velocity == 0):
                return None
            return [mido.Message("note_on", channel=msg.channel,
                                 note=int(target), velocity=127)]
        return [mido.Message(msg.type, channel=msg.channel, note=int(target), velocity=msg.velocity)]
    return None


def translate_pitchwheel(msg, cfg):
    """Convert TM8 pitchwheel data to Pioneer 14-bit tempo CC data."""
    pitch = cfg.get("pitch", {})
    if not pitch.get("enabled", False) or msg.type != "pitchwheel":
        return None
    if str(msg.channel) not in pitch.get("channels", ["0", "1"]):
        return None
    unsigned = max(0, min(16383, int(msg.pitch) + 8192))
    msb = unsigned >> 7
    lsb = unsigned & 0x7F
    cc = int(pitch.get("output_cc", 0))
    return [
        mido.Message("control_change", channel=msg.channel, control=cc, value=msb),
        mido.Message("control_change", channel=msg.channel,
                     control=int(pitch.get("output_lsb_cc", 32)), value=lsb),
    ]


def translate_mixer(msg, cfg):
    """Translate only the tested channel-fader, gain and EQ controls."""
    mixer = cfg.get("mixer", {})
    if not mixer.get("enabled", False) or msg.type != "control_change":
        return None
    targets = mixer.get("target_cc_by_input_cc", {})
    target = targets.get(str(msg.control))
    if target is None:
        return None
    return mido.Message("control_change", channel=msg.channel,
                        control=int(target), value=max(0, min(127, int(msg.value))))


def translate_filter(msg, cfg):
    """Translate TM8 filter CC13 to DDJ-SX CFX controls on channel 7."""
    filt = cfg.get("filter_control", {})
    if not filt.get("enabled", False) or msg.type != "control_change":
        return None
    if msg.control != int(filt.get("input_cc", 13)):
        return None
    target = filt.get("output_cc_by_channel", {}).get(str(msg.channel))
    if target is None:
        return None
    return mido.Message("control_change",
                        channel=int(filt.get("output_channel", 6)),
                        control=int(target),
                        value=max(0, min(127, int(msg.value))))


def translate_browse(msg, cfg):
    """Translate the TM8 browse encoder and its push/enter action."""
    browse = cfg.get("browse", {})
    if not browse.get("enabled", False):
        return None
    out_channel = int(browse.get("output_channel", 6))
    if msg.type == "control_change":
        if msg.channel != int(browse.get("input_channel", 0)) or msg.control != int(browse.get("input_cc", 40)):
            return None
        return mido.Message("control_change", channel=out_channel,
                            control=int(browse.get("output_cc", 64)), value=msg.value)
    if msg.type in ("note_on", "note_off") and msg.channel == int(browse.get("input_channel", 0)) and msg.note == int(browse.get("press_note", 40)):
        if browse.get("press_only", True) and (msg.type == "note_off" or msg.velocity == 0):
            return None
        return mido.Message("note_on", channel=out_channel,
                            note=int(browse.get("output_note", 65)), velocity=127)
    return None


def run(config_path: Path, dump_only=False, debug=False):
    cfg = load_config(config_path)
    inp = choose_port("in", cfg["input_contains"])
    out = choose_port("out", cfg["output_contains"])
    print(f"IN : {inp}\nOUT: {out}")
    print("Bridge aktiv. Beenden: Ctrl+C")
    dump_fp = open(cfg["dump_file"], "a", encoding="utf-8") if dump_only else None
    touch_active = {0: False, 1: False, 2: False, 3: False}
    last_loop_cc = {}
    try:
        with mido.open_input(inp) as midi_in, mido.open_output(out) as midi_out:
            for msg in midi_in:
                if dump_fp: dump_message(dump_fp, msg)
                if dump_only: continue
                if cfg.get("filter", {}).get("drop_sysex") and msg.type == "sysex": continue
                # The TM8 emits centered CC7 traffic while a jog is idle. Do
                # not expose that traffic to rekordbox; only pass rotation
                # while the corresponding platter is physically touched.
                if (cfg.get("jog", {}).get("require_touch", False)
                        and msg.type in ("note_on", "note_off")
                        and msg.note == cfg["jog"]["touch_note_by_deck"].get(str(deck_from_channel(msg.channel)), -1)):
                    touch_active[deck_from_channel(msg.channel)] = (msg.type == "note_on" and msg.velocity > 0)
                translated = translate_jog(msg, cfg)
                transport = translate_transport(msg, cfg)
                loop_message = translate_loop(msg, cfg, last_loop_cc)
                pitch_message = translate_pitchwheel(msg, cfg)
                mixer_message = translate_mixer(msg, cfg)
                filter_message = translate_filter(msg, cfg)
                browse_message = translate_browse(msg, cfg)
                if debug and transport is not None:
                    print(f"TRANSPORT IN {msg.bytes()} -> OUT {transport.bytes()}", flush=True)
                if debug and loop_message is not None:
                    print(f"LOOP IN {msg.bytes()} -> OUT {[m.bytes() for m in loop_message]}", flush=True)
                if debug and pitch_message is not None:
                    print(f"PITCH IN {msg.pitch} -> OUT {[m.bytes() for m in pitch_message]}", flush=True)
                if debug and mixer_message is not None:
                    print(f"MIXER IN {msg.bytes()} -> OUT {mixer_message.bytes()}", flush=True)
                if debug and filter_message is not None:
                    print(f"FILTER IN {msg.bytes()} -> OUT {filter_message.bytes()}", flush=True)
                if debug and browse_message is not None:
                    print(f"BROWSE IN {msg.bytes()} -> OUT {browse_message.bytes()}", flush=True)
                if (cfg.get("jog", {}).get("require_touch", False)
                        and msg.type == "control_change"
                        and msg.control == cfg["jog"]["cc_by_deck"].get(str(deck_from_channel(msg.channel)))
                        and not touch_active[deck_from_channel(msg.channel)]):
                    translated = None
                if debug and translated is not None:
                    print(f"JOG IN  {msg.bytes()}  -> OUT {translated.bytes()}", flush=True)
                if cfg.get("filter", {}).get("jog_only_test"):
                    # Diagnostic mode: output ONLY translated jog rotation and
                    # touch. This prevents Play/Pause, Load, pads and every
                    # other raw TM8 message from reaching rekordbox.
                    if translated is not None:
                        midi_out.send(translated)
                    continue
                if cfg.get("filter", {}).get("transport_only"):
                    if transport is not None:
                        midi_out.send(transport)
                    elif loop_message is not None:
                        for loop_msg in loop_message:
                            midi_out.send(loop_msg)
                    elif pitch_message is not None:
                        for pitch_msg in pitch_message:
                            midi_out.send(pitch_msg)
                    elif mixer_message is not None:
                        midi_out.send(mixer_message)
                    elif filter_message is not None:
                        midi_out.send(filter_message)
                    elif browse_message is not None:
                        midi_out.send(browse_message)
                    elif translated is not None:
                        midi_out.send(translated)
                    continue
                # Drop the original TM8 jog/touch message after translating;
                # pass all other controls through unchanged.
                if translated is not None:
                    midi_out.send(translated)
                elif mixer_message is not None:
                    midi_out.send(mixer_message)
                elif filter_message is not None:
                    midi_out.send(filter_message)
                elif browse_message is not None:
                    midi_out.send(browse_message)
                elif not (msg.type in ("control_change", "note_on", "note_off") and
                          ((msg.type == "control_change" and msg.control in cfg["jog"]["cc_by_deck"].values()) or
                           (msg.type in ("note_on", "note_off") and msg.note in cfg["jog"]["touch_note_by_deck"].values()))):
                    midi_out.send(msg)
    except KeyboardInterrupt:
        print("\nBridge beendet.")
    finally:
        if dump_fp: dump_fp.close()


def list_ports():
    print("MIDI Eingänge:"); [print("  ", p) for p in mido.get_input_names()]
    print("MIDI Ausgänge:"); [print("  ", p) for p in mido.get_output_names()]

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.json")
    ap.add_argument("--list", action="store_true", help="MIDI-Ports anzeigen")
    ap.add_argument("--dump", action="store_true", help="MIDI-Daten in Dump-Datei protokollieren")
    ap.add_argument("--debug", action="store_true", help="übersetzte Jogwheel-Bytes anzeigen")
    args = ap.parse_args()
    try:
        if args.list: list_ports()
        else: run(Path(args.config), dump_only=args.dump, debug=args.debug)
    except Exception as e:
        print(f"FEHLER: {e}", file=sys.stderr); sys.exit(1)
