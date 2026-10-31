# --- 3rd Party ---
import customtkinter as ctk

# --- Built-in ---
import sys
import json
import logging

# --- Local ---
from src.utils import Util

config_json = 'src/data/config.json'
if not Util.find_path(config_json):
    sys.exit(1)

with open(config_json, 'r') as f:
    config = json.load(f)

class Tap(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("home")
        self.add("placeholder")

        self.label = ctk.CTkLabel(master=self.tab("home"))
        self.label.grid(row=0, column=0, padx=20, pady=10)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(config["root"].get("geometry", "300x600"))
        self.title(config["root"].get("title", "Keycaps"))

        self.grid_columnconfigure((0,1,2,3),weight=1)
        self.grid_rowconfigure((0,1,2),weight=1)

        self.tab_view = Tap(master=self)
        self.tab_view.grid(row=0, column=0, padx=10, pady=10)

@Util.timer
def main():
    try:
        app = App()
        ctk.set_appearance_mode(config["root"].get("appearance", "System"))
        app.mainloop()
    except KeyboardInterrupt:
        logging.shutdown()
        sys.exit(0)
    except Exception as e:
        logging.shutdown()
        print(f"Unexpected error: {e}")
        sys.exit(1)