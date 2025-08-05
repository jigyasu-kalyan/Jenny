# 🎙️ Jenny – Voice-Activated Virtual Assistant  

Jenny is a Python-based **voice-activated assistant** with wake word detection, speech recognition, text-to-speech (TTS), and system automation capabilities.  
It can open/close applications, play music, browse websites, and is designed with future AI integration support using OpenAI API.  

---

## ✨ Features  
- 🔊 **Wake word detection** – Activates on the word "Jenny"  
- 🎤 **Speech recognition** – Uses `SpeechRecognition` for command input  
- 🗣️ **Text-to-Speech (TTS)** – Powered by `gTTS` with cached audio for faster response  
- 🖥️ **System automation** – Open/close apps like Telegram, WhatsApp, ChatGPT  
- 🌐 **Web automation** – Opens YouTube, Wikipedia, and plays specific songs  
- 🔑 **Secure API usage** – Environment variable support for OpenAI API key  
- 🔄 **Scalable design** – Ready for AI response generation integration  

---

## 🛠️ Tech Stack  
- **Python**  
- `SpeechRecognition` – Speech-to-text  
- `gTTS` – Text-to-speech conversion  
- `Pygame` – Audio playback  
- `pydub` – Audio manipulation  
- `subprocess` & `webbrowser` – System and web automation  
- *(Optional)* `OpenAI` – AI response generation (environment-secured)  

---

## 🚀 Setup & Installation  

1. **Clone the repository**  
     git clone https://github.com/jigyasu-kalyan/Jenny.git
     cd Jenny
2. Create and activate a virtual environment
     python3 -m venv myenv
     source myenv/bin/activate   # Mac/Linux
     myenv\Scripts\activate      # Windows
3. Install dependencies
     pip install -r requirements.txt
4. (Optional) Set up OpenAI API key
     export OPEN_AI_API="your_openai_api_key"      # Mac/Linux
     setx OPEN_AI_API "your_openai_api_key"        # Windows
5. Run the assistant
     python main.py

🎯 Usage
- Say "Jenny" to wake the assistant.
- Speak commands like:
- "Introduce team"
- "Open YouTube"
- "Play Nadaniya"
- "Close Telegram"

🔮 Future Improvements
- Integrate OpenAI API for AI-driven conversational responses
- Add cross-platform desktop notifications
- Expand command set (calendar, reminders, weather)

👨‍💻 Author

Jigyasu Kalyan
