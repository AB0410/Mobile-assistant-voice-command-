import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
#import face_recog
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning")

    elif hour >= 12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good Evening")
    speak("Hello sir I am clara, how can i help you ?")


def take_cmd():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('basu.arjit4@gmail.com','myphone4')
    server.sendmail('basu.arjit4@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = take_cmd().lower()

        # Logic for excuting tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open steam' in query:
            webbrowser.open("https://store.steampowered.com/")

        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=Qe500eIK1oA&list=RDQe500eIK1oA&start_radio=1_")
        
        elif 'the time' in query:
            str_time =  datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {str_time}")
        
        elif 'email to user' in query:
            try:
                speak("what should i say?")
                content = take_cmd()
                to = "maidmyday40@gmail.com"
                send_email(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry email not sent !!!")
        elif 'can you see me' in query:
            speak("yes i can see you")
            import face_recog





        elif 'shut down' in query:
            break







