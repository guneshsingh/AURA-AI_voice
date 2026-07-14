# importing modules that are needed.
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

# Initializes the text-to-speech engine and converts the given text into spoken audio
def speak(text):
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    print("Finished speaking")
# Activating the openAI
client=OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
# Sends the user's question to the AI model and returns the generated response
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
# A dictionary containing link of the websites that are accessible by AURA
websites = {
    "google": "https://google.com",
    "facebook": "https://facebook.com",
    "linkedin": "https://linkedin.com",
    "youtube": "https://youtube.com",
    "whatsapp": "https://web.whatsapp.com",
}
# After accepting the command it executes it in different ways
def processcommand(c):
    command = c.lower().strip()
    # Part of the function that performs opening tasks of websites
    if "open" in command.lower():
        matched=False
        for site in websites:
            if site in command:
                speak(f"Opening {site}")
                webbrowser.open(websites[site])
                matched=True
                break
        if not matched:
                speak("Sorry, I don't know that website.")
    #Part of the function that plays different songs
    elif "play" in command.lower():
        found=False
        for song in musiclibrary.music:
            if song in command:
                speak(f"Playing {song}")
                webbrowser.open(musiclibrary.music[song])
                found=True
        if not found:
            speak("Sorry, I couldn't find that song.")
    #Part of the function that displays the latest news
    elif "news" in c.lower():
        speak("News for today")
        webbrowser.open("https://www.thehindu.com/")
    # All the other tasks which are performed by openAI
    else:
        answer = ask_ai(c)
        print(answer)
        speak(answer)

        
# MAIN PART OF THE PROGRAM
if __name__=="__main__":
    speak("Initialising AURA.............")
    # Assining a variable with False so that it moves in a loop
    active=False
    # assigning the timeout so that after that much time it exits the loop
    idle_timeout=60
    last_time=None
    while True:
       
        try:
            #If wake word is not initiated
            if not active:
                with sr.Microphone() as source:
                    print("Listening..........")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
                print("Recognising")
                word=recognizer.recognize_google(audio)
                print(word)
                # if user wishes to exit the loop without the waking command 
                if "exit" in word.lower():
                    speak("Exiting AURA!!!! Thank You .............. See you soon!!")
                    break
                # Activating AURA
                if "hello" in word.lower():
                    print("AURA active..........")
                    speak("hey!!good to see you.")
                    speak("AURA active..........")
                    active=True
                    time.sleep(1)
            else:
                #IF wake word is already initiated
                try:
                    with sr.Microphone() as source:
                        print("Listening for command")
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        audio = recognizer.listen(source)
                    print("Recognising")
                    command=recognizer.recognize_google(audio)
                    print(command)
                    #if user want to exit after waking up AURA
                    if "exit" in command.lower():
                        
                        processcommand(command)
                        speak("Exiting Aura!!")
                        break
                    processcommand(command)
                    # If for 60 seconds no speech is detected then timeout
                except sr.WaitTimeoutError:
                    print("No speech detected")
                    if time.time()-last_time>idle_timeout:
                        print("TimeOut!!!!!!!!")
                        speak("Going back to sleep.say hello to wake me up")

        #if no speech is detected
        except sr.WaitTimeoutError:
            speak("No speech detected.")
        #if the command is not understood 
        except sr.UnknownValueError:
            speak("Couldn't understand.")
        #internet connection is not active
        except sr.RequestError:
            speak("Internet connection error.")
        #to deal with other types of errors.
        except Exception as e:
            print(type(e).__name__, e)
