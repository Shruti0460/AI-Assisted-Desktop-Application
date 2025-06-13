import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import wikipedia

def say(text):
    """Speak out the given text"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """Takes voice input from user and returns it as a string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"🗣️ You said: {query}")
            return query.lower()
        except Exception as e:
            print("❌ Error:", e)
            say("Sorry, I didn't catch that. Please try again.")
            return ""

if __name__ == '__main__':
    print("🟢 Voice Assistant Started")
    say("Hello! I am ready to assist you.")

    sites = [
        ["youtube", "https://youtube.com"],
        ["wikipedia", "https://www.wikipedia.com"],
        ["google", "https://google.com"]
    ]

    while True:
        query = takeCommand()

        # 🔹 Open websites
        found = False
        for site in sites:
            if site[0] in query:
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
                found = True
                break
        if found:
            continue

        # 🔹 Send WhatsApp Message
        if "whatsapp" in query:
            say("Who should I send the message to? Please say the number.")
            number = takeCommand().replace(" ", "")
            say("What should I say?")
            message = takeCommand()
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute + 1
            try:
                pywhatkit.sendwhatmsg(f"+91{number}", message, hour, minute)
                say("WhatsApp message scheduled successfully.")
            except Exception as e:
                print(e)
                say("Sorry, the message could not be sent.")

        # 🔹 Tell the current time
        elif "time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            say(f"The current time is {time}")

        # 🔹 Tell a joke
        elif "joke" in query:
            joke = pyjokes.get_joke(language="en", category="all")
            say(joke)

        # 🔹 Wikipedia Search
        elif "wikipedia" in query or "tell me about" in query:
            say("Searching Wikipedia...")
            try:
                topic = query.replace("wikipedia", "").replace("tell me about", "")
                result = wikipedia.summary(topic, sentences=2)
                say("According to Wikipedia")
                say(result)
            except:
                say("Sorry, I could not find anything on Wikipedia.")

        # 🔹 Exit command
        elif "stop" in query or "exit" in query or "goodbye" in query:
            say("Okay. Shutting down your assistant.")
            break

        # 🔹 Unknown command
        else:
            say("Sorry, I didn't understand that.")
