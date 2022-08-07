import speech_recognition as sr
import pyttsx3
import os
import ecapture as ec
from win10toast import ToastNotifier






engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()  


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            # speak("i didnt hear you, please say that again")
            return "none"
        return statement

speak('Jarvis Start Up is now open')

if __name__=='__main__':

    while True:
        # speak("what can i do for you?")
        statement = takeCommand().lower()

        if statement==0:
            continue

        if "goodbye jarvis" in statement or "bye jarvis" in statement or "stop jarvis" in statement or "turn off jarvis" in statement:
            speak ('see you later!')
            break
        
        if "wake up jarvis" in statement or "open jarvis" in statement or "activate jarvis" in statement:
            speak('opening jarvis')
            os.system('cmd /c "python Jarvis.py"')
            



    