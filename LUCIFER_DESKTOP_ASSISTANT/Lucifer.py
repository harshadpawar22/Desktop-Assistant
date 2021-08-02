import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
import operator
import smtplib
import wolframalpha
import json
import requests
import pyjokes



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) 
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Lucifer. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing")
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please")    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")
    server.sendmail("RECIVERS EMAIL ADDRESS", to, content)
    server.close()

    
if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if "good bye" in query or "ok bye" in query or "stop" in query:
            speak('your personal assistant LUCIFER is shutting down,Good bye')
            print('your personal assistant LUCIFER is shutting down,Good bye')
            break        

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)   

        elif 'question' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="J72884-K75HUPLPH4"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'who are you' in query or 'what can you do' in query:
            speak('I am LUCIFER version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
            print('I am LUCIFER version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')      


        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Harshad")
            print("I was built by Harshad")

        elif "how are you" in query:
            speak('I am good, thankyou for asking. How may I help you')
            print('I am good, thankyou for asking. How may I help you')

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())               
            
        elif 'weather' in query:
            api_key="944b4f22ca390b9cb7066041f0cb234a"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak("Temperature in " +
                       str(city_name) +
                      "\nTemperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print("Temperature in " +
                       str(city_name) +
                      "\nTemperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))                       

        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open(query)
                
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open meet' in query:
            webbrowser.open("https://meet.google.com/") 

        elif 'open classroom' in query:
            webbrowser.open("https://classroom.google.com/u/1/h") 

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")          

        elif 'open yahoo' in query:
            webbrowser.open("yahoo.com")    

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query:
            music_dir = 'D:\\Python\\Desktop_Assistant\\Music'
            songs = os.listdir(music_dir)
            print(songs) 
            d=random.choice(songs)   
            os.startfile(os.path.join(music_dir, d))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")    

        elif 'open code' in query:
            codePath = "C:\\Users\\H PAWAR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'open brave' in query:
            codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath) 

        elif 'open downloads' in query:
            codePath = "C:\\Users\\H PAWAR\\Downloads"
            os.startfile(codePath)

        elif 'open documents' in query:
            codePath = "C:\\Users\\H PAWAR\\Documents"
            os.startfile(codePath) 

        elif 'open pitcures' in query:
            codePath = "C:\\Users\\H PAWAR\\Pictures"
            os.startfile(codePath)

        elif 'open word' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\WINWORD.exe"
            os.startfile(codePath)
        
        elif 'open outlook' in query:
            codePath = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\OUTLOOK.exe"
            os.startfile(codePath)

        elif 'email to ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ("RECIVERS EMAIL ADDRESS")
                print(to)   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")

        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])        
                
        
  