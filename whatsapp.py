import pyautogui 
from time import sleep
import pyttsx3
import speech_recognition as sr
import webbrowser as wb

ai = pyttsx3.init()
voices = ai.getProperty('voices')
ai.setProperty('voice', voices[0].id)
ai.setProperty('rate',170)

def speak(audio):
    print(" ")
    print(f"Adam: {audio}")
    ai.say(audio)
    ai.runAndWait()
    print(" ")

def Mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(": Recognizing...")
        query = r.recognize_google(audio,language='en')
        print(f"User : {query}\n")
    except:
        return ""
    return query.lower()

def WhatsappMsg():
        user_name = {
            'mother':'',
            'brother':'',
            'rupesh':''
        }
        try:
            speak('To whom you want to send the whatsapp message')
            name = Mic().lower()
            phone_no = user_name[name]
            speak("What is the message")
            message = Mic()
            msg(phone_no,message)
            speak("Your message has been sent")
        except Exception as e:
            print(e)
            speak("Was not able to send the message")

def msg(phone_no,message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(15)
    pyautogui.press('enter')






   