import requests
from bs4 import BeautifulSoup
import urllib.request
from say import speak

def temperature(query):
    search = query
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"htal.parser") 
    temp = data.find("div",class_="BNeawe").text
    speak(f"current {search} is {temp}")         
            