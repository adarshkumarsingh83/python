from config import AppConfig
from ollama import OllamaService
import pyaudio # Handles audio input/output.
from vosk import Model, KaldiRecognizer # speech recognition framework
import requests  # pip install requests
import pyttsx3  # Converts text to speech
import json  # Parses JSON data 

config = AppConfig()
ollama_service = OllamaService()

# Listen to microphone input and transcribe using Vosk
def listen_and_transcribe(model):
    rec = KaldiRecognizer(model, 16000)  # Vosk model and a sample rate of 16000 Hz
    audio = pyaudio.PyAudio() # Initializes the PyAudio instance for handling audio input/output.
    stream = audio.open(
        format=pyaudio.paInt16, # Opens an audio input stream
        channels=1, # Indicates mono audio (single channel).
        rate=16000, #The sample rate
        input=True, #Specifies that this stream is for audio input.
        frames_per_buffer=8192 # Sets the size of the buffer that holds audio data before being processed.
        )
    stream.start_stream()  # Begins the audio stream 

    print("Listening... Speak now.")
    while True:
        data = stream.read(4096) # Reads 4096 bytes of audio data (half of the buffer size)
        if rec.AcceptWaveform(data):   #Processes the audio chunk Returns True if the audio chunk is sufficient
            result = rec.Result()  #Retrieves the transcription result as a JSON string.
            text = eval(result).get('text', '')  # Converts the JSON string into a Python dictionary
            if text:
                return text

# Convert Ollama's response to speech
def speak_text(text):
    engine = pyttsx3.init()  # This function initializes the text-to-speech engine
    engine.say(text) #The say() method takes the string passed as an argument (in this case, text) and adds it to the speech queue.
    engine.runAndWait() #tells the engine to start processing the queued text and actually speak it out loud.

# Main function to integrate all components
def main():
    try:
        # Load Vosk model
        model = config.load_vosk_model()

        while True:
            # Listen to user input
            user_input = listen_and_transcribe(model)
            print(f"You said: {user_input}")

            # Query Ollama API
            response = ollama_service.query_ollama(user_input)
            print(f"Ollama: {response}")

            # Speak Ollama's response
            speak_text(response)

    except KeyboardInterrupt:
        print("\nExiting. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
