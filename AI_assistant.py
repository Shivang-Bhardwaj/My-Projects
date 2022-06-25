import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


friend=pyttsx3.init()
voices=friend.getProperty('voices')
friend.setProperty('voice',voices[2].id)
friend.setProperty('rate',160)


def speak(text):
    friend.say(text)
    friend.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am R.C. Sir, version 1 point 0. Do you want any help?')


def takeCommand():
    ''' take microphone input and return string '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio=r.listen(source)
        try:
            print('Recognising...')
            query=r.recognize_google(audio,language='en-in')
            print(f'You said: {query}\n')
        except:
            print('Say that again please')
            return 'None'
        return query





if __name__=='__main__':
    wishMe()
    while True:
        query=takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak('According to wikipedia-')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open bing' in query:
            webbrowser.open('bing.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'search songs' in query:
            webbrowser.open('https://gaana.com')

        elif 'play music' in query:
            music_dir=r'C:\Users\DELL PC\Music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'The time is {strTime}')

        elif 'open vs code' in query:
            codePath=r"C:\Users\DELL PC\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'open paint' in query:
            codePath=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint'
            os.startfile(codePath)

        elif 'quit' in query:
            exit()