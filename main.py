import os
import speech_recognition as sr
from gtts import gTTS
import pygame  # Import pygame for audio playback
from pydub import AudioSegment  # Import pydub for audio manipulation
from openai import OpenAI
import webbrowser
import subprocess
import time

# Initialize the OpenAI API Key
# client = OpenAI(
#     api_key=os.environ["OPEN_AI_API"]
# )
# def get_openai_response(prompt):
#     try:
#         chat_completion = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }
#             ]
    #     )
    #     return chat_completion.choices[0].message
    # except Exception as e:
    #     return f"Error: {e}"

# Cache directory to store pre-generated audio
CACHE_DIR = "cache/"
os.makedirs(CACHE_DIR, exist_ok=True)

# Initialize pygame mixer with custom buffer size (larger buffer can reduce lags)
pygame.mixer.init(buffer=512)  # Default is 4096, lower values reduce latency but can cause stuttering

# Function to change the speed of audio playback using pydub
def change_speed(audio, speed=1.20):
    return audio.speedup(playback_speed=speed)

# Function to play sound using pygame
def play_sound_with_pygame(audio_file):
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Prevents script from ending while audio plays

# Function to check if an audio file exists and generate it if not
def get_audio_path(text, speed=1.0):
    file_name = f"{CACHE_DIR}{hash(text)}.mp3"
    if not os.path.exists(file_name):
        tts = gTTS(text=text, lang='en', slow=False)  # Set slow=False for normal speed
        tts.save(file_name)
    
    # Load and optionally modify the audio file
    audio = AudioSegment.from_mp3(file_name)
    
    if speed != 1.0:
        modified_audio = change_speed(audio, speed)
        modified_file_name = f"{CACHE_DIR}{hash(text)}_speed_{speed}.mp3"
        modified_audio.export(modified_file_name, format="mp3")
        return modified_file_name
    
    return file_name

# Function to speak using pre-cached or newly generated speech
def speak(text, speed=1.0):  # Added speed parameter
    audio_file = get_audio_path(text, speed)
    try:
        play_sound_with_pygame(audio_file)
    except Exception as e:
        print(f"Error playing sound: {e}")

def close_application(app_name):
    try:
        subprocess.run(["osascript", "-e", f'quit app "{app_name}"'])
        speak(f"Successfully closed {app_name}.")
    except Exception as e:
        speak(f"Error closing {app_name}.", speed=1.2)
        print(f"Error closing {app_name}: {e}")

# Function to process recognized commands
def process_command(command):
    command = command.lower()

    if "introduce team" in command:
        speak("Of course! Hi everyone, I’m Jenny, here to assist, Let me introduce you to the amazing team behind this project", speed=1.3)
        speak("Team Leader and Database Manager, Ritesh", speed=1.3)
        speak("A.I. and Machine Learning Specialist, Jigyasu", speed=1.3)
        speak("Backend Developer, Manya", speed=1.3)
        speak("Frontend Developer, Satyam and Swati", speed=1.3)
        speak("Q A Tester, Pranavi", speed=1.3)

    elif "introduce yourself" in command:
        speak("Hi, I am Jenny, a virtual voice-activated assistant!", speed=1.2)

    elif "open gpt" in command:
        speak("Opening GPT for you...", speed=1.3)
        subprocess.Popen(["open", "-a", "ChatGPT"])

    elif "close gpt" in command:
        close_application("ChatGPT")

    elif "open telegram" in command:
        speak("Opening Telegram for you...", speed=1.3)
        subprocess.Popen(["open", "-a", "Telegram"])

    elif "close telegram" in command:
        close_application("Telegram")

    elif "open whatsapp" in command:
        speak("Opening Whatsapp for you...", speed=1.3)
        subprocess.Popen(["open", "-a", "Whatsapp"])

    elif "close whatsapp" in command:
        close_application("Whatsapp")

    elif "close settings" in command:
        close_application("Settings")

    elif "open youtube" in command:
        speak("Opening YouTube for you.", speed=1.2)
        webbrowser.open("https://www.youtube.com")
    
    elif "open wikipedia" in command:
        speak("Opening Wikipedia for you.", speed=1.2)
        webbrowser.open("https://www.wikipedia.org/")

    elif "play nadaniya" in command:
        speak("Playing Nadaniya for you!", speed=1.2)
        webbrowser.open("https://youtu.be/gPpQNzQP6gE?si=ua0GlW_WS3i6epXk")

    elif "play my fav" in command:
        speak("Playing Nasamajh according to your wish!", speed=1.0)
        webbrowser.open("https://youtu.be/Xukxjs9VYiI?si=iG8DITzcd5VTZMPN")
    
    elif "play rudra" in command:
        speak("Playing Rudra's fav according to your wish!", speed=1.0)
        webbrowser.open("https://youtu.be/eKe1xry7yZA?si=j8lGhING9fTbOhdL")

    elif "thanks" in command:
        speak("Glad I could help!", speed=1.3)

    else:
        speak("I didn't understand that, can you please repeat", speed=1.0)
        # openai_answer = get_openai_response(command)
        # print(openai_answer)

def is_wake_word_detected(command, wake_word="jenny"):
    return wake_word.lower() in command.lower()

# Function to recognize speech and process the command
def recognize_speech_and_process():
    recognizer = sr.Recognizer()
    wake_word = "jenny"
    print("Waiting for wake word...")
    while True:  # Continuously listen for the wake word
        with sr.Microphone() as source:
            try:
                # Listen for audio
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio)
                print(f"Recognized: {command}")
                
                if is_wake_word_detected(command, wake_word):
                    print("Wake word detected!")
                    speak("Hi, I am Jenny. How can I assist you?", speed=1.2)
                    listen_and_process_commands(recognizer)  # Process further commands
                    
            except sr.UnknownValueError:
                print("Listening... (Unrecognized speech)")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

def listen_and_process_commands(recognizer):
    with sr.Microphone() as source:
        print("Listening for a command...")
        try:
            # Listen for a command
            audio = recognizer.listen(source, timeout=10)
            command = recognizer.recognize_google(audio)
            print(f"Command recognized: {command}")
            process_command(command)  # Process the recognized command
            
        except sr.UnknownValueError:
            print("I didn't understand that command!")
            speak("I didn't catch that. Could you repeat?", speed=1.2)
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("I'm having trouble connecting. Please try again later.", speed=1.2)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    # speak("Yeah?", speed=1.0)  # Set an initial speed
    while True:
        recognize_speech_and_process()

if __name__ == "__main__":
    main()