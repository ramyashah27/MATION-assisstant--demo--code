import speech_recognition as s 
import os
import pyjokes
import random
import datetime
from playsound import playsound
import time
import webbrowser
import pyttsx3
import cv2

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
sr=s.Recognizer()
print("HOW MAY I HELP U please TELL")




with s.Microphone() as m:
    audio=sr.listen(m)
    query=sr.recognize_google(audio,language='eng-in')
    print(query)

if 'Discord' in query:
    print('opening discord for YOU')
    codepath= 'C:\\Users\\ADMIN\\Desktop\\ramya shah\\Discord.lnk'
    os.startfile(codepath)
if "joke" in query:
    print(pyjokes.get_joke())
    speak(pyjokes.get_joke())
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
    speak('NOW PLAYING dheeme dheeme for kiara topa')
    playsound('C:\\Users\\ADMIN\\Desktop\\python\\chapter 1\\Dheeme Dheeme.mp3')
# elif "google" or "Google" in query:
#     webbrowser.open('https://www.google.com/')
elif "youtube" or "Youtube" or "YouTube" in query:
    webbrowser.open('https://www.youtube.com/')
elif "snake water gun" or  "Snake water gun" in query:
    def game(comp,you):
        if comp==you:
            return None 
        elif comp == 's':
            if you=='w':
                return False
            elif you=='g':
                return True
        elif comp == 'w':
            if you=='g':
                return False
            elif you=='s':
                return True
        elif comp == 'g':
            if you=='s':
                return False
            elif you=='w':
                return True
    print("computer Turn: Snake(s) Water(w) or Gun(g)?")
    randno= random.randint(1,3) 
    if randno == 1:
        comp = 's'
    elif randno == 2:
        comp = 'w'
    elif randno == 3:
        comp = 'g'

    you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
    print(f'you chose {you}')
    print(f'computer chose {comp}')
    a=game(comp,you)
    if a== None:
        print('THE GAME IS TIE')
    elif a:
        print('YOU WIN')
    else:
        print('YOU LOSE ')