from openai import OpenAI
import speech_recognition as sr
import pyttsx3
import os
import time

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 175)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Female voice (optional)


def speak(text):
    """Speak and print text safely in chunks."""
    print("Assistant:", text)
    max_length = 200  # number of characters per chunk

    # Split long responses so pyttsx3 doesn't fail silently
    for i in range(0, len(text), max_length):
        chunk = text[i:i+max_length]
        engine.say(chunk)
        engine.runAndWait()



def listen():
    """Listen through mic and convert to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""


def ask_gpt(prompt):
    """Ask GPT for a response."""
    try:
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=[
                {"role": "system", "content": "You are a helpful personal voice assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


def open_application(cmd):
    """Open desktop apps or websites."""
    sites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "whatsapp": "https://web.whatsapp.com",
        "linkedin": "https://linkedin.com",
        "gmail": "https://mail.google.com",
        "facebook": "https://facebook.com",
        "instagram": "https://instagram.com",
        "twitter": "https://twitter.com",
        "spotify": "https://open.spotify.com",
        "chatgpt": "https://chat.openai.com"
    }

    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "start chrome",
        "edge": "start msedge",
        "command prompt": "cmd.exe"
    }

    for name, link in sites.items():
        if name in cmd:
            os.system(f"start {link}")
            speak(f"Opening {name}")
            return True

    for name, path in apps.items():
        if name in cmd:
            os.system(path)
            speak(f"Opening {name}")
            return True

    return False


def tell_time():
    """Return current time."""
    current_time = time.strftime("%I:%M %p")
    return f"The time is {current_time}."


def tell_date():
    """Return current date."""
    today = time.strftime("%A, %B %d, %Y")
    return f"Today is {today}."


def execute_command(cmd):
    """Main command logic."""
    if "open" in cmd or "launch" in cmd:
        if not open_application(cmd):
            speak("I don't recognize that app or website.")
    elif "time" in cmd:
        speak(tell_time())
    elif "date" in cmd:
        speak(tell_date())
    elif "exit" in cmd or "stop" in cmd or "quit" in cmd:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("Let me think...")
        reply = ask_gpt(cmd)
        speak(reply)



def main():
    speak("Hello, I am your AI assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            execute_command(command)


if __name__ == "__main__":
    main()
