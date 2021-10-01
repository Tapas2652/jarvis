import speedtest #pip install speedtest
from bs4 import BeautifulSoup #pip install bs4
from pywikihow import search_wikihow #pip install pywikihow
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speech_recognition
import datetime #pip install datetime
import os
import cv2 #pip install opencv-python
import random #pip install random
from requests import get
import webbrowser #pip install webbrowser
import sys
import urllib #pip install urllib
import time #pip install time
import pyjokes #pip install pyjokes
import pyautogui #pip install pyautogui
import geopy #pip install geopy
import requests #pip install requests
import subprocess #pip install subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
        r = sr.Recognizer() 
        with sr.Microphone() as source:
            print("Listning....")
            r.pause_threshold = 2
            audio = r.listen(source,timeout=10,phrase_time_limit=5)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("sir tell me again,please...") 
            return "none"
        query = query.lower()
        return query

def temperature():
    search = "temperature in brajrajnagar"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    speak(f"current temperature outside is {temp}")
    
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=4 and hour<12:
        speak(f"Hello sir, Good morning, its {tt}")
    elif hour>=12 and hour<18:
        speak(f"Hello sir, Good Afternoon, its {tt}")
    elif hour>=18 and hour<=21:
        speak(f"Hello sir, Good evening, its {tt}")
    else:
        speak("Good night sir")
   
    speak("Please tell me how may i help you!")


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])
    
if __name__=='__main__':
    wish()
    while True:
        if 1:  
            query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\Windows\system32\\notepad.exe"
            os.startfile(npath)

        elif "what day is today" in query:
            day = datetime.datetime.today().weekday() + 1
            Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'} 
            day_of_the_week = Day_dict[day]
            speak("Today is " + day_of_the_week)
            
        elif "temperature" in query or "what is the temperature now" in query or "todays temperature" in query:
            search = "temperature in brajrajnagar"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif "how much power left" in query or "how much power we have" in query or "battery" in query or "battery health" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our system have {percentage} percent battery.")
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif percentage<=20 and percentage<=35:
                speak("we don't have enough power to continue our work, please charge the system")
            elif percentage<=15:
                speak("we have very low power, please connect to charging, The system will shutdown very soon.")
            
        elif "open whatsapp" in query:
            bpath = "E:\Whatsapp\\WhatsApp.exe" #paste path of whatsapp in ur computer
            os.startfile(bpath)

        elif "open game" in query:
            speak("ok sir, i am opening a game for you")
            cpath = "E:\Assassin's Creed - Origins\\ACOrigins.exe" #paste path of any game in ur computer
            os.startfile(cpath)

        elif "calculate" in query:
            import operator
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate, example: 3 plus 3")
                audio = r.listen(source)
                query=r.recognize_google(audio)
                print(f"{query}")
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' :operator.__truediv__,
                    'Mod' : operator.mod,
                    'mod' : operator.mod,
                    '^' : operator.xor,
                    }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            print(eval_binary_expr(*(query.split())))
        
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            
        elif "play music" in query or "play songs" in query or "play song" in query or "music please" in query or "sound" in query:
            music_dir = "E:\\music" #paste path of music library in ur computer
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))
            exit()

        elif "what is my ip address" in query or "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            
        elif "internet speed" in query or "check internet speed" in query or "what is my net speed" in query:
             st = speedtest.Speedtest()
             dl = st.download()
             up = st.upload()
             speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
            exit()
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
            exit()
		
        elif "open college portal" in query:
            webbrowser.open("http://www.xyz.com/bete-portal/") #paste link of ur college portal in ur computer
            exit()
        elif "attend class" in query or "open class" in query:
            webbrowser.open("https://meet.google.com/yt-hfg-wzj?pli=1&authuser=4") #paste link of ur class in ur computer
            sys.exit()
             
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            exit()

        elif "open google" in query:
            speak("sir, what should i search in google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            exit()
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
            exit()
            
        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/xyzx") #paste path of your gmail in ur computer
            exit()

        elif "take screenshot" in query:
            ss = pyautogui.screenshot()
            ss.save(r'E:\pictures\Screenshots\ss_2.png')
            speak("screenshot taken sir")

        elif ("do you know how to make coffee") in query or ("how to make coffee") in query:
            speak("of course sir, add coffee powder and add sugar in milk, then boil it for 2 minutes, your cofee is ready, can i taste it sir? ,ha ha ha, just kidding sir!")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "restart the system" in query:
            speak("ok sir system will restart in 10 seconds")
            os.system("shutdown /r /t 10")
            exit()
            
        elif "shutdown the system" in query:
            speak("ok sir, system will shutdown in 10 seconds")
            os.system("shutdown /s /t 10")
            exit()
            
        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(2)
            pyautogui.keyUp("alt")

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
            
        elif "thank you" in query:
            speak("Its my pleasure, any otherwork sir?")
                
        elif ("how are you") in query:
            speak("i am fine sir, hope u must be fine.")
        elif ("what are you") in query:
            speak("I am Your ai assistant sir")

        elif ("which comes first the egg or the chicken") in query or ("which comes first egg or chicken") in query:
            speak("egg chicken,egg chicken,egg chicken, oops stack overflow ")

        elif ("who Created You") in query or ("who made you") in query:
            speak("I was Designed in GIET University, Gunupur")
            
        elif ("are you intelligent") in query:
            speak("Well, when i was at school, i had to cheat on my chemistry exam, by looking into the soul of the girl next to me, she was so talented, i like her.")

        elif ("what do you think of google assistant") in query or ("what do you think of siri") in query or("what do you think of alexa") in query:
            speak ("I am a bigfan of good listeners and helpful beings.")

        elif ("how old are you") in query:
            speak("Age is nothing but a number. But technically, it's also a word.")

        elif ("are you a robot") in query:
            speak("i am not a person or a robot, i am an ai software, here to help you.")

        elif ("who are you") in query:
            speak("i am jarvis, an ai software , and your virtual assistant.")

        elif "search" in query or "please search" in query or "i want to search" in query:
            sr.Microphone(device_index=1)
            r=sr.Recognizer()
            r.energy_threshold=10000
            with sr.Microphone() as source:
                speak("what do you want to Search :")
                audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                print(f"user said: {text}")
                url='https://www.google.co.in/search?q='
                search_url=url+text
                webbrowser.open(search_url)
                speak("Here is some results, You can check.")
                break
                
            except:
                speak("sorry sir, i can't Recognize")

        elif "make a note" in query or "write this down" in query or "remember this" in query:
            speak("What would you like me to write down?")
            note_text = takecommand().lower()
            note(note_text)
            speak("I've made a note of that.")
                        
        elif "you can sleep" in query or "sleep now" in query or "exit" in query:
            speak("okey sir, i am going to sleep, but you can call me anytime.")
            sys.exit()
		
	#you can add more elif conditions according to ur need.
