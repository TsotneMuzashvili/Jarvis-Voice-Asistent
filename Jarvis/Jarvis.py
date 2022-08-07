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
from googletrans import Translator










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
    speak("Jarvis is now open")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning sir!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good Evening sir!")
    else:
        speak("Good Night sir!")

def morning():
    speak("Good Morning sit!")

def end():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("wish you Good Morning sir! see you later, if u need somthing i am here")
    elif hour >=12 and hour<18:
        speak("wish you Good Afternoon sir! see you later, if u need somthing i am here")
    elif hour >=18 and hour<24:
        speak("wish you Good Evening sir! see you later, if u need somthing i am here")
    else:
        speak("wish you Good Night sir! see you later, if u need somthing i am here")

def swearing():
    swearing = ['fuck', 'fuck you', 'shit', 'piss off', 'dick head', 'asshoile', 'son of a bitch', ' bastard', 'bitch', 'damn', 'cunt']
    value = random.choice(swearing)
    speak(value)

def news():
    main_url = 'https://newsapi.org/v2/everything?domains=wsj.com&apiKey=094ee193b1514c5cb2b3eeb5ee593595'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "secound", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "thenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def location():
    res = requests.get('https://ipinfo.io')
    data = res.json()

    city = data['city']
    country = data['country']

    speak(city)
    speak(country)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in-geo')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("i didnt hear you, please say that again")
            return "none"
        return statement


    







if __name__=='__main__':

    wishme()
    speak('i am happy to see you again')
    speak('how can i help you?')

    

    while True:
        statement = takeCommand().lower()

        if statement==0:
            continue

        if "you are free" in statement or "sleep" in statement:
            end()
            break

        elif "who is george" in statement:
            speak("george is dickhead")

        elif "introduce yourself Jarvis" in statement:
            speak("hello my name is jarvis, i am your voice assistent")

        elif 'open wikipedia' in statement:
            webbrowser.open_new_tab("https://www.wikipedia.org/")
            speak("wikipedia is now open")

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://youtube.com")
            speak("youtube is now open")
            
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("google is now open")

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.google.com/gmail")
            speak("Google Mail is open now")

        elif 'open facebook' in statement:
            webbrowser.open_new_tab("https://www.facebook.com")
            speak("Facebook is open now")

        elif 'shop mymarket' in statement or 'mymarket' in statement:
            webbrowser.open_new_tab("https://www.mymarket.ge")
            speak("good shoping in mymarket master")

        elif 'shop newegg' in statement or 'newegg' in statement or 'new egg' in statement:
            webbrowser.open_new_tab("https://www.newegg.com")
            speak("good shoping in newegg master")

        elif 'shop amazon' in statement or 'amazon' in statement:
            webbrowser.open_new_tab("https://www.amazon.com")
            speak("good shoping in amazon master")

        elif 'weather' in statement or 'temperature' in statement:
            search = "temperature in rustavi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif 'time' in statement:
            speak("time now is")
            time()

        elif 'date' in statement:
            speak("today is")
            date()

        elif "hello jarvis" in statement:
            speak("i am fine sir, how can i help you?")

        elif "what is my dog's name" in statement:
            speak("your dogs name is ginda")

        elif "how are you jarvis" in statement:
            speak("i am fine master, how are u")

        elif "i am fine" in statement or "I'm fine too" in statement:
            speak("i am happy for you, how can i help you?")

        elif "thank you jarvis" in statement:
            speak("you are welcome master")

        elif "swearing" in statement or "swear" in statement:
            speak("i am sorry master but here is swear u asked")
            swearing()
            speak("i am sorry")

        elif "open calculator" in statement:
            subprocess.call('calc.exe')
            speak("calculator is open now")

        elif "close calculator" in statement:
            speak("okey sit, closing calculator")
            os.system("taskkill /f /im calc.exe")

        elif "open notepad" in statement:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            speak("notepad is now open")

        elif "close notepad" in statement:
            speak("okey sit, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "play music" in statement:
            musicdir = "C:\Tsotne\music"
            songs = os.listdir(musicdir)
            rd = random.choice(songs)
            os.startfile(os.path.join(musicdir, rd))

        #elif "set alarm" in statement:
            #nn = int(datetime.datetime.now().hour)
            #if nn == 22:
                #music_dir = "C:\Tsotne\music"
                #songs = os.listdir(music_dir)
                #os.startfile(os.path.join(music_dir, songs[0]))
            
        elif "info" in statement or "information" in statement:
            info = wikipedia.summary(statement)
            speak(info)

        elif "play" in statement:
            play = pywhatkit.playonyt(statement)
            speak(statement)
            speak("is now playing")
            
        elif "joke" in statement:
            speak("okey master, i have good joke for you, get ready")
            joke = pyjokes.get_joke()
            speak(joke)

        elif "switch the window" in statement:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

        elif "news" in statement:
            speak("please wait sir, fetching the latest news")
            news()

        elif "search" in statement:
            import wikipedia as googleScrap
            statement = statement.replace("Jarvis", "")
            statement = statement.replace("search", "")
            speak("this is what i found on the web")
            pywhatkit.search(statement)

            try:
                result = googleScrap.summary(statement,3)
                speak(result)

            except:
                speak("no data available")

        elif "where am i" in statement or "where i am" in statement or "where we are" in statement:
            
            speak("i am not sure sir, but i think we are in")
            location()

        elif "open the 48 laws of power book" in statement or "open the laws of power book" in statement:
            webbrowser.open_new_tab("file:///C:/Users/snaka/Documents/The_48_Laws_of_Power.pdf")
            speak("the 48 laws of power book is now open")

        elif "my name is" in statement:
            speak("i am happy to meet you, my name is Jarvis")

        elif "my name" in statement:
            speak("your name is tsotne")

        elif "alarm" in statement or "open alarm" in statement:
            webbrowser.open_new_tab('https://kukuklok.com/')
            speak("clock is now open")
        
        elif "github" in statement:
            webbrowser.open_new_tab('https://github.com/TsotneMuzashvili')
            speak("github is now open")