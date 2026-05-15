import os
import webbrowser
import pyautogui
import pygame
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour<12:speak("Good morning sir")
    elif hour>12 and hour<18:speak("Good after noon sir")
    else:speak("Good evening sir")


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:

        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        return text

def div(q):
    q=q.split("plus")
    queries=[]
    for i in range(len(q)):
        if "+" in q[i]:
            l=q[i].split("+")
            for j in l:
                queries.append(j)
        else:
            queries.append(q[i])
    return queries
def sound(a):
    # Initialize the mixer
    pygame.mixer.init()
    pygame.mixer.music.load(a)
    pygame.mixer.music.play()

    # print("start speaking")

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

limit=0
if __name__ == "__main__":
    wishme()
    while True:
        try:
            sound(r"C:\Users\karsh\PycharmProjects\some_extra\effects\say.mp3")
            queries=div(listen().lower())
            print(*queries)
        except sr.UnknownValueError:speak("Sorry, I did not understand that.");continue
        except sr.RequestError:speak("Sorry,something went wrong");break
        for query in queries:
            if 'wikipedia' in query and len(query)!=9:
                speak('Searching Wikipedia...')
                try:
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except:
                    speak("didn't found for what you were searching ")
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")
            elif "joke" in query or "jokes" in query or "something funny" in query:
                print(x:=pyjokes.get_joke())
                speak(x)

            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")
            elif "quit" in query or "leave it" in query or "exit" in query:
                quit()
            elif "aaspaas" in query or "aas paas" in query or "aas pass" in query or "introduction" in query:
                speak(" Hey there! I’m your digital assistant, ready to make your day smoother. Need answers, recommendations, or just a friendly chat? Let’s dive in and explore together")
            elif "fuck" in query or "bitch" in query:
                if limit:
                    speak("I’ll need to step back for now since we went off track. Take care!")
                    sound(r"C:\Users\karsh\PycharmProjects\some_extra\effects\off.mp3")
                    quit()
                else:
                    speak("I’d appreciate it if we keep things respectful. Let's keep our chat positive!")
                limit += 1
            elif "your name" in query:
                speak("I have no name. You can call me whatever you want")

            elif "say" in query:
                speak(query[query.rfind("say")+3:])
            elif "voice typing" in query:
                pyautogui.hotkey("win","h")
            elif "how r u" in query or "how are you" in query:
                speak("i am fine what about you")
            elif "owner" in query or "master" in query or "who built" in query :
                speak("I was created by a wizard and AI enthusiasts, "
                      "dedicated to making conversations more engaging and insightful. Just "
                      "think of me as your friendly digital companion, powered by some serious brainpower!")
            elif "fine" in query:
                speak("Great to hear that")
            elif "saved tab" in query or "saved tabs" in query:
                pyautogui.hotkey("alt","o")
            elif "battery status" in query:
                pyautogui.hotkey("alt","b")
            elif "close tab" in query:
                pyautogui.hotkey("ctrl","w")
            elif "camera" in query:
                os.system("start microsoft.windows.camera:")
            elif "python" in query or "pycharm" in query or "pie chart" in query:
                os.system(r"start pycharm64.exe")


