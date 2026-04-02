import tkinter as tk
import json
from datetime import datetime

LOG_FILE = "keystrokes_words.json"

current_word = ""
logs = []

def log_key(event):
    global current_word

    # If it's a normal character
    if event.char.isprintable() and event.keysym != "space":
        current_word += event.char

    # If space or enter → save word
    elif event.keysym in ["space", "Return"]:
        if current_word:
            logs.append({
                "word": current_word,
                "timestamp": datetime.now().isoformat()
            })
            save_logs()
            current_word = ""

    # Handle backspace
    elif event.keysym == "BackSpace":
        current_word = current_word[:-1]

def save_logs():
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

# GUI
root = tk.Tk()
root.title("Keylogger Demo - Word Capture")

label = tk.Label(root, text="Type here (Words will be logged)", font=("Arial", 14))
label.pack(pady=20)

text = tk.Text(root, height=10, width=50)
text.pack(pady=20)

text.bind("<Key>", log_key)

root.mainloop()