import pyttsx3 
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()    


def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!, Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!, Sir")   

    else:
        speak("Good Evening!, Sir")  

    speak("I am Jarvis, How may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)  
        print("Say that again please...")  
        speak("i didn't get it, Sir")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'hi','hello' in query:
            speak("Hello, I am your own personal assistant, Caren")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")   

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\91777\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    

        elif 'email to Amar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "puflex@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, Sir. I am not able to send this email")     

        elif 'open arduino' in query:
            codePath = "C:\\Program Files (x86)\\arduino-1.8.10\\arduino.exe" 
            os.startfile(codePath)        


        elif 'open my youtube account' in query:
            webbrowser.open("https://www.youtube.com/channel/UCNmD23ZDlzXAKLYjGQUINLQ?view_as=subscriber")