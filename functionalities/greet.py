import datetime


def greet():
    current_hour = int(datetime.datetime.now().hour)
    phrase = ""
    if current_hour >= 0 and current_hour < 12:
        phrase = "Good morning"
    elif current_hour >= 12 and current_hour < 17:
        phrase = "Good afternoon"
    else:
        phrase = "Good evening"
    return f"Hey dude !! {phrase}. Please tell me how can i help you?"
