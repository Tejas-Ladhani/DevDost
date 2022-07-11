import os
from requests import get
from functionalities.speak import speak
from functionalities.listen import listen
import wikipedia
import webbrowser
import sys

def openApplication(query):

    if "open notepad" in query:
        path = "C:\\Windows\\system32\\notepad.exe"
        if os.path.exists("C:\\Windows\\system32\\notepad.exe"):
            os.startfile(path)
            speak("Okay!! done.")

    if "open vs code" in query:
        speak("here you go !")
        os.system("code")

    if (
        "open command prompt" in query
        or "open cmd" in query
        or "open terminal" in query
    ):
        speak("why not, here is your command prompt.")
        os.system("start cmd")
        print("CMD")

    if "what's my ip" in query or "my ip" in query:
        my_ip = get("https://api.ipify.org").text
        speak(f"your ip address is {my_ip}")

    """
    example:
    🗣 : what is python according to wikipedia.
    query.replace() -> removes "wikipedia" from query and searches it to wikipedia

    """
    if "wikipedia" in query or "wiki" in query:
        speak("okay, searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia,")
        print(f"📩 {results}")
        speak(results)

    """
    handling all/around youtube
    """
    if (
        "search youtube" in query
        or "search in youtube" in query
        or "search on youtube" in query
    ):
        toSearch = query.replace("youtube", "")
        toSearch = query.replace("in", "")
        toSearch = query.replace("on", "")
        toSearch = toSearch.replace("search", "")
        speak("taking you to the... not moon but youtube!")
        webbrowser.open_new_tab(
            f"https://www.youtube.com/results?search_query={toSearch}"
        )
    elif "open youtube" in query:
        speak("okay, my lordship!")
        webbrowser.open_new_tab("www.youtube.com")

    """
    Handles all/around stackoverflow
    """
    if (
        "search stackoverflow" in query
        or "searching on stackoverflow" in query
        or "search in stackoverflow" in query
        or "search on stackoverflow" in query
    ):
        toSearch = query.replace("stackoverflow", "")
        toSearch = toSearch.replace("search", "")
        speak("Yo, taking you to the stackoverflow")
        webbrowser.open_new_tab(f"https://stackoverflow.com/search?q={toSearch}")
    elif "stackoverflow" in query:
        speak("here, it is!")
        webbrowser.open_new_tab("https://stackoverflow.com/")

    """
    browser
    """
    if "search browser" in query:
        speak("what should I search ?")
        toSearch = listen().lower()
        speak("Okay, here you go!")
        webbrowser.open_new_tab(f"https://www.google.co.in/search?q={toSearch}")
    elif "open browser" in query or "start browser" in query:
        speak("Okay!")
        webbrowser.open_new_tab("https://www.google.com")

    if "no thanks" in query:
        speak("Okay, have a good day!")
        sys.exit(1)

    # speak("Dude, any more work for me ?")
    """
    whatsapp
    """

    """
    send email, any updates ? etc
    """

    """
    any updates from social media -> Linkedin Twitter Instagram
    """