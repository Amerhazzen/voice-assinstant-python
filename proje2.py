import time
import datetime
import pywhatkit
import pyttsx3
import wikipedia
import speech_recognition as sr
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.recognizer()
    with sr.microphone() as source:
        print("listening!....")
        audio = recognizer.listening(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"user siad:{command}")
        except sr.UnknownValueError:
            print("sorry, i did not understand that")
            return None
        return command.lower()
def respond(command):
    if "hello" in command:
        speak("hello! how can I assist you today:")
    elif "time" in command:
        time_now = datetime.datetime.now().strftime('%H:%M')
        speak(f"the current time is{time_now}")
    elif 'date' in command:
        date_today = datetime.datetime.now().strftime('%Y,%m,%d')
        speak(f"today date is{date_today}")
    elif 'search'in command:
        topic = command.replace('search', '').strip()
        speak(f"searching wikipedia for{topic}")
        result = wikipedia.summary(topic, sentence=1)
        speak(result)
    elif 'play music' in command:
        speak("play music on youtube")
        pywhatkit.playonyt("music")
    elif 'set reminder' in command:
        speak('what is the reminder?')
        reminder = listen()
        speak("when would you like to be reminder? please say the time in HH:MM format.")
        reminder_time = listen()
        try:
            reminder_hour, reminder_minute = map(int, reminder_time.split(":"))
            reminder_time_obj = datetime.datetime.now().replace(hour=reminder_hour,minute=reminder_minute, second=0)
            if reminder_time_obj < datetime.datetime.now():
                reminder_time_obj += datetime.timedelta(days=1)
            time_difference = (reminder_time_obj - datetime.datetime.now()).total_seconds()
            speak(f"reminder set for{reminder_time_obj.strftime('%Y-%m-%d %H:%M')}.")
            time.sleep(time_difference)
            speak(f"reminder:{reminder}")
        except:
            speak("sorry, I could not understand the time format. please try again")
    elif 'exit' in command:
        speak("Goodbaye. Have a nice day!")
        exit()
    else:
        speak("sorry, I did not understand that. can you try again?")
if __name__ == "__main__":
    speak("Hello, I am Amirhossein. how can i help you?")
    while True:
        command = listen()
        if command:
            respond(command)