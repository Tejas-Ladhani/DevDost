from email.mime import audio
import speech_recognition as sr


def listen():
    recognizor = sr.Recognizer()
    with sr.Microphone() as source:
        print("👂Listening...")
        recognizor.pause_threshold = 1
        audio = recognizor.listen(source=source, timeout=2, phrase_time_limit=5)

        try:
            print("🧠 recognizing")
            query = recognizor.recognize_google(audio, language="en-in")
            print(f"🗣 : {query}")

        except Exception as exc:
            # Not handling the exception here, leaving it on the utilizer of this function, to give custom feedback to the user.
            raise Exception(exc)

        return query
