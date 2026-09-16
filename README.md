| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |# Reloop Terminal Mix 8 → rekordbox 6 MIDI-Bridge
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Diese Bridge übersetzt MIDI-Signale eines **Reloop Terminal Mix 8** in MIDI-Signale, die rekordbox über ein virtuelles loopMIDI-Gerät mit dem Profil **PIONEER DDJ-SX** verarbeiten kann.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Der aktuelle Stand ist für Windows 10/11 und rekordbox 6 ausgelegt. Er unterstützt zwei Jogwheels, Play/Pause, Cue, Load für Deck 1 und 2, den Tempo-Fader für Deck 1/2 sowie einen experimentellen Loop-Bereich. Die funktionierenden Kernfunktionen werden über einen kontrollierten Filter weitergegeben; unbekannte MIDI-Signale werden nicht an rekordbox gesendet.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |> **Wichtig:** Das Projekt verwendet ein virtuelles MIDI-Gerät. Der physische Terminal Mix 8 darf in rekordbox nicht zusätzlich als zweiter aktiver MIDI-Eingang für dieselben Funktionen gemappt werden.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## Funktionsumfang
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Funktion | Status | Beschreibung |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert ||---|---:|---|
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Jogwheel Deck 1 | Aktiv | Scratch/Rotation über DDJ-SX-Jog-Signal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Jogwheel Deck 2 | Aktiv | Scratch/Rotation über DDJ-SX-Jog-Signal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Jog-Touch | Aktiv | Touch-Signal für beide Decks |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Play/Pause Deck 1/2 | Aktiv | TM8 Note 5 wird auf Pioneer Note 11 übersetzt |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Cue Deck 1/2 | Aktiv | TM8 Note 4 wird auf Pioneer Note 12 übersetzt |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Load Deck 1/2 | Aktiv | TM8 Note 16 wird deckabhängig auf `96 46`/`96 47` übersetzt |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Tempo-Fader Deck 1/2 | Aktiv | 14-Bit-Pitchwheel wird als Pioneer-HiRes-CC 0 + CC 32 ausgegeben |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Kanal-Fader Deck 1–4 | Bereit zum Test | TM8 CC 15 wird auf Pioneer CC 19 übersetzt |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Crossfader | Bereit zum Test | TM8 Kanal 1/CC 43 wird auf Pioneer Kanal 7/CC 31 übersetzt |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Gain und EQ | Bereit zum Test | TM8 CC 9–12 werden auf Pioneer CC 4/7/11/15 übersetzt |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Loop-ON | Experimentell | AutoLoop an der aktuellen Position mit gewählter Loop-Länge |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Loop-Encoder | Experimentell | kleiner/größer über LoopHalf/LoopDouble |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Encoder-Druck | Absichtlich deaktiviert | erzeugt keine Aktion |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Pitch-Bend | Deaktiviert | wird nicht zum Jogwheel hinzugefügt |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## Roadmap und Mapping-Fortschritt
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Der Fortschritt wird nach **Funktionsgruppen des Terminal Mix 8** bewertet, nicht nach der Anzahl einzelner CSV-Zeilen. Eine Gruppe gilt erst als fertig, wenn das Eingangssignal identifiziert, die Bridge-Übersetzung implementiert, das Rekordbox-Profil angepasst und die Funktion am Controller getestet wurde.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### Gesamtfortschritt: **ca. 60 %**
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Bereich | Fortschritt | Status |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert ||---|---:|---|
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Jogwheels und Jog-Touch, Deck 1/2 | 100 % | Fertig und getestet |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Play/Pause, Deck 1/2 | 100 % | Fertig und getestet |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Cue, Deck 1/2 | 100 % | Fertig und getestet |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Load, Deck 1/2 | 100 % | Fertig und getestet |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Loop-ON/AutoLoop | 70 % | Signal und AutoLoop-Ziel bekannt; Rekordbox-Verhalten wird weiter abgesichert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Loop-Encoder Deck 2 | 50 % | Eingangssignal bekannt; LoopHalf/LoopDouble-Ausgabe noch in Validierung |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Loop-Encoder Deck 1 | 0 % | Encoder liefert im aktuellen Dump keine MIDI-Daten; Hardwareprüfung erforderlich |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Tempo-Fader und Tempo-Funktionen | 100 % | 14-Bit-Tempo-Fader implementiert und in rekordbox getestet |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Kanal-Fader, Crossfader und EQ | 50 % | Rohsignale identifiziert und Bridge-Übersetzung implementiert; Controller-Test steht noch aus |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Pads, Hot Cues und Sampler | 0 % | Noch nicht aufgenommen und getestet |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || FX-Regler und FX-Tasten | 0 % | Noch nicht aufgenommen und getestet |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Browser, Track-Auswahl und weitere Bedienelemente | 0 % | Noch nicht aufgenommen und getestet |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### Nächste Schritte
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |1. **Loop-ON und Loop-Encoder stabilisieren**, ohne den funktionierenden Transport- und Jogwheel-Bereich zu verändern.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |2. **Mixer-Bereich** mit Kanal-Fadern, Crossfader, Gain und EQ mit der neuen Bridge-Version testen und danach als fertig markieren.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |3. **Pads und Hot Cues** pro Deck aufnehmen und testen.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |4. **FX- und Browser-Bereich** ergänzen.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |5. Nach jeder Gruppe eine versionierte Sicherung erstellen und alle bereits fertigen Funktionen erneut testen.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |> Die Prozentangabe ist eine technische Projektanzeige und keine Garantie für eine bestimmte rekordbox-Version. MIDI-Profile können sich zwischen rekordbox-Versionen unterscheiden; jede neue Gruppe muss deshalb auf dem Zielsystem getestet werden.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## MIDI-Signalübersicht
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### Reloop Terminal Mix 8 → Bridge
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || TM8-Funktion | Rohsignal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert ||---|---|
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Jog Deck 1 drehen | Kanal 1, CC 7 |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Jog Deck 2 drehen | Kanal 2, CC 7 |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Jog-Touch Deck 1 | Kanal 1, Note 7 |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Jog-Touch Deck 2 | Kanal 2, Note 7 |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Play/Pause | Note 5 auf dem jeweiligen Deck-Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Cue | Note 4 auf dem jeweiligen Deck-Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Load | Note 16 auf dem jeweiligen Deck-Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Loop-Encoder Deck 2 | Kanal 2, CC 29, Werte 63/65 |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Loop-ON | Note 30 auf dem jeweiligen Deck-Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Tempo-Fader | Pitchwheel auf dem jeweiligen TM8-Deck-Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### Bridge → rekordbox/DDJ-SX-Profil
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Funktion | Zielsignal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert ||---|---|
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Jog Rotation | CC 34 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Jog-Touch | Note 54 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Play/Pause | Note 11 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Cue | Note 12 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Load Deck 1 | `96 46` |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Load Deck 2 | `96 47` |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || AutoLoop | Note 20 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Loop kleiner | Note 18 |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Loop größer | Note 19 |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Tempo-Fader MSB | CC 0 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Tempo-Fader LSB | CC 32 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Kanal-Fader | CC 19 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Crossfader | CC 31 auf Kanal 7 |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || Gain | CC 4 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || EQ High | CC 7 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || EQ Mid | CC 11 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert || EQ Low | CC 15 auf dem jeweiligen Kanal |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## Voraussetzungen
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |- Windows 10 oder Windows 11
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |- Reloop Terminal Mix 8 mit USB-Verbindung
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |- rekordbox 6
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |- loopMIDI
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |- Python 3.11 oder 3.12
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |- Python-Pakete aus `requirements.txt`
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## Installation
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### 1. loopMIDI installieren
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Installiere loopMIDI von der offiziellen Tobias-Erichsen-Webseite. Erstelle anschließend genau einen virtuellen Port mit dem Namen:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |PIONEER DDJ-SX
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Der Name muss exakt übereinstimmen. Groß-/Kleinschreibung ist normalerweise unkritisch, zusätzliche Leerzeichen oder ein anderer Name können aber dazu führen, dass die Bridge den Ausgang nicht findet.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### 2. Bridge-Ordner anlegen
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Entpacke das Repository beispielsweise nach:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |C:\DJ\DJ Tools\terminal_mix8_rekordbox
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |In diesem Ordner müssen mindestens diese Dateien liegen:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |terminal_mix8_rekordbox.py
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |config.json
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |requirements.txt
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |PIONEER DDJ-SX.midi.csv
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### 3. Python-Abhängigkeiten installieren
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Öffne eine Eingabeaufforderung im Bridge-Ordner und führe aus:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```bat
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |py -3.12 -m pip install -r requirements.txt
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Falls Python 3.11 installiert ist, kann stattdessen verwendet werden:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```bat
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |py -3.11 -m pip install -r requirements.txt
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### 4. Rekordbox-MIDI-Profil installieren
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Kopiere ausschließlich diese Datei in den rekordbox-MIDI-Mappings-Ordner:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |PIONEER DDJ-SX.midi.csv
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Ein typischer Pfad ist:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |C:\Program Files\Pioneer\rekordbox 6\MidiMappings\
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Je nach Installation kann der Versionsordner anders heißen. Suche bei Bedarf im rekordbox-Installationsordner nach `MidiMappings`.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Vor dem Ersetzen sollte die vorhandene Datei gesichert werden:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |PIONEER DDJ-SX.midi.csv.original.backup
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### 5. Rekordbox und Bridge vollständig neu starten
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Nach dem Kopieren der CSV muss rekordbox vollständig beendet und neu gestartet werden. Ein bloßes Schließen des MIDI-Fensters reicht nicht immer aus.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## Start
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Die empfohlene Startreihenfolge lautet:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |1. Terminal Mix 8 per USB anschließen.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |2. loopMIDI starten und den Port `PIONEER DDJ-SX` aktivieren.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |3. Eine Eingabeaufforderung im Bridge-Ordner öffnen.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |4. Bridge starten:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```bat
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |py -3.12 terminal_mix8_rekordbox.py --config config.json --debug
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Erwartete Ausgabe:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |IN : Terminal Mix 8 0
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |OUT: PIONEER DDJ-SX 2
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Bridge aktiv. Beenden: Ctrl+C
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |5. Erst jetzt rekordbox starten.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |6. In rekordbox das Profil `PIONEER DDJ-SX` auswählen.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## Bedienung und Testreihenfolge
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Nach dem Start sollten die Funktionen in dieser Reihenfolge geprüft werden:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |1. Play/Pause Deck 1 und Deck 2
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |2. Cue Deck 1 und Deck 2
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |3. Load Deck 1 und Deck 2
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |4. Jogwheel Deck 1
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |5. Jogwheel Deck 2
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |6. Loop-Länge auf einen Wert wie 8 Beats stellen
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |7. Loop-ON-Taste testen
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |8. Loop-Encoder langsam nach links und rechts drehen
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Die Debug-Ausgabe zeigt übersetzte Nachrichten. Beispiele:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |TRANSPORT IN [144, 5, 127] -> OUT [144, 11, 127]
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |TRANSPORT IN [144, 4, 127] -> OUT [144, 12, 127]
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Jogwheel-Ausgaben sehen beispielsweise so aus:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |JOG IN [176, 7, 65] -> OUT [176, 34, 65]
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Loop-Ausgaben sehen beispielsweise so aus:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |LOOP IN [144, 30, 127] -> OUT [[144, 20, 127]]
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## Wichtige rekordbox-Einstellungen
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Der physische Eingang `Terminal Mix 8` darf nicht zusätzlich parallel zum virtuellen `PIONEER DDJ-SX`-Eingang dieselben Transportfunktionen steuern. Der empfohlene Signalweg ist:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Terminal Mix 8 → Bridge → loopMIDI PIONEER DDJ-SX → rekordbox
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Nicht empfohlen ist:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Terminal Mix 8 → rekordbox
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Terminal Mix 8 → Bridge → rekordbox
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Das parallele Aktivieren beider Wege kann Play/Pause doppelt auslösen oder einen Track sofort wieder starten.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## Fehlerbehebung
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### `Kein Treffer für 'PIONEER DDJ-SX'`
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Prüfe, ob loopMIDI geöffnet ist und der Port exakt so heißt:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |PIONEER DDJ-SX
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Zeige die verfügbaren Ports an mit:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```bat
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |py -3.12 terminal_mix8_rekordbox.py --list
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### `MidiInWinMM::openPort: error creating Windows MM MIDI input port`
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Der Terminal Mix 8 wird wahrscheinlich bereits von einem zweiten Programm geöffnet. Schließe rekordbox, Serato, Mixxx, die Bridge und andere MIDI-Monitor-Programme. Starte anschließend nur die Bridge neu.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### Jogwheel funktioniert im CMD, aber nicht in rekordbox
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Prüfe:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |1. Liegt `PIONEER DDJ-SX.midi.csv` im richtigen `MidiMappings`-Ordner?
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |2. Wurde rekordbox nach dem Kopieren vollständig neu gestartet?
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |3. Ist in rekordbox das Profil `PIONEER DDJ-SX` aktiv?
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |4. Wird wirklich nur der virtuelle Port verwendet?
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |5. Zeigt die Bridge `OUT: PIONEER DDJ-SX` an?
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### Play/Pause startet sofort wieder
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Bridge und rekordbox schließen. Prüfe, dass kein zweites direktes Terminal-Mix-8-Mapping aktiv ist. Verwende außerdem nur eine einzige `PIONEER DDJ-SX.midi.csv` im aktiven `MidiMappings`-Ordner.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |### Loop geht direkt wieder aus
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Prüfe, dass keine alte zweite CSV mit Loop-Zeilen aktiv ist. Die aktuelle Bridge verwendet für AutoLoop einen einmaligen Tastendruck. Wenn rekordbox den Loop weiterhin direkt abschaltet, teste zunächst Jog, Play/Pause, Cue und Load ohne Loop-Zuordnungen und sichere diesen funktionierenden Stand.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## Sicherung und Rückkehr zum stabilen Stand
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Vor jeder Änderung sollten diese Dateien kopiert werden:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |config.json
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |terminal_mix8_rekordbox.py
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |PIONEER DDJ-SX.midi.csv
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Eine empfehlenswerte Sicherung heißt beispielsweise:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |TM8_WORKING_BACKUP_YYYY-MM-DD
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Wenn eine neue Funktionsgruppe Probleme verursacht, schließe Bridge und rekordbox und stelle alle drei Dateien aus der letzten funktionierenden Sicherung wieder her.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## Beenden
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Im Bridge-Fenster:
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```text
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Ctrl+C
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |```
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Falls `Ctrl+C` nicht reagiert, schließe das CMD-Fenster über das X. Danach sollte rekordbox beendet werden, bevor die MIDI-Konfiguration geändert wird.
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |## Lizenz und Hinweise
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |
| Gain und EQ | Implementiert || Crossfader | Implementiert || Kanal-Fader Deck 1–4 | Implementiert |Dieses Projekt ist eine private, nicht-offizielle MIDI-Bridge. Es ist nicht mit Reloop, AlphaTheta, Pioneer DJ, rekordbox oder loopMIDI verbunden. Die MIDI-Zielcodes basieren auf dem verwendeten DDJ-SX-Rekordbox-Profil und können sich zwischen rekordbox-Versionen oder Profilen unterscheiden.
