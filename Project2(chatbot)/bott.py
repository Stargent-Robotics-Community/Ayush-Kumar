import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()

introduction = " Hi myself alexa , how may i hep you"
engine.say(introduction)
engine.runAndWait()


def command():

    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        listener.pause_thresh1old = 1
        print("listening....")

        audio=listener.listen(source)
        word=listener.recognize_google(audio)
        print(word)

        try:
            if word == "hello":
                print(" hello sir, how may i help you")
                engine.say("hello sir, how may i help you")
                engine.runAndWait()


            elif word == "tell about yourself":
                print("i am chatbot,made by ayush")
                engine.say("i am chatbot,made by ayush")
                engine.runAndWait()
                return command()

            elif word == "how are you ":
                print("i am fine thankyou sir ")
                engine.say(" i am fine thankyou sir")
                engine.runAndWait()
                return command()

            elif word == " ok then byee ":
                print(" bye sir ,have a good day")
                engine.say("bye sir ,have a good day")
                engine.runAndWait()
                return command()

            elif word == "thanks ":
                print(" welcome ")
                engine.say(" welcome ")
                engine.runAndWait()
                return command()

            elif word == "open google":
                print("opening google")
                engine.say("opening google")
                engine.runAndWait()
                webbrowser.open("www.google.com")
                return command()







        except:
             engine.say("sorry, Try again")
             print(": sorry try again")
             return command()
command()


