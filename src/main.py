# --- 3rd Party ---
import customtkinter as  ctk

# --- Build-in ---
import os
import json

# --- Local ---
from src.utils import Logger, Util

config_json = 'src/data/config.json'
Util.find_path(config_json)

with open('src/data/config.json', 'r') as f:
    config = json.load(f)

class App:
    def __init__(self):
        ...
@Util.timer
def main():
    ...