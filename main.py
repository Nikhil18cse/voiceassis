import speech_recognition as sr
import pyttsx3
from selenium import webdriver

recognizer = sr.Recognizer()
engine = pyttsx3.init()
driver = webdriver.Chrome()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("Sorry, I couldn't understand your request. Please try again.")
        return ""

def open_website(url):
    driver.get(url)

command = listen()

if command:
    if "hi" in command:
        speak("Hello")
    elif "open youtube" in command:
        speak("Opening YouTube.")
        open_website("https://www.youtube.com/")
    else:
        speak("Command not recognized.")
