import pyttsx3
import speech_recognition as sr
import datetime
import time
import os
import webbrowser
import requests
import pyjokes
import random
import subprocess
import wikipedia
import pywhatkit
from datetime import date
from notifypy import Notify
from playsound import playsound
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup










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
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("wish you Good Morning sir! see you later, if u need somthing i am here")
    elif hour >=12 and hour<18:
        speak("wish you Good Afternoon sir! see you later, if u need somthing i am here")
    elif hour >=18 and hour<24:
        speak("wish you Good Evening sir! see you later, if u need somthing i am here")
    else:
        speak("wish you Good Night sir! see you later, if u need somthing i am here")

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

    speak("Jarvis is now open")
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

        elif "time" in statement:
            time()

        elif "date" in statement:
            date()

        elif "news" in statement:
            speak("please wait sir, fetching the latest news")
            news()

        elif "joke" in statement:
            speak("okey master, i have good joke for you, get ready")
            joke = pyjokes.get_joke()
            speak(joke)

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

        elif "github" in statement:
            webbrowser.open_new_tab('https://github.com/TsotneMuzashvili')
            speak("github is now open")

        elif 'shop mymarket' in statement or 'mymarket' in statement:
            webbrowser.open_new_tab("https://www.mymarket.ge")
            speak("good shoping in mymarket master")

        elif 'shop newegg' in statement or 'newegg' in statement or 'new egg' in statement:
            webbrowser.open_new_tab("https://www.newegg.com")
            speak("good shoping in newegg master")

        elif 'shop amazon' in statement or 'amazon' in statement:
            webbrowser.open_new_tab("https://www.amazon.com")
            speak("good shoping in amazon master")

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

        elif "info" in statement or "information" in statement:
            info = wikipedia.summary(statement)
            speak(info)

        elif "play music" in statement:
            musicdir = "C:\Tsotne\music"
            songs = os.listdir(musicdir)
            rd = random.choice(songs)
            os.startfile(os.path.join(musicdir, rd))

        elif "play" in statement:
            play = pywhatkit.playonyt(statement)
            speak(statement)
            speak("is now playing")

        elif "where am i" in statement or "where i am" in statement or "where we are" in statement:
            
            speak("i am not sure sir, but i think we are in")
            location()

        elif "open the 48 laws of power book" in statement or "open the laws of power book" in statement:
            webbrowser.open_new_tab("file:///C:/Users/snaka/Documents/The_48_Laws_of_Power.pdf")
            speak("the 48 laws of power book is now open")

        elif "alarm" in statement:
            speak("Enter The Time Sir")
            time = input("Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = datetime.datetime.now().strftime("%I:%M:%S")

                if now == time:
                    speak("Time To wake Up Sir!")
                    playsound('wakeup.mp3')
                    speak("Alarm Closed!")

                elif now>time:
                    break
            
        elif 'weather' in statement or 'temperature' in statement:
            search = "temperature in rustavi"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif 'home screen' in statement:

            press_and_release('windows + m')

        elif 'minimize' in statement:

            press_and_release('windows + m')

        elif 'show start' in statement:

            press('windows')

        elif 'open setting' in statement:

            press_and_release('windows + i')

        elif 'open search' in statement:

            press_and_release('windows + s')

        elif 'screen shot' in statement:

            press_and_release('windows + SHIFT + s')

        elif 'restore windows' in  statement:

            press_and_release('Windows + Shift + M')

        elif 'new tab' in statement:

            press_and_release('ctrl + t')

        elif 'close tab' in statement:

            press_and_release('ctrl + w')

        elif 'new window' in statement:

            press_and_release('ctrl + n')

        elif 'history' in statement:

            press_and_release('ctrl + h')

        elif 'downloads' in statement:

            press_and_release('ctrl + j')

        elif 'bookmark' in statement:

            press_and_release('ctrl + d')

            press('enter')

        elif 'incognito' in statement:

            press_and_release('Ctrl + Shift + n')

        elif 'switch tab' in statement:

            tab = statement.replace("switch tab ", "")
            Tab = tab.replace("to","")
        
            num = Tab

            bb = f'ctrl + {num}'

            press_and_release(bb)

        elif 'open' in statement:

            name = statement.replace("open ","")

            NameA = str(name)

        else:

            string = "https://www." + NameA + ".com"

            string_2 = string.replace(" ","")

            webbrowser.open(string_2)