import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import os
import pyjokes
import random
import time
from playsound import playsound
import datetime
import time
import cv2
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am MATION Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'discord' in query:
            print('opening discord for YOU')
            speak('opening discord for YOU')
            codepath= 'C:\\Users\\ADMIN\\Desktop\\ramya shah\\Discord.lnk'
            os.startfile(codepath)
        if "joke" in query:
            cjoke=pyjokes.get_joke()
            print(cjoke)
            speak(cjoke)
        if "time" in query:
            aclock=time.ctime()
            print(aclock)
            speak(aclock)
        if "camera" in query:
            cam = cv2.VideoCapture(0)
            while cam.isOpened():
                ret, frame = cam.read() 
                if cv2.waitKey(10) == ord('q'):
                    break
                cv2.imshow('ramya shah', frame)
        if "music" in query:
            speak('NOW PLAYING dheeme dheeme FOR you')
            playsound('C:\\Users\\ADMIN\\Desktop\\python\\chapter 1\\Dheeme Dheeme.mp3')
        if "google" in query:
            speak("opening google for u")
            webbrowser.open('https://www.google.com/')    
        elif "youtube" in query:
            speak("OPENING YOTUBE FOR YOU")
            webbrowser.open("https://www.youtube.com/")
        elif "github" in query:
            speak('github is OP opening it--> ')
            print('-->')
            webbrowser.open("https://www.github.com")
