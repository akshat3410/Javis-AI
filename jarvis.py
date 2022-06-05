import datetime
from email.mime import audio
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning sir")
    
    elif hour>= 12 and hour<18:
        speak("Good Afternoon sir!")
    
    else:
        speak("Good Evening sir!")

    speak("I am Friday, How can i help you ")

def takeCommand():
    """It take microphone input from the user"""
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listning...")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"

if __name__ == '__main__':
    wishMe()