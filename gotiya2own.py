import speech_recognition as s 
import os
import pyjokes
import random
import datetime
from playsound import playsound
import time
import pyttsx3
import cv2
import webbrowser

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)
def speak(audio):

    engine.say(audio) 
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am gotiya the OP bot how may i help U")
if __name__ == "__main__":
    wishme()
    while True:
        sr=s.Recognizer()
        print("I AM LISTING,HOW MAY I HELP U please TELL")
        with s.Microphone() as m:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            print(query)

        # if "browser" or "browser" in query:
        #     webbrowser.open('https://www.google.com/')
        # elif "YouTube" in query:
        #     webbrowser.open('https://www.youtube.com')
        # else:
        #     speak("cant reach it")
        #     print('cant reach it')
        if 'Discord' in query:
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
        if query==('Google'):
            speak("opening google for u")
            webbrowser.open('https://www.google.com/')
        # if "Remind" or "remind" in query:
        #     speak('what u want to remind me please tell')
        #     s.Microphone(query)
        #     print(query)
        #     with open('remind.txt',"w") as f:
        #         f.write('queryremind')
        #     with open('remind.txt') as re:   
        #         reminder=re.read()
        # if "what did i tell you" in query:
        #     speak(reminder)
