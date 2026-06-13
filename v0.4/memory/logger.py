import os
from datetime import datetime

def log_time():
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    return time

def log(prompt, output, error):
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    log_path = os.path.join(BASE_DIR, "memory", "log.txt")
    
    with open(log_path, 'a', encoding="utf-8") as file:
        timestamp = log_time()
        file.write("=====================================\n")
        file.write(
            f"TIMESTAMP: {timestamp}\n"
            f"INPUT: {prompt}\n"
            f"OUTPUT: {output}\n"
            f"ERROR: {error}\n"
        )