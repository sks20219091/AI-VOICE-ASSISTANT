from googletrans import Translator
import pyttsx3
import speech_recognition as sr

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

def trans():
    des = {
        'french':'fr'
    }
    try:
        speak("what text do you want to translate")
        query = Mic()
        speak("what language")
        name = Mic().lower()
        trans = Translator()
        out=trans.translate(query, dest=des[name], src='en' )
        speak(out.text)

    except:
        speak("Unable to translate")


