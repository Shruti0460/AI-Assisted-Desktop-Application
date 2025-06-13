hi
# AI-Assisted-Desktop-Application
This project is an AI-powered desktop assistant built using Python. It can interact with users through voice commands and respond using speech. The assistant is capable of performing several tasks, such as opening websites, sending messages, and responding intelligently to queries — making human-computer interaction more natural and efficient.

The primary objective of this assistant is to provide hands-free desktop automation, increase productivity, and demonstrate the integration of artificial intelligence with real-time system control.

💡 Key Features:
🎙️ Voice Recognition using Speech Recognition (speech_recognition)

🔊 Text-to-Speech using pyttsx3 to talk back to the user

🌐 Web Automation like opening YouTube, Google, Wikipedia via voice commands

💬 Custom Commands like “stop,” “exit,” or “send WhatsApp message”

📲 (Optional) WhatsApp Messaging Automation using pywhatkit

🧠 (Extendable) Connect with OpenAI for intelligent responses

⚙️ Technologies Used:
Python

speech_recognition – for capturing voice input

pyttsx3 – for voice output

webbrowser – to open websites

pyautogui – for automating mouse/keyboard if needed

(Optional) pywhatkit – for WhatsApp message automation

(Optional) openai – to integrate GPT-based responses

🎯 How It Works:
On launch, the assistant greets the user and starts listening.

It captures voice commands through the microphone.

Based on the input:

It can open specific websites.

Send messages.

Exit on voice command like "stop" or "exit".

Uses speech output to confirm every action it performs.

