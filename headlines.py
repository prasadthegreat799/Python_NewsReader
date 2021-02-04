import requests
import pyttsx3
from bs4 import BeautifulSoup
import json

engine = pyttsx3.init()
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
engine.setProperty('rate', 120)    
engine.setProperty('volume', 0.9) 



def print_headlines(response_text):
    soup = BeautifulSoup(response_text, 'lxml')
    headlines = soup.find_all(attrs={"itemprop": "headline"})
    for headline in headlines:
        data=headline.text
        print(headline.text,"\n")
        engine.say(data)
        engine.runAndWait()


url = 'http://www.inshorts.com/en/read/technology'
response = requests.get(url)
print_headlines(response.text)
