import speech_recognition as sr
import webbrowser
import os
import pyttsx3
import time
import musiclibrary
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


def processcommand(c):
    if "open google" in c.lower():
        speak("Opening google")
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        speak("Opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        speak("Opening linkedin")
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        speak("Opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open watsaap" in c.lower():
        speak("Opening watsaap")
        webbrowser.open("https://web.whatsapp.com")
    elif c.lower().startswith("play"):
        speak("playing the song")
        song = c.lower().replace("play", "", 1).strip()
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
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