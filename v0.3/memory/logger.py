import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, "log.txt")

#Returns date and time for log
def log_date_time():
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    date = now.strftime("%d %B %Y")
    date_time = f"{date}, {time}"
    return date_time

def log(prompt, output, errors):
    timestamp = log_date_time()
    log_file = open(LOG_PATH, "a")
    log_file.write("===================================================\n")
    log_file.write(f"TIME: {timestamp} \nINPUT: {prompt} \nOUTPUT: {output} ERRORS: {errors}\n")
    log_file.close()