import speech_recognition as sr
import webbrowser
import os
import pyttsx3
import time
import musiclibrary
import webbrowser

from openai import OpenAI
recognizer=sr.Recognizer()
from dotenv import load_dotenv
import os
load_dotenv()

def speak(text):
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    print("Finished speaking")

client=OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
def ask_ai(question):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are aura, a friendly voice assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content
#if you want to add more websites , add here inside the website (in dict. format )
websites = {
    "google": "https://google.com",
    "facebook": "https://facebook.com",
    "linkedin": "https://linkedin.com",
    "youtube": "https://youtube.com",
    "whatsapp": "https://web.whatsapp.com",
}
    

def processcommand(c):
    command = c.lower().strip()
    
    if command.startswith("open"):
        website = command.replace( "open", "",1).strip()
    
        if website in websites:
                speak(f"Opening {website}")
                webbrowser.open(websites[website])
        else:
                speak("Sorry, I don't know that website.")

    elif command.startswith("play"):
        song = command.replace("play", "", 1).strip()
        if song in musiclibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musiclibrary.music[song])
        else:
            speak("Sorry, I couldn't find that song.")
    elif "news" in command:
        speak("News for today")
        webbrowser.open("https://www.thehindu.com/")
    else:
        answer = ask_ai(c)
        print(answer)
        speak(answer)

        
    

if __name__=="__main__":
    speak("Initialising AURA.............")
    while True:
       
        try:
            with sr.Microphone() as source:
                print("Listening..........")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
            print("Recognising")
            word=recognizer.recognize_google(audio)
            if "aura" in word.lower():
                print("AURA active..........")
                speak("YA")
                time.sleep(1)
                with sr.Microphone() as source:
                    print("Listening for command")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source)
                command=recognizer.recognize_google(audio)
                processcommand(command)


        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Couldn't understand.")

        except sr.RequestError:
            print("Internet connection error.")

        except Exception as e:
            print(type(e).__name__, e)
