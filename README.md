# Razer Snap Tap Emulator

Dieses Projekt ist ein Emulator für das Razer Snap Tap Feature, implementiert in Python mit einer grafischen Benutzeroberfläche.

## Beschreibung

Der Razer Snap Tap Emulator ahmt das Verhalten des Razer Snap Tap Features nach, das die Tastenpriorität bei gleichzeitigem Drücken entgegengesetzter Richtungstasten verändert. Es bietet zwei Modi:

1. Standard-Modus (Snap Tap aus): Wenn zwei entgegengesetzte Richtungstasten gleichzeitig gedrückt werden, wird keine Bewegung registriert.
2. Snap Tap-Modus (Snap Tap an): Die zuletzt gedrückte Taste hat Priorität, ermöglicht schnelle Richtungswechsel ohne Loslassen der anderen Taste.

## Features

- Konfigurierbare Tasten für Links- und Rechtsbewegung
- Einstellbarer Hotkey zum Ein- und Ausschalten von Snap Tap
- Grafische Benutzeroberfläche zur einfachen Konfiguration
- Echtzeit-Anzeige der aktuellen Bewegungsrichtung

## Installation

1. Stellen Sie sicher, dass Python 3.x auf Ihrem System installiert ist.
2. Klonen Sie dieses Repository:
   ```
   git clone https://github.com/yourusername/razer-snap-tap-emulator.git
   ```
3. Navigieren Sie in das Projektverzeichnis:
   ```
   cd razer-snap-tap-emulator
   ```
4. Installieren Sie die erforderlichen Abhängigkeiten:
   ```
   pip install pynput
   ```

## Verwendung

1. Starten Sie das Programm:
   ```
   python razer_snap_tap_emulator.py
   ```
2. Konfigurieren Sie die gewünschten Tasten und den Hotkey in der GUI.
3. Klicken Sie auf "Anwenden", um die Einstellungen zu übernehmen.
4. Aktivieren oder deaktivieren Sie Snap Tap mit der Checkbox oder dem konfigurierten Hotkey.
5. Testen Sie das Verhalten mit den konfigurierten Richtungstasten.

## Disclaimer

**Wichtiger Hinweis:** Dieser Emulator wurde entwickelt, ohne Zugang zu einer echten Razer-Tastatur zu haben. Das tatsächliche Verhalten des Razer Snap Tap Features konnte nicht direkt getestet oder verglichen werden. 

Die Implementierung basiert auf öffentlich verfügbaren Beschreibungen des Features. Es können Abweichungen vom Original-Feature vorhanden sein.

Wenn Sie eine Razer-Tastatur mit Snap Tap besitzen und Unterschiede zum echten Feature feststellen, würden wir uns sehr über Ihr Feedback freuen. Bitte öffnen Sie ein Issue oder kontaktieren Sie uns direkt, um zur Verbesserung dieses Emulators beizutragen.

## Beitragen

Beiträge zu diesem Projekt sind willkommen! Wenn Sie Verbesserungsvorschläge haben oder Fehler finden, zögern Sie bitte nicht, ein Issue zu öffnen oder einen Pull Request einzureichen.

## Lizenz

[MIT License](LICENSE)
