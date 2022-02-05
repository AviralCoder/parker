# IF ANY CODE IS WRITTEN BADLY, PLEASE DON'T JUDGE ME,
#  I AM NOT FAMILIAR WITH PYTHON, THIS IS MY FIRST TIME, 
# I USUALLY ONLY CODE JAVASCRIPT (REACT JS, 
# HTML, CSS, SCSS, Node.js, Express, TypeScript, Stuff...)

from functions.loadData import loadData
from functions.wish import greet
from lib.list import app_paths
import webbrowser
import pyttsx3
import time
import os
import speech_recognition as sr
from lib.list import feedback_phrases, positive_words, negative_words

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[38].id)

# IMPORTANT VARIABLES
DEBUGGING = False

details: dict = loadData("./lib/credentials.json")

def speak(speech: str):
    print(speech)
    engine.say(speech)
    engine.runAndWait()

def process(command: str, name: str, username: str):
    if "open website" in command:
        print("open website is there")
        website = command.replace(f"{name} open website", "").replace(" ","")
        print(website)
        try:
            if website == "github":
                webbrowser.open("https://github.com")
            elif website == "githubmyaccount":
                webbrowser.open("https://github.com/AviralCoder")
            elif website == "classroom":
                webbrowser.open("https://classroom.google.com")
            elif website == "youtube":
                webbrowser.open("https://youtube.com")
            elif website == "gmail":
                webbrowser.open("https://mail.google.com")
            else:
                if "https://" in command:
                    webbrowser.open(website)
                else: 
                    webbrowser.open(f'https://{website}')
            speak(f"{website} opened!")
        except:
            raise Exception("An error occured")
            
    elif "calculate" in command:
        expression = command.replace(f"{name} calculate", " ").replace(" ", "")
        try:
            answer = eval(expression)
            speak(f"Your answer is {answer}")
        except SyntaxError:
            speak("Looks like this isn't an expression.")
            time.sleep(0.1)
            speak(f'{username}, look if each character in your expression is a digit or a symbol or something mathematical.')

    elif "open app" in command:
        app = command.replace(f"{name} open app", "").replace(" ","")
        if ".app" not in app:
            os.system(f'open {app_paths.get(app)}')
        else:
            os.system(f'open /Applications/{app}')
        
        speak(f"{app} opened!")
    
    elif "how are you" in command:
        
    
    else:
        for phrase in feedback_phrases:
            if phrase in command:
                for adjective in positive_words:
                    if (adjective in command):
                        speak("Thanks!")
                        break
                    else: 
                        continue
                for adjective in negative_words:
                    if adjective in command:
                        speak("I am trying to do better!")
                        break
                    else:
                        continue



def main(ai_name: str):
    # credentials
    AI_NAME = ai_name
    USERNAME = details.get("username")

    if DEBUGGING: 
         engine.say(f"{AI_NAME} started")

    # engine.say(f"Hello {USERNAME}")
    # engine.say(greet())

    engine.say(f'Hello {USERNAME}')
    time.sleep(1)
    engine.say(greet())
    engine.runAndWait()


    while True:
        command = input(">>> ")
        continuation = False,
        if command == "q":
            break
        else: 
            if command.split(' ', 1)[0] == AI_NAME.lower():
                process(command, AI_NAME.lower(), USERNAME)

if __name__ == "__main__":
    main(details.get("ai_name"))