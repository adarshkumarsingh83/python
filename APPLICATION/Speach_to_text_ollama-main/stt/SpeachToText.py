import json
import pyaudio # Handles audio input/output.
from vosk import Model, KaldiRecognizer

class SpeachToText:

    # Listen to microphone input and transcribe using Vosk
    def listen_and_transcribe(self, model: Model):
        rec = KaldiRecognizer(model, 16000)  # Vosk model and a sample rate of 16000 Hz
        audio = pyaudio.PyAudio() # Initializes the PyAudio instance for handling audio input/output.
        stream = None
        
        try:
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
                    text = json.loads(result).get('text', '')  # Converts the JSON string into a Python dictionary
                    if text:
                        return text
        except Exception as e:
            print(f"Error in listen_and_transcribe: {e}")
            raise
        finally:
            if stream is not None:
                stream.stop_stream()
                stream.close()
            audio.terminate()
