import pyttsx3
import pyautogui
import pyjokes
import psutil
import PyPDF2
import pywhatkit
import datetime as dt
import calendar as cal
import time as tt
import smtplib
import ctypes
import clipboard
import requests 
import randfacts     
import wikipedia
import webbrowser as wb
import wolframalpha
import winshell
import subprocess
import json
import urllib.request
import speech_recognition as sr
import playsound
import os
import string as str
import random
import nltk
from nltk.tokenize import word_tokenize
from random import randrange
from bs4 import BeautifulSoup
from gtts import gTTS
#from email.message import EmailMessage
from flask import Flask
from pywikihow import WikiHow , search_wikihow
from translate import Translator
from newsapi import NewsApiClient
from privacy import *
from transal import *
from whatsapp import *
from timer import *
from ToDo import *
from googlemap import *
from test import *
from wiki import information
from webscraper import *

ai = pyttsx3.init('sapi5')
voices = ai.getProperty('voices')
ai.setProperty('voice', voices[0].id)
ai.setProperty('rate',170)

def speak(audio):   
    print(" ")
    print(f"Adam:{audio}")
    print(" ")  
    ai.say(audio)
    ai.runAndWait()

def response(text):
    print(text)
    tts = gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)

def getvoices(voice):
    voices = ai.getProperty('voices')
    if voice == 1:
        ai.setProperty('voice', voices[1].id)
    if voice == 2:
        ai.setProperty('voice', voices[2].id) 
    #Speak("Hello this is Sandra")

def Current_Time():
    time = dt.datetime.now().strftime("%I:%M:%S")        
    speak("The Currrent Time is :")
    speak(time)

def date():
    now = dt.datetime.now()
    date_now = dt.datetime.today()
    week_now = cal.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day
    month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31",
    ]
    print(f'Today is {week_now}, {month[month_now - 1]} the {ordinals[day_now - 1]}.')
    speak(f'Todat is {week_now}, {month[month_now - 1]} the {ordinals[day_now - 1]}.')

def how():
    response = ["Hey, I'm Good !",
		"I'm good",
		"I'm good, what about you?",
		"I'm fine, hope you're also fine",
		"Good, how about you?",
		"Doing fine, and you?",
		"I'm doing great",
		"I'm doing Well" ]
    m = random.choice(response) + ", sir"
    speak(m)

def who():
    response = ["I'm your Personal Assistant",
		"You know me right! If not then I'm your Personal Assistant",
		"You developed me, so you must know who I am",
		"Did I forget to introduce myself? I'm your Personal Assistant" ]
    m = random.choice(response) + ", sir"
    speak(m)

def smart():
    response = ["Yes, I'm smart",
		"Ofcourse I'm smart",
		"I'm a program, so I'm smart"]
    m = random.choice(response) + ", sir"
    speak(m)

def fine():
    response = ["Hope you're fine",
		"Good to know that you are fine",
		"Good to know" ]
    m = random.choice(response) + ", sir"
    speak(m)

def name():
    response = ["You can call me adam",
		"Name doesn't matter",
		"I'm your Personal AI Voice Assistant" ]
    m = random.choice(response) + ", sir"
    speak(m)

def wish():
    hour = dt.datetime.now().hour
    if hour >= 5 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour < 22:
        speak("Good Evening Sir!")
    else :
        print("Why are not asleep")

def greeting():
    speak("Welcome, Iam AI voice assistant Adam")
    Current_Time()
    date()
    wish()
    speak("How may i Assist you?")
    

def Music():
    speak("What song do you like to hear!")
    musicName = Mic()
    if 'iadhd' in musicName:
        os.startfile('')
    elif 'jdjdk' in musicName:
        os.startfile('')
    else:
        pywhatkit.playonyt(musicName)
        speak("Enjoy the song, Sir!")

def GoogleSearch():
    speak("what do you want to search in google")
    term = Mic()
    term = term.replace("about", "")
    Query = (term)
    pywhatkit.search(Query)
    try:
        if 'how to' in Query:
            max_result = 1
            how_to_func = search_wikihow(query=Query,max_results=max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            print(how_to_func[0].summary)
        else:
            search = wikipedia.summary(Query,2)
            speak(f": According To Your Search : {search}")
    except:
        speak("I Can not define them")

def SimpleGoogleSearch():
    speak("what do wnat to search")
    Title = Mic()
    Title = Title.replace("about", "")
    pywhatkit.search(Title)

def yahoo():
    speak("What do you want to search in yahoo, Sir")
    search = Mic()
    search = search.replace("about", "")
    wb.open('https://in.search.yahoo.com/yhs/search?p='+search)

def youtube():
    speak("What do you want to watch in youtube, Sir")
    topic = Mic()
    topic = topic.replace("about", "")
    result = "https://www.youtube.com/results?search_query=" + topic
    wb.open(result)
    speak("This is the latest video Sir")
    pywhatkit.playonyt(topic)

def weather():
    speak("What city weather are you looking for")
    city = Mic()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&unit=imperial&appid='
    try:
        res = requests.get(url)
        data = res.json()
        weather = data['weather'] [0] ['main']
        temp = data['main']['temp']
        desp = data['weather'] [0] ['description']
        temperature = round(temp - 273.15)
        print(weather)
        print(temperature)
        print(desp)
        speak(f'The weather in {city} is like ')
        speak('Temperature : {} degree celcius'.format(temperature))
        speak('Weather is  {} '.format(desp))
    except:
        speak("check your connection")

def news(n=2):
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=')

    try:
        response = requests.get(url)
    except:
        speak("check your connection")
    news = json.loads(response.text)
    count = 0
    for new in news["articles"]:
        count+=1
        if count>n:
            break
        else:
            print(new["title"],"\n")
            speak(new["title"])
            print(new["description"],"\n")
            speak(new["description"])  

def read_text():
    text = clipboard.paste()
    print(text)
    speak(text)

def Reader():
        speak("Tell Me The Name Of The Book!")
        name = Mic()
        if 'stories' in name:
            os.startfile("C:\\Users\\RITVIK JOHNSON\\OneDrive\\Desktop\\python_work\\AI\\extrafiles\\stories.pdf")
            book = open("C:\\Users\\RITVIK JOHNSON\\OneDrive\\Desktop\\python_work\\AI\\extrafiles\\stories.pdf",'rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            speak(f"Number Of Pages In This Books Are {pages}")
            speak("From Which Page I Have To Start Reading ?")
            numPage = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            speak(text)
        else:
            speak("Book not found")

def covid():
	r = requests.get('https://coronavirus-19-api.herokuapp.com/all')
	data = r.json()
	covid_data = (f'Confirm cases : {(data["cases"])} \n Deaths : {data["deaths"]} \n Recovered {data["recovered"]}')
	speak(covid_data)
       
def symptoms():
    speak('Do you want to know the symtoms')
    res = Mic()
    if 'yes' in res:
        speak("Some common symptomsare")
        symt = ['1. Fever',
            '2. Coughing',
            '3. Shortness of breath',
            '4. Trouble breathing',
            '5. Fatigue',
            '6. Chills, sometimes with shaking',
            '7. Body aches',
            '8. Headache',
            '9. Sore throat',
            '10. Loss of smell or taste',
            '11. Nausea',
            '12. Diarrhea']
        print(symt)
        speak(symt)
    else:
        speak("No problem sir")

def screenshot():
    speak("Taking screen shot")
    name_img = tt.time()
    name_img = f'C:\\Users\\RITVIK JOHNSON\\OneDrive\\Desktop\\python_work\\AI\\Screenshot\\{name_img}.png'
    playsound.playsound("C:\\Users\\RITVIK JOHNSON\\OneDrive\\Desktop\\python_work\\AI\\extrafiles\\audios\\photoclick.mp3")
    img = pyautogui.screenshot(name_img)
    img.show()

def remember():
    speak("what should i remember, sir?")
    data = Mic()
    speak("You asked me to remember that" +data)
    remember = open('data.txt','w')
    remember.write(data)
    remember.close()

def remind_me():
    reminder = open('data.txt','r')
    speak("You asked me to remind you that, " +reminder.read())

def password():
    s1 = str.ascii_lowercase
    s2 = str.ascii_uppercase
    s3 = str.digits
    s4 = str.punctuation

    passlen = 10
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip():
    speak("Ok sir, Flipping coin")
    playsound.playsound("C:\\Users\\RITVIK JOHNSON\\OneDrive\\Desktop\\python_work\\AI\\extrafiles\\audios\\coin.mp3")
    coin = ['Heads','Tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    print(toss)
    speak("I flipped the coin and got :" +toss)

def roll_dice():
    speak("Okay sir, Rolling a dice for you")
    playsound.playsound("C:\\Users\\RITVIK JOHNSON\\OneDrive\\Desktop\\python_work\\AI\\extrafiles\\audios\\dice.mp3")
    dice = ['1','2','3','4','5','6']
    roll = []
    roll.extend(dice)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    speak("I rolled a die and you got " + roll)

def jokes():
	URL = 'https://icanhazdadjoke.com/'
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')

	try:
		p = soup.find('p')
		return p.text
	except Exception as e:
		raise e

def cpu():
    usage = (psutil.cpu_percent())
    speak(f"CPU usage is at {usage} percentage")
    battery = psutil.sensors_battery()
    speak(f"Battery is at {battery.percent} percentage")

def operating_system(a):
    if a == 1:
        codepath = 'C:\\Users\\RITVIK JOHNSON\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(codepath)
    elif a == 2:
        codepath = 'C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe'
        os.startfile(codepath)
    elif a == 3:
        codepath = ''
        os.startfile(codepath)
    elif a == 4:
        codepath = ''
        os.startfile(codepath)
    elif a == 5:
        codepath = ''
        os.startfile(codepath)
    else:
        speak("File not found")

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

def main():
    #greeting()
    while True:
        wake_word = "rohit"
        query = Mic().lower()
        query = word_tokenize(query)
        if wake_word in query:
            #query = Mic().lower()
            if 'time' in query:
                Current_Time()
                break
            elif 'hello' in query:
                hello()
                break
            elif 'how' in query and 'are'in query and 'you' in query:
                how()
                speak("What About YOU?")
                break
            elif 'fine' in query or 'good' in query:
                fine()
                break
            elif 'smart' in query or 'intelligent' in query:
                smart()
                break
            elif 'who' in query and 'are' in query and 'you' in query:
                who()
                break
            elif 'what' in query and 'is' in query and 'your' in query and 'name' in query:
                name()
                break
            elif 'you' in query and 'need' in query and 'a' in query and 'break' in query:
                speak("Ok Sir")
                speak("we'll see each other in 10 seconds")
                startTimer('10 seconds')
                break
            elif 'date' in query:
                date()
                break
            elif 'wish' in query:
                wish()   
                break
            elif 'email' in query:
                email_list = {'mother':'',
                                'rupesh':'kumarrupesh231020@gmail.com',
                                'david':'davidpeter123@gmail.com'
                }
                try:
                    speak('To whom you want to send the mail')
                    name = Mic().lower()
                    receiver = email_list[name]
                    speak("What is the subject of mail")
                    subject = Mic()
                    speak("What should i say")
                    content = Mic()
                    mail(receiver,subject,content)
                    speak("Your mail has been sent")
                except Exception as e:
                    print(e)
                    speak("Was not able to send the mail")
                break
            elif 'whatsapp' in query:
                WhatsappMsg()
                break
            elif 'wikipedia' in query:
                try:
                    speak("what do you want to search in Wikipedia")
                    a = Mic()
                    a = a.replace("about", "")
                    speak("Searching in Wikipedia...")
                    AD = information()
                    AD.get_info(a)
                    result = wikipedia.summary(a, sentences = 2)
                    speak(result)
                except Exception as e:
                    print(e)
                    speak("can not define")
                break
            elif 'google' in query:
                GoogleSearch()
                break
            elif 'simple' in query:
                SimpleGoogleSearch()
                break
            elif 'map' in query or 'Map' in query:
                speak("What place are you looking for")
                Place = Mic()
                GoogleMaps(Place)
                break
            elif 'translate' in query:
                trans()
                break
            elif 'image' in query or 'images' in query:
                downloadImage(4)
                break
            elif 'yahoo' in query:
                yahoo()
                break
            elif 'youtube' in query:
                youtube()
                break
            elif 'weather' in query:
                weather()
                break
            elif 'news' in query:
                news()
                break
            elif 'read' in query:
                read_text()
                break
            elif 'book' in query:
                Reader()
                break
            elif 'covid' in query:
                covid()
                symptoms()
                break
            elif 'list' in query:
                speak("What do want to do")
                ToDo = Mic()
                toDoList(ToDo)
                break
            elif 'question' in query or 'answer' in query:
                try:
                    AskAnything()
                except:
                    speak("Answer not found")
                speak("Do you have anyother question")
                ai.runAndWait()
                next = Mic()
                if 'yes' in next:
                    AskAnything()
                elif 'no' in next:
                    speak("no problem sir")
                else:
                    speak("Time limit exceeded ")
                break
            elif 'joke' in query:
                #speak(pyjokes.get_joke())
                jok = jokes()
                speak(jok)
                playsound.playsound("C:\\Users\\RITVIK JOHNSON\\OneDrive\\Desktop\\python_work\\AI\\extrafiles\\audios\\mixkit-human-male-casual-laugh-411.wav")
                break
            elif 'fact' in query:
                x = randfacts.getFact()
                speak("Did you know that" +x)
                break
            elif 'logout' in query:
                speak("locking the device ,sir")
                ctypes.windll.user32.LockWorkStation()
                quit()
            elif "restart" in query:
                speak("Hold On a Sec ! Your system is on its way to restart")
                subprocess.call(["shutdown", "/r"])
                quit()
            elif 'shutdown' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                quit()
            elif 'screenshot' in query:
                screenshot()
                break
            elif 'remind' in query and 'me' in query:
                remind_me()
                break
            elif 'remember' in query:
                remember()
                break
            elif 'password' in query:
                password()
                break
            elif 'flip' in query:
                flip()
                break
            elif 'roll' in query or 'dice' in query:
                roll_dice()
                break
            elif 'start' in query or 'set' in query or 'timer' in query:
                speak("what is the coundown")
                time = Mic()
                startTimer(time)
                break
            elif 'status' in query or 'performance' in query:
                cpu()
                break
            elif 'repeat' in query:
                speak("Speak Sir!")
                jj = Mic()
                speak(f"You Said : {jj}")
                break
            elif 'music' in query:
                Music()
                break
            elif 'launch' in query or 'website' in query:
                speak("Tell Me The Name Of The Website!")
                name = Mic()
                web = 'https://www.' + name + '.com'
                wb.open(web)
                speak("Done Sir!")
                break
            elif 'open' in query or 'file' in query:
                speak("What file should i open")
                filename = Mic()
                if 'visual code' in filename:
                    operating_system(1)
                elif 'virtualbox' in filename:
                    operating_system(2)
                break
            elif 'offline' in query or 'sleep' in query or 'bye' in query or 'off' in query:
                speak("Ok bye see you later")
                quit()
        
if __name__ ==  "__main__" :
    main()
        

    

