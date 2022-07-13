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
    return f"Hi,{phrase}. I am Dev Dost. It's {datetime.datetime.today().strftime('%I:%M %p')}. Please tell me how can i help you?"
