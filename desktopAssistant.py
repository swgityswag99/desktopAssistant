from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from Websearch import Web
from User import User
import time
import Assistant

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        
        print('You said: ' + command + '\n')
        

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand()
    return command

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
        Assistant.scroll_to_bottom_webpage(user)

    elif "sleep" in command or 'hibernation mode' in command:
        talkToMe('I will be here when you need me')

    elif 'friday' in command:
        talkToMe("ready")
        
    elif 'open' in command:
        c = command.split("open")
        link = c[1]
        Assistant.select_link(user,link)

    elif 'go back' in command:
        Assistant.go_back(user)
        
user = User()
talkToMe('Awaiting your Command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand(),user)
