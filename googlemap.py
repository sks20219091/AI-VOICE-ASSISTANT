import pyttsx3
import geocoder
import requests
from geopy import location
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import geopy
import webbrowser as wb

ai = pyttsx3.init()
voices = ai.getProperty('voices')
ai.setProperty('voice', voices[0].id)
ai.setProperty('rate',170)

def speak(audio):   
    print(" ")
    print(f"Adam:{audio}")
    print(" ")  
    ai.say(audio)
    ai.runAndWait()

def GoogleMaps(Place):
    Url_Place = "https://www.google.com/maps/place/" + str(Place)
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(Place , addressdetails= True)
    target_latlon = location.latitude , location.longitude
    wb.open(url=Url_Place)
    location = location.raw['address']
    target = {'city' : location.get('city',''),
                'state' : location.get('state',''),
                'country' : location.get('country','')}
    current_loca = geocoder.ip('me')
    current_latlon = current_loca.latlng
    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)
    speak(f"{target} .{Place} Is {distance} Kilometre Away From Your Place .")
    

