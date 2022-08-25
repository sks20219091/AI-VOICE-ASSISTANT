import urllib.request
import requests
import os
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr


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
        print(f": User : {query}\n")
    except:
        return ""
    return query.lower()

def downloadImage(n):
	speak("What image do you want to download")
	query = Mic()
	URL = "https://www.google.com/search?tbm=isch&q=" + query
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')
	imgTags = soup.find_all('img', class_='yWs4tf') # old class name -> t0fcAb (Update this)

	if os.path.exists('Downloads')==False:
		os.mkdir('Downloads')

	count=0
	for i in imgTags:
		if count==n: break
		try:
			urllib.request.urlretrieve(i['src'], 'Downloads/' + str(count) + '.jpg')
			count+=1
			print('Downloaded', count)
			speak('images has downloaded, please check your download folder')
		except:
			speak('can not download the image')
	



