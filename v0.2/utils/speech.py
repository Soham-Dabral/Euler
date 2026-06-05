import pyttsx3

engine =pyttsx3.init()
engine.setProperty("rate", 170) #Speech Speed

def speak(text: str):
    engine.say(text)
    engine.runAndWait()