# Code for virtual assistant with GUI
import speech_recognition as sr
import pyttsx3
import time
import webbrowser
import playsound
import os
import random
import tkinter
from tkinter import *
from PIL import ImageTk,Image
from AI import main

ai = pyttsx3.init("sapi5")
voices = ai.getProperty('voices')
ai.setProperty('voice', voices[0].id)
ai.setProperty('rate',170)


def speak(audio):   
    print(" ")
    print(f"Adam:{audio}")
    print(" ")  
    ai.say(audio)
    ai.runAndWait()

def Mic():
    m = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        m.energy_threshold = 1000
        m.adjust_for_ambient_noise(source,1.2)
        m.pause_threshold = 1
        audio = m.listen(source)
    try:
        print("Recognizing...")
        query = m.recognize_google(audio, language = "en")
        print(f"User: {query}")
    except Exception as e:
        print(e)
        speak("Sorry, Can You repeat it again")
        return "None"
    return query

class Widget:
    def __init__(self):
        root = Tk()
        root.title('AI Voice Assistant')
        root.geometry('720x480')
        img = ImageTk.PhotoImage(Image.open('Mic.png'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')
        compText = StringVar()
        userText = StringVar()
        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(root, text='Adam', font=('Railways', 24,'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='black',fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Offline', font=('railways', 10,'bold'), bg='white', fg='black', command=root.destroy).pack(fill='x', expand='no')
        speak('Iam Your AI Voice Assistant Adam')
        speak('How can i help you Sir?')
        root.mainloop()
    def clicked(self):
        main()

if __name__== '__main__':
    widget = Widget()
    time.sleep(1)
    speak("ok bye sir")