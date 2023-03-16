import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good morning!")
    elif hour >= 12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("Hi i'm Friday ! Please tell me how can i be of assistance ?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-bg')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Can you repeat please?")
        return None
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com', 'Testmail369')
    server.sendmail('email@gmail.com', to , content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is exactly {strtime}")

        elif "Play music" in query:
            webbrowser.open("https://www.youtube.com/watch?v=u4Cr0h4vXDg&ab_channel=ParkerMichael")
