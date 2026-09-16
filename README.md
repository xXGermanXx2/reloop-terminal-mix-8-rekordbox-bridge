# Reloop Terminal Mix 8 → rekordbox 6 MIDI-Bridge

Diese Bridge übersetzt MIDI-Signale eines **Reloop Terminal Mix 8** in MIDI-Signale, die rekordbox über ein virtuelles loopMIDI-Gerät mit dem Profil **PIONEER DDJ-SX** verarbeiten kann.

Der aktuelle Stand ist für Windows 10/11 und rekordbox 6 ausgelegt. Er unterstützt zwei Jogwheels, Play/Pause, Cue, Load für Deck 1 und 2, den Tempo-Fader für Deck 1/2 sowie Kanal-Fader, Gain und EQ über eine isolierte Mixer-Übersetzung. Der Crossfader bleibt vorerst deaktiviert. Die funktionierenden Kernfunktionen werden über einen kontrollierten Filter weitergegeben; unbekannte MIDI-Signale werden nicht an rekordbox gesendet.

> **Wichtig:** Das Projekt verwendet ein virtuelles MIDI-Gerät. Der physische Terminal Mix 8 darf in rekordbox nicht zusätzlich als zweiter aktiver MIDI-Eingang für dieselben Funktionen gemappt werden.

## Funktionsumfang

| Funktion | Status | Beschreibung |
|---|---:|---|
| Jogwheel Deck 1 | Aktiv | Scratch/Rotation über DDJ-SX-Jog-Signal |
| Jogwheel Deck 2 | Aktiv | Scratch/Rotation über DDJ-SX-Jog-Signal |
| Jog-Touch | Aktiv | Touch-Signal für beide Decks |
| Play/Pause Deck 1/2 | Aktiv | TM8 Note 5 wird auf Pioneer Note 11 übersetzt |
| Cue Deck 1/2 | Aktiv | TM8 Note 4 wird auf Pioneer Note 12 übersetzt |
| Load Deck 1/2 | Aktiv | TM8 Note 16 wird deckabhängig auf `96 46`/`96 47` übersetzt |
| Tempo-Fader Deck 1/2 | Aktiv | 14-Bit-Pitchwheel wird als Pioneer-HiRes-CC 0 + CC 32 ausgegeben |
| Kanal-Fader Deck 1–4 | Neu, zu testen | TM8 CC 15 wird isoliert auf Pioneer CC 19 übersetzt |
| Gain und EQ Deck 1–4 | Neu, zu testen | TM8 CC 9–12 werden isoliert auf Pioneer CC 4/7/11/15 übersetzt |
| Crossfader | Deaktiviert | Wird in dieser Version absichtlich nicht weitergeleitet |
| Loop-ON | Experimentell | AutoLoop an der aktuellen Position mit gewählter Loop-Länge |
| Loop-Encoder | Experimentell | kleiner/größer über LoopHalf/LoopDouble |
| Encoder-Druck | Absichtlich deaktiviert | erzeugt keine Aktion |
| Pitch-Bend | Deaktiviert | wird nicht zum Jogwheel hinzugefügt |

## Roadmap und Mapping-Fortschritt

Der Fortschritt wird nach **Funktionsgruppen des Terminal Mix 8** bewertet, nicht nach der Anzahl einzelner CSV-Zeilen. Eine Gruppe gilt erst als fertig, wenn das Eingangssignal identifiziert, die Bridge-Übersetzung implementiert, das Rekordbox-Profil angepasst und die Funktion am Controller getestet wurde.

### Gesamtfortschritt: **ca. 60 %**

| Bereich | Fortschritt | Status |
|---|---:|---|
| Jogwheels und Jog-Touch, Deck 1/2 | 100 % | Fertig und getestet |
| Play/Pause, Deck 1/2 | 100 % | Fertig und getestet |
| Cue, Deck 1/2 | 100 % | Fertig und getestet |
| Load, Deck 1/2 | 100 % | Fertig und getestet |
| Loop-ON/AutoLoop | 70 % | Signal und AutoLoop-Ziel bekannt; Rekordbox-Verhalten wird weiter abgesichert |
| Loop-Encoder Deck 2 | 50 % | Eingangssignal bekannt; LoopHalf/LoopDouble-Ausgabe noch in Validierung |
| Loop-Encoder Deck 1 | 0 % | Encoder liefert im aktuellen Dump keine MIDI-Daten; Hardwareprüfung erforderlich |
| Tempo-Fader und Tempo-Funktionen | 100 % | 14-Bit-Tempo-Fader implementiert und in rekordbox getestet |
| Kanal-Fader, Gain und EQ | 50 % | Bridge und CSV ergänzt; Controller-Test steht noch aus |
| Crossfader | 0 % | Absichtlich ausgelassen |
| Pads, Hot Cues und Sampler | 0 % | Noch nicht aufgenommen und getestet |
| FX-Regler und FX-Tasten | 0 % | Noch nicht aufgenommen und getestet |
| Browser, Track-Auswahl und weitere Bedienelemente | 0 % | Noch nicht aufgenommen und getestet |

### Nächste Schritte

1. **Loop-ON und Loop-Encoder stabilisieren**, ohne den funktionierenden Transport- und Jogwheel-Bereich zu verändern.
2. **Kanal-Fader, Gain und EQ** einzeln testen, ohne den Crossfader zu aktivieren.
3. **Pads und Hot Cues** pro Deck aufnehmen und testen.
4. **FX- und Browser-Bereich** ergänzen.
5. Nach jeder Gruppe eine versionierte Sicherung erstellen und alle bereits fertigen Funktionen erneut testen.

> Die Prozentangabe ist eine technische Projektanzeige und keine Garantie für eine bestimmte rekordbox-Version. MIDI-Profile können sich zwischen rekordbox-Versionen unterscheiden; jede neue Gruppe muss deshalb auf dem Zielsystem getestet werden.

## MIDI-Signalübersicht

### Reloop Terminal Mix 8 → Bridge

| TM8-Funktion | Rohsignal |
|---|---|
| Jog Deck 1 drehen | Kanal 1, CC 7 |
| Jog Deck 2 drehen | Kanal 2, CC 7 |
| Jog-Touch Deck 1 | Kanal 1, Note 7 |
| Jog-Touch Deck 2 | Kanal 2, Note 7 |
| Play/Pause | Note 5 auf dem jeweiligen Deck-Kanal |
| Cue | Note 4 auf dem jeweiligen Deck-Kanal |
| Load | Note 16 auf dem jeweiligen Deck-Kanal |
| Loop-Encoder Deck 2 | Kanal 2, CC 29, Werte 63/65 |
| Loop-ON | Note 30 auf dem jeweiligen Deck-Kanal |
| Tempo-Fader | Pitchwheel auf dem jeweiligen TM8-Deck-Kanal |

### Bridge → rekordbox/DDJ-SX-Profil

| Funktion | Zielsignal |
|---|---|
| Jog Rotation | CC 34 auf dem jeweiligen Kanal |
| Jog-Touch | Note 54 auf dem jeweiligen Kanal |
| Play/Pause | Note 11 auf dem jeweiligen Kanal |
| Cue | Note 12 auf dem jeweiligen Kanal |
| Load Deck 1 | `96 46` |
| Load Deck 2 | `96 47` |
| AutoLoop | Note 20 auf dem jeweiligen Kanal |
| Loop kleiner | Note 18 |
| Loop größer | Note 19 |
| Tempo-Fader MSB | CC 0 auf dem jeweiligen Kanal |
| Tempo-Fader LSB | CC 32 auf dem jeweiligen Kanal |
| Kanal-Fader | CC 19 auf dem jeweiligen Kanal |
| Gain | CC 4 auf dem jeweiligen Kanal |
| EQ High | CC 7 auf dem jeweiligen Kanal |
| EQ Mid | CC 11 auf dem jeweiligen Kanal |
| EQ Low | CC 15 auf dem jeweiligen Kanal |

## Voraussetzungen

- Windows 10 oder Windows 11
- Reloop Terminal Mix 8 mit USB-Verbindung
- rekordbox 6
- loopMIDI
- Python 3.11 oder 3.12
- Python-Pakete aus `requirements.txt`

## Installation

### 1. loopMIDI installieren

Installiere loopMIDI von der offiziellen Tobias-Erichsen-Webseite. Erstelle anschließend genau einen virtuellen Port mit dem Namen:

```text
PIONEER DDJ-SX
```

Der Name muss exakt übereinstimmen. Groß-/Kleinschreibung ist normalerweise unkritisch, zusätzliche Leerzeichen oder ein anderer Name können aber dazu führen, dass die Bridge den Ausgang nicht findet.

### 2. Bridge-Ordner anlegen

Entpacke das Repository beispielsweise nach:

```text
C:\DJ\DJ Tools\terminal_mix8_rekordbox
```

In diesem Ordner müssen mindestens diese Dateien liegen:

```text
terminal_mix8_rekordbox.py
config.json
requirements.txt
PIONEER DDJ-SX.midi.csv
```

### 3. Python-Abhängigkeiten installieren

Öffne eine Eingabeaufforderung im Bridge-Ordner und führe aus:

```bat
py -3.12 -m pip install -r requirements.txt
```

Falls Python 3.11 installiert ist, kann stattdessen verwendet werden:

```bat
py -3.11 -m pip install -r requirements.txt
```

### 4. Rekordbox-MIDI-Profil installieren

Kopiere ausschließlich diese Datei in den rekordbox-MIDI-Mappings-Ordner:

```text
PIONEER DDJ-SX.midi.csv
```

Ein typischer Pfad ist:

```text
C:\Program Files\Pioneer\rekordbox 6\MidiMappings\
```

Je nach Installation kann der Versionsordner anders heißen. Suche bei Bedarf im rekordbox-Installationsordner nach `MidiMappings`.

Vor dem Ersetzen sollte die vorhandene Datei gesichert werden:

```text
PIONEER DDJ-SX.midi.csv.original.backup
```

### 5. Rekordbox und Bridge vollständig neu starten

Nach dem Kopieren der CSV muss rekordbox vollständig beendet und neu gestartet werden. Ein bloßes Schließen des MIDI-Fensters reicht nicht immer aus.

## Start

Die empfohlene Startreihenfolge lautet:

1. Terminal Mix 8 per USB anschließen.
2. loopMIDI starten und den Port `PIONEER DDJ-SX` aktivieren.
3. Eine Eingabeaufforderung im Bridge-Ordner öffnen.
4. Bridge starten:

```bat
py -3.12 terminal_mix8_rekordbox.py --config config.json --debug
```

Erwartete Ausgabe:

```text
IN : Terminal Mix 8 0
OUT: PIONEER DDJ-SX 2
Bridge aktiv. Beenden: Ctrl+C
```

5. Erst jetzt rekordbox starten.
6. In rekordbox das Profil `PIONEER DDJ-SX` auswählen.

## Bedienung und Testreihenfolge

Nach dem Start sollten die Funktionen in dieser Reihenfolge geprüft werden:

1. Play/Pause Deck 1 und Deck 2
2. Cue Deck 1 und Deck 2
3. Load Deck 1 und Deck 2
4. Jogwheel Deck 1
5. Jogwheel Deck 2
6. Loop-Länge auf einen Wert wie 8 Beats stellen
7. Loop-ON-Taste testen
8. Loop-Encoder langsam nach links und rechts drehen

Die Debug-Ausgabe zeigt übersetzte Nachrichten. Beispiele:

```text
TRANSPORT IN [144, 5, 127] -> OUT [144, 11, 127]
TRANSPORT IN [144, 4, 127] -> OUT [144, 12, 127]
```

Jogwheel-Ausgaben sehen beispielsweise so aus:

```text
JOG IN [176, 7, 65] -> OUT [176, 34, 65]
```

Loop-Ausgaben sehen beispielsweise so aus:

```text
LOOP IN [144, 30, 127] -> OUT [[144, 20, 127]]
```

## Wichtige rekordbox-Einstellungen

Der physische Eingang `Terminal Mix 8` darf nicht zusätzlich parallel zum virtuellen `PIONEER DDJ-SX`-Eingang dieselben Transportfunktionen steuern. Der empfohlene Signalweg ist:

```text
Terminal Mix 8 → Bridge → loopMIDI PIONEER DDJ-SX → rekordbox
```

Nicht empfohlen ist:

```text
Terminal Mix 8 → rekordbox
Terminal Mix 8 → Bridge → rekordbox
```

Das parallele Aktivieren beider Wege kann Play/Pause doppelt auslösen oder einen Track sofort wieder starten.

## Fehlerbehebung

### `Kein Treffer für 'PIONEER DDJ-SX'`

Prüfe, ob loopMIDI geöffnet ist und der Port exakt so heißt:

```text
PIONEER DDJ-SX
```

Zeige die verfügbaren Ports an mit:

```bat
py -3.12 terminal_mix8_rekordbox.py --list
```

### `MidiInWinMM::openPort: error creating Windows MM MIDI input port`

Der Terminal Mix 8 wird wahrscheinlich bereits von einem zweiten Programm geöffnet. Schließe rekordbox, Serato, Mixxx, die Bridge und andere MIDI-Monitor-Programme. Starte anschließend nur die Bridge neu.

### Jogwheel funktioniert im CMD, aber nicht in rekordbox

Prüfe:

1. Liegt `PIONEER DDJ-SX.midi.csv` im richtigen `MidiMappings`-Ordner?
2. Wurde rekordbox nach dem Kopieren vollständig neu gestartet?
3. Ist in rekordbox das Profil `PIONEER DDJ-SX` aktiv?
4. Wird wirklich nur der virtuelle Port verwendet?
5. Zeigt die Bridge `OUT: PIONEER DDJ-SX` an?

### Play/Pause startet sofort wieder

Bridge und rekordbox schließen. Prüfe, dass kein zweites direktes Terminal-Mix-8-Mapping aktiv ist. Verwende außerdem nur eine einzige `PIONEER DDJ-SX.midi.csv` im aktiven `MidiMappings`-Ordner.

### Loop geht direkt wieder aus

Prüfe, dass keine alte zweite CSV mit Loop-Zeilen aktiv ist. Die aktuelle Bridge verwendet für AutoLoop einen einmaligen Tastendruck. Wenn rekordbox den Loop weiterhin direkt abschaltet, teste zunächst Jog, Play/Pause, Cue und Load ohne Loop-Zuordnungen und sichere diesen funktionierenden Stand.

## Sicherung und Rückkehr zum stabilen Stand

Vor jeder Änderung sollten diese Dateien kopiert werden:

```text
config.json
terminal_mix8_rekordbox.py
PIONEER DDJ-SX.midi.csv
```

Eine empfehlenswerte Sicherung heißt beispielsweise:

```text
TM8_WORKING_BACKUP_YYYY-MM-DD
```

Wenn eine neue Funktionsgruppe Probleme verursacht, schließe Bridge und rekordbox und stelle alle drei Dateien aus der letzten funktionierenden Sicherung wieder her.

## Beenden

Im Bridge-Fenster:

```text
Ctrl+C
```

Falls `Ctrl+C` nicht reagiert, schließe das CMD-Fenster über das X. Danach sollte rekordbox beendet werden, bevor die MIDI-Konfiguration geändert wird.

## Lizenz und Hinweise

Dieses Projekt ist eine private, nicht-offizielle MIDI-Bridge. Es ist nicht mit Reloop, AlphaTheta, Pioneer DJ, rekordbox oder loopMIDI verbunden. Die MIDI-Zielcodes basieren auf dem verwendeten DDJ-SX-Rekordbox-Profil und können sich zwischen rekordbox-Versionen oder Profilen unterscheiden.
