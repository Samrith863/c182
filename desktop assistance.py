from tkinter import *
import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
from datetime import datetime
root = Tk()
root.geometry("500x500")
root.configure(bg="light blue")

label_hi=Label(root,text="Welcome to the desktop assistant",font=("Arial",30,"bold"),bg="light blue")
label_hi.place(relx=0.5,rely=0.2,anchor=CENTER)

text_to_speech=pyttsx3.init()
def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()



def r_audio():
    speak("How can I help you?")
    
        
    speech_recognisor= sr.Recognizer()
    with sr.Microphone() as source:
        audio=  speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data=  speech_recognisor.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('Please repeat i did not get that')
            speak("please repeat, i did not get that")
    respond(voice_data)
    
def respond(voice_data):
    print(voice_data)
    if "name" in voice_data:
        speak("Hello, my name is Sam")
        print("Hello, my name is Sam")
    if "time" in voice_data:
        speak("the current time is:")
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
    if "search" in voice_data:
        print("Opening google")
        speak("Opening google")
        webbrowser.get().open("https://www.google.com/")
    if "video" in voice_data:
        print("Opening Youtube")
        speak("Opening Youtube")
        webbrowser.get().open("https://www.youtube.com/")
    if "videos" in voice_data:
        print("Opening Youtube")
        speak("Opening Youtube")
        webbrowser.get().open("https://www.youtube.com/")
    if "text editor" in voice_data:
        print("Opening text editor")
        speak("Opening text editor")
        subprocess.Popen(["notepad.exe"])
    
    
btn=Button(root,text="Start",bg="red",fg="white",relief=FLAT,padx=10,pady=1,font=("Arial",10,"bold"),command=r_audio)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()