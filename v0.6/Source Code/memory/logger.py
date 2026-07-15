import os
import sys

from datetime import datetime

def log_time():
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    return time

def log(prompt, output, error):

    if getattr(sys, "frozen", False):
        BASE_DIR = os.path.dirname(sys.executable)
    else:
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    memory_dir = os.path.join(BASE_DIR, "memory")
    os.makedirs(memory_dir, exist_ok=True)

    log_path = os.path.join(memory_dir, "log.txt")

    with open(log_path, "a", encoding="utf-8") as file:
        timestamp = log_time()
        file.write("=====================================\n")
        file.write(
            f"TIMESTAMP: {timestamp}\n"
            f"INPUT: {prompt}\n"
            f"OUTPUT: {output}\n"
            f"ERROR: {error}\n"
        )
