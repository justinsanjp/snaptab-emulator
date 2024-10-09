import tkinter as tk
from tkinter import ttk
from pynput import keyboard

class RazerSnapTapEmulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Razer Snap Tap Emulator")
        self.master.geometry("400x300")

        self.key_left = tk.StringVar(value="a")
        self.key_right = tk.StringVar(value="d")
        self.hotkey = tk.StringVar(value="<ctrl>+<alt>+l")
        self.is_active = tk.BooleanVar(value=False)

        self.create_widgets()

        self.listener = None
        self.current_direction = None
        self.keys_pressed = set()
        self.start_listener()

    def create_widgets(self):
        ttk.Label(self.master, text="Linke Taste:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self.master, textvariable=self.key_left).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.master, text="Rechte Taste:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(self.master, textvariable=self.key_right).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.master, text="Hotkey:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Entry(self.master, textvariable=self.hotkey).grid(row=2, column=1, padx=5, pady=5)

        ttk.Checkbutton(self.master, text="Snap Tap Aktiv", variable=self.is_active).grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(self.master, text="Anwenden", command=self.apply_settings).grid(row=4, column=0, columnspan=2, pady=10)

        self.direction_label = ttk.Label(self.master, text="Aktuelle Richtung: Keine")
        self.direction_label.grid(row=5, column=0, columnspan=2, pady=10)

    def apply_settings(self):
        if self.listener:
            self.listener.stop()
        self.start_listener()

    def toggle_active(self):
        self.is_active.set(not self.is_active.get())
        print(f"Razer Snap Tap ist {'aktiv' if self.is_active.get() else 'inaktiv'}")

    def on_press(self, key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)

        if self.is_hotkey(key):
            self.toggle_active()
            return

        if key_char in [self.key_left.get(), self.key_right.get()]:
            self.keys_pressed.add(key_char)
            self.update_direction()

    def on_release(self, key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)

        if key_char in self.keys_pressed:
            self.keys_pressed.remove(key_char)
            self.update_direction()

    def update_direction(self):
        if self.is_active.get():
            # Snap Tap aktiv: Priorisiere die zuletzt gedrückte Taste
            if self.key_right.get() in self.keys_pressed:
                self.set_direction("Rechts")
            elif self.key_left.get() in self.keys_pressed:
                self.set_direction("Links")
            else:
                self.set_direction(None)
        else:
            # Snap Tap inaktiv: Standard-Verhalten
            if self.key_left.get() in self.keys_pressed and self.key_right.get() in self.keys_pressed:
                self.set_direction(None)
            elif self.key_right.get() in self.keys_pressed:
                self.set_direction("Rechts")
            elif self.key_left.get() in self.keys_pressed:
                self.set_direction("Links")
            else:
                self.set_direction(None)

    def set_direction(self, direction):
        if direction != self.current_direction:
            self.current_direction = direction
            self.update_direction_display()
            print(f"Richtung: {direction if direction else 'Keine'}")

    def update_direction_display(self):
        self.direction_label.config(text=f"Aktuelle Richtung: {self.current_direction if self.current_direction else 'Keine'}")

    def is_hotkey(self, key):
        hotkey_parts = self.hotkey.get().lower().split('+')
        return all(k in str(key).lower() for k in hotkey_parts)

    def start_listener(self):
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = RazerSnapTapEmulator(root)
    root.mainloop()