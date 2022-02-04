# IF ANY CODE IS WRITTEN BADLY, PLEASE DON'T JUDGE ME,
#  I AM NOT FAMILIAR WITH PYTHON, THIS IS MY FIRST TIME, 
# I USUALLY ONLY CODE JAVASCRIPT (REACT JS, 
# HTML, CSS, SCSS, Node.js, Express, TypeScript, Stuff...)

from functions.loadData import loadData
from functions.wish import greet
import webbrowser
import os

# IMPORTANT VARIABLES
DEBUGGING = False

details: dict = loadData("./lib/credentials.json")

def process(command: str):
    if "open website" in command:
        website = command.replace("open website", "").replace(" ","")
        try:
            if website == "github":
                webbrowser.open("https://github.com")
            elif website == "github=myaccount":
                webbrowser.open("https://github.com/AviralCoder")
            elif website == "classroom":
                webbrowser.open("https://classroom.google.com")
            else:
                if "https://" in command:
                    webbrowser.open(website)
                else: 
                    webbrowser.open(f'https://{website}')
            print("Website should have successfully opened on your default web browser!")
        except:
            raise Exception("An error occured")
    if "calculate" in command:
        expression = command.replace("calculate", " ").replace(" ", "")
        print(f"Your answer is {eval(expression)}")

    if "open app" in command:
        app = command.replace("open website", "").replace(" ","")

        

def main(ai_name: str):
    # credentials
    AI_NAME = ai_name
    USERNAME = details.get("username")

    if DEBUGGING: 
         print(f"{AI_NAME} started")

    print(f"Hello {USERNAME}")
    print(greet())

    while True:
        command = input(">>> ")
        continuation = False,
        if command == "q":
            break
        else: 
            process(command)

if __name__ == "__main__":
    main(details.get("ai_name"))