# 🎙️ AI Voice Assistant (Python + OpenAI GPT-4o-mini)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![OpenAI API](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent **voice-controlled AI assistant** built in Python that listens to your commands, understands natural language using **OpenAI’s GPT-4o-mini**, and responds with **speech**.  
It can open websites, desktop applications, tell the time/date, and answer questions — just like a personal smart assistant!

---

## 🚀 Features

✅ Voice recognition using `SpeechRecognition`  
✅ Text-to-speech replies via `pyttsx3`  
✅ AI-powered responses using **GPT-4o-mini**  
✅ Opens apps and popular websites (YouTube, WhatsApp, LinkedIn, etc.)  
✅ Continuous listening loop for interactive conversation  

---

## 🧩 Tech Stack

| Component | Library / Tool |
|------------|----------------|
| AI Model | OpenAI GPT-4o-mini |
| Speech Recognition | `speech_recognition`, `PyAudio` |
| Text-to-Speech | `pyttsx3` |
| Environment | Python 3.10+ |
| Platform | Windows (recommended) |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-assistant.git
cd ai-assistant
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```bash
# .env
OPENAI_API_KEY=your_OpenApi_key
MODEL=gpt-4o-mini
```

> 💡 **Important:**
> Never expose your real API key in public repositories.
> Use the `.env` file locally and make sure `.gitignore` includes it (which it does).

---

### 5️⃣ Run the Assistant

```bash
python assistant.py
```

You’ll hear:

> 🎧 “Hello, I am your AI assistant. How can I help you?”

Now start speaking — for example:

* “Open YouTube”
* “Tell me about Elon Musk”
* “What’s the time?”
* “Open LinkedIn”
* “Who invented Tesla?”

---

## 📁 Project Structure

```
ai-assistant/
│
├── assistant.py          # Main AI assistant code
├── requirements.txt      # Dependencies
├── .env                  # API keys (ignored by Git)
├── .gitignore            # Ignore system and venv files
└── README.md             # Project documentation
```

---

## 📦 Example Commands

| Command                   | What It Does                     |
| ------------------------- | -------------------------------- |
| “Open YouTube”            | Launches YouTube in your browser |
| “What’s the time?”        | Speaks the current time          |
| “Tell me about Elon Musk” | GPT explains Elon Musk in voice  |
| “Open WhatsApp”           | Opens WhatsApp Web               |
| “Exit”                    | Ends the assistant               |

---

## 🧠 How It Works

1. Your voice is captured using the microphone (`SpeechRecognition`).
2. Converted to text via Google Speech API.
3. The text is sent to **OpenAI GPT-4o-mini** for understanding.
4. The response is spoken aloud using `pyttsx3`.

---



