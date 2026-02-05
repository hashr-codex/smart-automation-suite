import json
import os
from datetime import datetime


HISTORY_FILE = "run_log.json"

def save_run(moves):
    run_data ={
        "timestamp": datetime.now().isoformat(),
        "moves": moves
    }

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)

    else:
        history = []

    history.append(run_data)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def load_last_run():
    if not os.path.exists(HISTORY_FILE):
        raise FileNotFoundError("No history file found.")

    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)

    if not history:
        raise ValueError("No runs to undo")

    return history.pop(), history

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)