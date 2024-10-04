import pyttsx3      #audio for assistant/voice
import textwrap
import google.generativeai as genai
import datetime     
import speech_recognition as sr
import wikipedia    #searching
import webbrowser #for opening apps
import config
import subprocess
import ctypes
import pyjokes
import os       #playing songs
import random
from ecapture import ecapture as ec
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


name='champ'
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<16):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
   
    speak(f'I am {name}, your assistant , How can I help you')
def takeCommand():
    s=sr.Recognizer()
    s.energy_threshold=1000
    with sr.Microphone() as source:
        print("Listening ....")
        s.pause_threshold=1
        audio=s.listen(source,timeout=5)
    try:
        print("Recognizing .... ")
        query=s.recognize_google(audio,language='en-in')
        print(f"you said: {query}\n")
    except Exception as e:
        print("say again please ....")
        return None 
    return query

def to_markdown(text):
    text = text.replace('•', '  *')
    indented_text = textwrap.indent(text, ' ',predicate=lambda _: True)
    return indented_text
def text_response(prompt):
  res=model.generate_content(prompt)
  return to_markdown(res.text)

if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open whatsapp" in query:
            webbrowser.open("whatsapp.com")
        elif "open snapchat" in query:
            webbrowser.open("snapchat.com")
        elif "open instagram" in query:
            webbrowser.open("instagram.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%m-%d-%Y %H:%I%p")   
            speak(f"Mam, the time is {strTime}")
        elif 'how are you' in query:
            speak("I am fine, How are you?")
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by VARS.")
 
        elif 'fine' in query or "i am good" in query:
            speak("It's good to know that your fine")
 
        elif "change name" in query:
            speak("What would you like to call me,Mam")
            name = takeCommand()
            speak(f"Thanks for naming me, I love the name {name}")
 
        elif "what's your name" in query or "what is your name" in query:
            speak(f"My friends call me {name}")
           
 
        elif 'exit' in query or 'stop' in query or 'get lost' in query:
            speak("I'll miss you take care, bye bye")
            exit()

        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
            
        elif 'i hate you' in query:
            speak("sorry to hear that, but i love you")

        elif 'i love you' in query:
            speak("happy to hear that, i love you too , but as a friend")

        elif 'friend' in query:
            speak("i'd love to be your friend")

        elif 'will you be my' in query:
            speak("sorry , i am just a virtual assistant")

        elif "who are you" in query:
            speak("I am your virtual assistant created by VARS")

        elif 'shutdown' in query:
                speak("Please hold On! Your system is going to shut down")
                subprocess.call(["shutdown", "/s"])

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
      
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "champ Camera ", "img.jpg")

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'tell me about you' in query:
            speak("Hey! I am a virtual assistant and your virtual friend , i'm here to help you out when you have no one")

        elif 'play music' in query or "play song" in query:
            speak("Playing songs...")
            music = "C:\\Users\\renud\\Music"
            songs = os.listdir(music)
            play = os.startfile(os.path.join(music, songs[random.randint(0,len(songs)-1)]))

        else:
            genai.configure(api_key=config.API)
            model = genai.GenerativeModel('gemini-pro')
            
            data=text_response(query)
            with open('response.txt','w') as file:
                file.writelines(data)
            
            print(data)
            speak(data)
           
           
        