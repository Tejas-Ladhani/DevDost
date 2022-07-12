from functionalities.greet import greet
from functionalities.open_application import openApplication
from functionalities.speak import speak
from functionalities.listen import listen


if __name__ == "__main__":
    # speak("Hello dude")
    speak(greet())

    while True:
        try:
            query = listen().lower()
            openApplication(query)
        except Exception as exc:
            pass
            # speak("what was that! please say it again.")
