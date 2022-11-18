import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
from selenium import webdriver
from gtts import gTTS
import playsound
import time

#Variables

 #Reccomendations

   #Music
music_reccomendations = ['Murder In My Mind by Kordhell', 'Scrapyard by KSLV Noh', 'SHADOW by ONIMXRU', 'NEON BLADE by MoonDeity', 'Live Another Day by Kordhell', 'SUNRISE (Slowed + Reverb) by Xantesha', 'MIDNIGHT by PLAYAMANE', 'Phony Tribu by Funk Tribu', 'Demons Around by yatashigang', 'PSYCHO CRUISE by ONIMXRU']
random_music_reccomendations = random.choice(music_reccomendations)

 #Greets and stuff
greets = ['Howdy', 'Hello', 'Hey there']
random_greets = random.choice(greets)
 
 #Thank you's and stuff
thankyous = ['No problem', 'No thank you!', 'That is nice of you to say', 'No worries']
random_thankyous = random.choice(thankyous)

 #Jokes

jokes = ['What is the best thing about Switzerland? I do not know, but the flag is a big plus.', 'Did you hear about the mathematician who iss afraid of negative numbers? He will stop at nothing to avoid them.', 'Hear about the new restaurant called Karma? There is no menu: You get what you deserve.', 'Did you hear about the actor who fell through the floorboards? He was just going through a stage.', 'Did you hear about the claustrophobic astronaut? He just needed a little space.', 'Where are average things manufactured? The satisfactory.', 'A man tells his doctor, Doc, help me. I am addicted to Twitter! The doctor replies, “Sorry, I do not follow you …']
random_jokes = random.choice(jokes)

  #Racist jokes
racist_jokes = ['What do you call a black person with a PhD? A nigger.', 'How do you keep a nigger from becoming President? Don not elect one.', 'Why do not niggers like blow jobs? They don not like being called " mouth breathers."', 'How do you get a nigger out of a tree? Cut the rope.', 'How do you get a nigger to mow your lawn? Put a piece of watermelon on the lawn.']
random_racist_jokes = random.choice(racist_jokes)

  #Dad jokes
dad_jokes = ['Why do scientists not trust atoms? Because they make up everything!', 'You know what I saw today? Everything I looked at.', 'Why do fathers take an extra pair of socks when they go golfing? In case they get a hole in one!', 'Singing in the shower is fun until you get soap in your mouth. Then it ss a soap opera.', 'What do you call a factory that makes okay products? A satisfactory.', 'What did the ocean say to the beach? Nothing, it just waved.', 'Why do seagulls fly over the ocean? Because if they flew over the bay, we would call them bagels.', 'I only know 25 letters of the alphabet. I do not know y.', 'How does the moon cut his hair? Eclipse it.']
random_dad_jokes = random.choice(dad_jokes)

 #Racial slurs
racial_slurs = ['Nigger', 'Rice eating strech eye', 'Black Monkey', 'Weird arab terrorist']
random_racial_slurs = random.choice(racial_slurs)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Wigly Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            browser = webdriver.Chrome()
            browser.get('www.youtube.com')

        elif 'open google' in query:
            browser = webdriver.Chrome()
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            browser = webdriver.Chrome()
            webbrowser.open("stackoverflow.com")

        elif 'funny sounds' in query:
            music_dir = 'C:/Users/MARIUCHINAS/Downloads/Sounds'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\MARIUCHINAS\\Downloads\\\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'tell a joke' in query or 'tell me a joke' in query:
            random_jokes = random.choice(jokes)
            speak(random_jokes)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'tell me a racial slur' in query:
            random_racial_slurs = random.choice(racial_slurs)
            speak(random_racial_slurs)

        elif 'tell a racist joke' in query or 'tell me a racist joke' in query:
            random_racist_jokes = random.choice(racist_jokes)
            speak(random_racist_jokes)

        elif 'tell a dad joke' in query or 'tell me a dad joke' in query:
            random_dad_jokes = random.choice(dad_jokes)
            speak(random_dad_jokes)

        elif 'what time is it' in query:
            speak(datetime.datetime.now().strftime('%I:%M %p'))
            print(datetime.datetime.now().strftime('%I:%M %p'))
        
        elif 'what is your name' in query:
            speak("My name is Wigly, Sir")

        elif 'thank you' in query or 'thanks' in query:
            random_thankyous = random.choice(thankyous)
            speak(random_thankyous)

        elif 'hello' in query or 'hi' in query:
            random_greets = random.choice(greets)
            speak(random_greets)

        elif 'favorite show' in query:
            speak("My favorite show is probably Breaking Bad or Beter Call Soul")

        elif 'favorite animated show' in query:
            speak("My favorite animated shows are Rick and morty, Family guy and The Simpsons")
            
        elif 'favorite video game' in query:
            speak("My favorite video games are Minecraft, Valorant and Roblox")

        elif 'what is life' in query or 'what is the meaning of life' in query:
            speak("There is much debate over what the meaning of life is, or whether it exists at all. Unfortunately, I cannot answer that question definitively. However, I can tell you that some people believe that the meaning of life is to find and fulfill our personal mission or purpose. Others believe that life is a never-ending cycle of becoming and passing away to the point where it is difficult to determine what the meaning of life is. Still, others believe that life is simply a brief moment of existence in a much larger picture.")

        elif 'favorite color' in query:
            speak("My favorite color is probably grey because i dont have feelings and i am empty inside")

        elif 'favorite food' in query:
            speak("My favorite food is kebab")

        elif 'favorite hobby' in query:
            speak("My favorite hobby is probably programing")

        elif 'favorite place to go' in query:
            speak("My favorite place to go is into the inner city")

        elif 'favorite book' in query:
            speak("Some of mine favorite books are nothing because books are for nerds lolololol")

        elif 'favorite kind of music' in query or 'favorite type of music' in query:
            speak("My favorite type of music is Phonk")

        elif 'music recommendations' in query:
            random_music_reccomendations = random.choice(music_reccomendations)
            speak(f"I reccomend {random_music_reccomendations} ")