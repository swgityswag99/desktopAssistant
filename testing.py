import selenium.webdriver as webdriver
import Assistant
from User import User
import requests
from bs4 import BeautifulSoup
import os
# import os

# def list_currrent_directory():
#     print(os.listdir(os.curdir))


# os.chdir("/Users/Swgityswag/Desktop")
# print(os.listdir(os.curdir))
def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

def assistant(command,user):
    "if statements for executing commands"
            
    if 'open chrome' in command or 'open browser' in command:
        talkToMe("command accepted")
        Assistant.open_browser(user)

    elif 'open blackboard' in command:
        talkToMe("command accepted")
        Assistant.open_blackboard(user)

    elif 'search again' in  command and 'for' in command :
        talkToMe("command accepted")
        Assistant.search_again(user,command)

    elif 'search' in  command and 'for' in command:
        talkToMe("command accepted")
        Assistant.search_web(user,command)

    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')

    elif 'scroll down' in command or 'keep scrolling' in command:
        talkToMe("command accepted")
        Assistant.scroll_down_webpage(user)
    
    elif 'scroll to bottom' in command:
        talkToMe("command accepted")
        Assistant.scroll_to_bottom_webpage(user)

    elif 'scroll to top' in command:
        talkToMe("command accepted")
        Assistant.scroll_to_top_webpage(user)

    elif "sleep" in command or 'hibernation mode' in command:
        talkToMe('I will be here when you need me')

    elif 'friday' in command:
        talkToMe("ready")
        
    elif 'open' in command:
        c = command.split("open")
        link = c[1]
        Assistant.select_link(user,link)
user = User()

while True:
    command = input("Awaiting command\n")
    assistant(command,user)