English is below
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
   git clone https://github.com/justinsanjp/snaptab-emulator.git
   ```
3. Navigieren Sie in das Projektverzeichnis:
   ```
   cd snaptab-emulator
   ```
4. Installieren Sie die erforderlichen Abhängigkeiten:
   ```
   pip install pynput
   ```

## Verwendung

1. Starten Sie das Programm:
   ```
   python app.py
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

Razer Snap Tap Emulator
This project is an emulator for the Razer Snap Tap feature, implemented in Python with a graphical user interface.

Description
The Razer Snap Tap Emulator mimics the behavior of the Razer Snap Tap feature, which changes button priority when opposite directional keys are pressed simultaneously. It offers two modes:

Standard Mode (Snap Tap off): When two opposite directional keys are pressed at the same time, no movement is registered.
Snap Tap Mode (Snap Tap on): The last key pressed takes priority, allowing quick direction changes without releasing the other key.
Features
Configurable keys for left and right movement
Settable hotkey to toggle Snap Tap on and off
Graphical user interface for easy configuration
Real-time display of the current movement direction
Installation
Ensure Python 3.x is installed on your system.
Clone this repository:
bash
コードをコピーする
git clone https://github.com/justinsanjp/snaptab-emulator.git
Navigate to the project directory:
bash
コードをコピーする
cd snaptab-emulator
Install the required dependencies:
bash
コードをコピーする
pip install pynput
Usage
Start the program:
bash
コードをコピーする
python app.py
Configure the desired keys and hotkey in the GUI.
Click "Apply" to save the settings.
Enable or disable Snap Tap using the checkbox or the configured hotkey.
Test the behavior with the configured directional keys.
Disclaimer
Important Notice: This emulator was developed without access to an actual Razer keyboard. The actual behavior of the Razer Snap Tap feature could not be directly tested or compared.

The implementation is based on publicly available descriptions of the feature, so there may be deviations from the original functionality.

If you own a Razer keyboard with Snap Tap and notice differences from the real feature, we would greatly appreciate your feedback. Please open an issue or contact us directly to help improve this emulator.

Contributing
Contributions to this project are welcome! If you have suggestions for improvements or find any bugs, please don't hesitate to open an issue or submit a pull request.

License
[MIT License](LICENSE)
