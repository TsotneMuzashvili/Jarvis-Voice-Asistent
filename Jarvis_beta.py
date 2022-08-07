import ipaddress
from logging import exception
from unittest import result
import speech_recognition as sr
import pyttsx3
import datetime
from datetime import date
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import subprocess
import pywhatkit
import requests
import pyjokes
from win10toast import ToastNotifier
import random
from functools import cache 
from bs4 import BeautifulSoup
import pyautogui
import pywikihow
from urllib.request import urlopen














toast = ToastNotifier()
toast.show_toast("Jarvis","Jarvis is stating", duration = 10)

os.chdir("C:\Tsotne\Python\Jarvis")



today = date.today()



engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(text):
    engine.say(text)
    engine.runAndWait()  

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    d2 = today.strftime("%B %d, %Y")
    speak(d2)

def wishme():
    speak("ჯარვისი ჩაიტვირთა")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning sir!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good Evening sir!")
    else:
        speak("Good Night sir!")

def end():
    speak("წარმატებულ დღეს გისურვებთ")




def takeCommandgeo():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("გისმენ...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='georgian')
            print(f"მომხმარებელმა თქვა:{statement}\n")

        except Exception as e:
            # speak("ვერ გავიგე, გთხოვ გაიმეორო")
            return "none"
        return statement

if __name__=='__main__':

    wishme()
    speak('მიხარია შენი დანახვა')

    while True:
        speak("რით შემიძლია დაგეხმარო??")
        statement = takeCommandgeo().lower()

        if statement==0:
            continue

        if "თავისუფალი ხარ ჯარვის" in statement:
            end()
            break

        elif "როგორ ხარ ჯარვის" in statement:
            speak("კარგად შენ როგორ ხარ?")