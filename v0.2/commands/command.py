from datetime import datetime
from datetime import timedelta
import time
from utils.speech import speak

#Returns the current time
def current_time():
    now = datetime.now()
    time = now.strftime("%I:%M %p")
    return (f"Sir, current time is {time}")

#Returns the current date
def current_date():
    now = datetime.now()
    date = now.strftime("%d %B %Y")
    day = datetime.strptime(date, "%d %B %Y")
    today = day.strftime("%A") + " " + date
    return (f"Sir, today's date is {today}")

#Sets timer
def set_timer(sec: int):
    now = datetime.now()
    end_time = now + timedelta(seconds = sec)
    while datetime.now() < end_time:
       time.sleep(0.2)
    speak("Sir, your timer has completed")
    # if datetime.now() >= end_time:
    return "Sir, your timer has completed"