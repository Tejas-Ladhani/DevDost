import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
