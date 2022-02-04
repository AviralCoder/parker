import datetime


def time():
    now = datetime.datetime.now()
    if now.hour >= 5 and now.hour < 12:
        return "morning"
    elif now.hour >= 12 and now.hour < 17:
        return "afternoon"
    elif now.hour >= 17 and now.hour < 21:
        return "evening"
    elif now.hour >= 21 and now.hour < 00:
        return "night"
    elif now.hour >= 00 and now.hour < 5:
        return "late night"

def greet():
    time_ = time().capitalize()
    if time == "late night":
        return "Don't you think it is too late. Anyway"
    else:
        return f"Good {time_}"