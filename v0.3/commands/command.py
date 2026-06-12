from datetime import datetime
from datetime import timedelta
from core.speech import speak
import time

#Returns the current time
def current_time():
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    return time

#Returns the current date
def current_date():
    now = datetime.now()
    date = now.strftime("%d %B %Y")
    day = datetime.strptime(date, "%d %B %Y")
    today = day.strftime("%A") + " " + date
    return today

#Sets timer
def set_timer(sec: int):
    now = datetime.now()
    end_time = now + timedelta(seconds = sec)
    while datetime.now() < end_time:
       time.sleep(0.2)
    speak("Sir, your timer has competed")
    return "completed"