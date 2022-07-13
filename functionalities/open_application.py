from datetime import datetime
import os
import random
from time import sleep, time
from PyPDF2 import PdfReader
import PyPDF2
from requests import get, request
import requests
from functionalities.speak import speak
from functionalities.listen import listen
import wikipedia
import webbrowser
import sys
import pyjokes
import pywhatkit
import pyautogui


def openApplication(query):

    if "open notepad" in query:
        path = "C:\\Windows\\system32\\notepad.exe"
        if os.path.exists("C:\\Windows\\system32\\notepad.exe"):
            os.startfile(path)
            speak("Okay!! done.")

    elif "open vs code" in query:
        speak("here you go !")
        os.system("code")

    elif (
        "open command prompt" in query
        or "open cmd" in query
        or "open terminal" in query
    ):
        speak("why not, here is your command prompt.")
        os.system("start cmd")
        print("CMD")

    elif "what's my ip" in query or "my ip" in query:
        my_ip = get("https://api.ipify.org").text
        speak(f"your ip address is {my_ip}")

    elif (
        "my location" in query
        or "where i am" in query
        or "am i at my home" in query
        or "am i at" in query
        or "what is this place" in query
        or "current location" in query
    ):
        speak("Okay, Let me check")
        try:
            my_ip = get("https://api.ipify.org").text
            locationURL = f"https://ipapi.co/{my_ip}/json"
            geo_requests = requests.get(locationURL)
            geo_data = geo_requests.json()
            city = geo_data["city"]
            state = geo_data["region"]
            country = geo_data["country_name"]
            postal_code= geo_data['postal']
            speak(f"Not sure, but it seems, you are around {city}, {state}, {country}, but the postal code is {postal_code}")
        except:
            speak("seems, there is a connectivity issue. Please try again")
    elif (
        "wikipedia" in query
        or "wiki" in query
        or "tell me about" in query
        or "who is" in query
        or "what is" in query
        or "tell me something about" in query
    ):

        speak("okay, searching wikipedia...")
        # replacing things if matches any or multiple.

        """
        example:
        🗣 : what is python according to wikipedia.
        query.replace() -> removes "wikipedia" from query and searches it to wikipedia
        """
        query = query.replace("wikipedia", "")
        query = query.replace("wiki", "")
        query = query.replace("tell me about", "")
        query = query.replace("who is", "")
        query = query.replace("tell me something about", "")
        query = query.replace("what is", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia,")
        print(f"📩 {results}")
        speak(results)

        """
        handling all/around youtube
        """
    elif (
        "youtube" in query
        or "search youtube" in query
        or "search in youtube" in query
        or "search on youtube" in query
    ):
        speak("Okay, what should i search?")
        toSearch = ""
        while toSearch == "":
            try:
                toSearch = listen()
            except Exception:
                speak("can you please repeat")
        temp = toSearch.split("search")
        # toSearch = toSearch.replace("search", "")
        toSearch = temp[1]
        speak("taking you to the... not moon but youtube!")
        webbrowser.open_new_tab(
            f"https://www.youtube.com/results?search_query={toSearch}"
        )
    elif "open youtube" in query:
        speak("okay, my lordship!")
        webbrowser.open_new_tab("www.youtube.com")
    elif (
        "play on youtube" in query
        or "music on youtube" in query
        or "on youtube" in query
        or "play youtube" in query
        or "play music" in query
        or "play song" in query
        or "play some song" in query
        or "some song" in query
        or "some music" in query
        or "play some music" in query
    ):
        speak("Okay, what should i play on youtube ?")
        whomToPlay = listen()
        pywhatkit.playonyt(whomToPlay if whomToPlay != "" else "arjit singh")

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
    """
    Jokes
    """
    if (
        "i am sad" in query
        or "i am unhappy" in query
        or "tell me some joke" in query
        or "joke" in query
        or "jokes" in query
        or "laugh" in query
    ):
        speak(random.choice(["let me make you happy", "here is one joke for you."]))
        joke = pyjokes.get_joke()
        speak(joke)

    """
    close running applications
    system shutdown, sleep, logout
    """
    if "close notepad" in query:
        speak("Okay, closing notepad.")
        os.system("taskkill /im notepad.exe")
    elif "close chrome" in query:
        speak("Okay, closing chrome.")
        os.system("taskkill /im chrome.exe")
    elif "close command prompt" in query or "close cmd" in query:
        speak("Okay, closing command prompt.")
        os.system("taskkill /im cmd.exe")
    elif "close vs code" in query:
        speak("sure, closing vs code.")
        os.system("taskkill /im code.exe")
    elif (
        "restart the pc" in query
        or "restart machine" in query
        or "restart pc" in query
        or "restart my machine" in query
        or "restart computer" in query
        or "restart the system" in query
        or "restart my laptop" in query
        or "machine restart" in query
        # or "restart" in query
    ):
        speak("Okay, restarting machine in 10 seconds")
        os.system("shutdown /r /t 10")
    elif (
        "sleep the pc" in query
        or "sleep machine" in query
        or "sleep pc" in query
        or "sleep my machine" in query
        or "sleep computer" in query
        or "sleep the system" in query
        or "sleep my laptop" in query
        or "pc sleep" in query
    ):
        speak("Okay, making pc sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    # speak("Dude, any more work for me ?")

    elif (
        "read pdf" in query
        or "read me a pdf" in query
        or "read a pdf" in query
        or "read the pdf" in query
        or "read book" in query
    ):
        speak("Okay Boss! Please Enter the path of that PDF")
        try:
            path = pyautogui.prompt("Please Enter the path", "PDF Path | DevDost")
            print(path)
            pdfFile = open(path, "rb")
            PdfReader = PyPDF2.PdfFileReader(pdfFile)
            numberOfPages = int(PdfReader.numPages)
            print(numberOfPages)
            speak(f"Total number of pages in this book is {numberOfPages}")
            speak("Please help me with the page number, that i have to read")
            try:
                pageNumberToRead = int(
                    pyautogui.prompt("Enter the page Number", "PDF | DevDost")
                )
                print(pageNumberToRead)
                if pageNumberToRead >= 0 and pageNumberToRead <= numberOfPages:
                    speak(f"Reading page {pageNumberToRead} for you")
                    page = PdfReader.getPage(pageNumberToRead - 1)
                    content = page.extractText()
                    speak(content.lower())
            except:
                speak("Please enter number only. please invoke the command again!")
        except:
            speak("Some Error ocurred! Probably you entered a invalid path or file.")
            print("💀 Some Error ocurred.")

    if (
        "message on whatsapp" in query
        or "whatsapp message" in query
        or "ping on whatsapp" in query
        or "on whatsapp" in query
        or "in whatsapp" in query
    ):
        speak("okay, to which number should we send ? please enter.")
        contact = pyautogui.prompt(
            "Please Enter the number", title="From DevDost | Number"
        )
        speak("okay. Now, what should be the message")
        message = pyautogui.prompt(
            "Please Enter the Message", title="From DevDost | Message"
        )
        pywhatkit.sendwhatmsg(
            contact,
            message,
            time_hour=int(datetime.now().hour),
            time_min=(int(datetime.now().minute) + 1),
        )
        speak("sent!")

    """
    switch tabs
    """
    if (
        "switch tab" in query
        or "one more tab" in query
        or "switch window" in query
        or "switch once more" in query
        or "switch the tab" in query
        or "switch the window" in query
        or "switch the screen" in query
        or "next tab" in query
        or "next window" in query
        or "next screen" in query
    ):
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        sleep(1)
        pyautogui.keyUp("alt")

    """
    take screenshot
    """
    if (
        "take screenshot" in query
        or "capture the screen" in query
        or "have the screenshot" in query
        or "capture screen" in query
        or "have screenshot" in query
        or "save screenshot" in query
        or "take ss" in query
        or "capture the ss" in query
        or "have the ss" in query
        or "capture ss" in query
        or "have ss" in query
        or "save ss" in query
    ):
        speak("okay!!")
        if not os.path.isdir("./generated_ss"):
            os.mkdir("./generated_ss")

        pyautogui.screenshot(
            f"./generated_ss/devDost_ss_{(random.randint(1,1000)*random.randint(1,10))}.png"
        )
        speak("Screenshot saved.")
        # pyautogui.press('prtscr')
        # try:
        #     os.system("start mspaint.exe")
        #     sleep(1)
        #     pyautogui.keyDown('ctrl')
        #     pyautogui.keyDown('v')
        #     sleep(1)
        #     pyautogui.keyUp('ctrl')
        #     pyautogui.keyUp('v')

        # except Exception:
        #     print("😟 some error occurred")

        # screenshot = pyautogui.screenshot()
        # screenshot.save(f"./new/DevDost_ss_{datetime.now()}.png")
    """
    send email, any updates ? etc
    """

    """
    any updates from social media -> Linkedin Twitter Instagram (scrapping or automation selenium)
    """

    """
    alarms - local + remote
    """

    """
    weather
    """

    """
    save the code === git add . + git commit
    push the code === git push
    fetch
    pull
    status

    """
