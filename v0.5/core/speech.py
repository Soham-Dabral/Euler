import pyttsx3

def speak(text: str):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170) #Speech Speed
    engine.say(text)
    engine.runAndWait()
