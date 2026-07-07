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
    active=False
    idle_timeout=60
    last_time=None
    while True:
       
        try:
            if not active:
                with sr.Microphone() as source:
                    print("Listening..........")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
                print("Recognising")
                word=recognizer.recognize_google(audio)
                print(word)

                if "exit" in word.lower():
                    speak("Exiting AURA!!!! Thank You .............. See you soon!!")
                    break

                if "hello" in word.lower():
                    print("AURA active..........")
                    speak("hey!!good to see you.")
                    speak("AURA active..........")
                    active=True
                    time.sleep(1)
            else:
                try:
                    with sr.Microphone() as source:
                        print("Listening for command")
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        audio = recognizer.listen(source)
                    print("Recognising")
                    command=recognizer.recognize_google(audio)
                    print(command)
                    if "exit" in command.lower():
                        
                        processcommand(command)
                        speak("Exiting Aura!!")
                        break
                    processcommand(command)
                except sr.WaitTimeoutError:
                    print("No speech detected")
                    if time.time()-last_time>idle_timeout:
                        print("TimeOut!!!!!!!!")
                        speak("Going back to sleep.say hello to wake me up")


        except sr.WaitTimeoutError:
            speak("No speech detected.")

        except sr.UnknownValueError:
            speak("Couldn't understand.")

        except sr.RequestError:
            speak("Internet connection error.")

        except Exception as e:
            print(type(e).__name__, e)
