import sys
from click import command
from functionalities.greet import greet
from functionalities.open_application import openApplication
from functionalities.speak import speak
from functionalities.listen import listen


def execute():
    speak(greet())

    while True:
        try:
            query = listen().lower()
            if "sleep now" in query or "please sleeep" in query or "can sleep" in query:
                speak("okay, sleeping now. please let know, if you need anything!")
                break
            openApplication(query)
        except Exception as exc:
            print("Are you saying anything ?")
            # speak("what was that! please say it again.")


if __name__ == "__main__":
    # speak("Hello dude")
    while True:
        try:
            command = listen().lower()
            if (
                "bye" in command
                or "stop dev dost" in command
                or "stop dd" in command
                or "stop d d" in command
                or "top d d" in command
                or "terminate yourself" in command
            ):
                speak("Okay, Thank you. It was nice to assist you.")
                break
            elif (
                "hey d d" in command
                or "hello" in command
                or "hi d d" in command
                or "hi didi" in command
                or "hey devdost" in command
                or "devdost" in command
                or "hey assistant" in command
                or "hola devdost" in command
                or "what's up devdost" in command
                or "dev dost" in command
                or "dev friend" in command
            ):
                execute()
        except:
            print("Please say something 🙄😫")
