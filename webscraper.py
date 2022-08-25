import wolframalpha
import pyttsx3
import speech_recognition as sr

try:
    client = wolframalpha.Client("")

except:
    speak("Answer not found")





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

def AskAnything():
    speak('what is your question')
    Problem = Mic()
    Problem = Problem.replace("calculate", "")
    client = wolframalpha.Client("")
    res = client.query(Problem)
    answer = next(res.results).text
    speak(answer)
    

