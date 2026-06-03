import json
import pyaudio # Handles audio input/output.
from vosk import Model, KaldiRecognizer
import logging
import time

logger = logging.getLogger(__name__)

class SpeachToText:

    # Listen to microphone input and transcribe using Vosk
    def listen_and_transcribe(self, model: Model, timeout=30, max_retries=3):
        """
        Listen to microphone input and transcribe using Vosk.
        
        Args:
            model: Vosk model instance
            timeout: Timeout in seconds for listening (default: 30 seconds)
            max_retries: Maximum number of retries on audio errors (default: 3)
        
        Returns:
            Transcribed text from audio input
        """
        rec = KaldiRecognizer(model, 16000)  # Vosk model and a sample rate of 16000 Hz
        audio = pyaudio.PyAudio() # Initializes the PyAudio instance for handling audio input/output.
        stream = None
        retry_count = 0
        
        try:
            stream = audio.open(
                format=pyaudio.paInt16, # Opens an audio input stream
                channels=1, # Indicates mono audio (single channel).
                rate=16000, #The sample rate
                input=True, #Specifies that this stream is for audio input.
                frames_per_buffer=4096 # Smaller buffer to reduce overflow issues with Bluetooth
                )

            print("Listening... Speak now.")
            start_time = time.time()
            
            while True:
                # Check for timeout
                if time.time() - start_time > timeout:
                    logger.warning("Listening timeout reached")
                    print("Listening timeout. Please try again.")
                    return ""
                
                try:
                    # Add small timeout to allow stream to be responsive
                    if stream.is_active():
                        data = stream.read(4096, exception_on_overflow=False)  # Reads audio data without raising on overflow
                        
                        if rec.AcceptWaveform(data):   #Processes the audio chunk
                            result = rec.Result()  #Retrieves the transcription result as a JSON string.
                            text = json.loads(result).get('text', '')  # Converts the JSON string into a Python dictionary
                            if text:
                                logger.info(f"Transcribed: {text}")
                                return text
                    else:
                        logger.error("Audio stream is not active")
                        raise Exception("Audio stream is not active")
                        
                except IOError as e:
                    # Handle Bluetooth device disconnection or buffer issues
                    retry_count += 1
                    logger.warning(f"Audio input error (attempt {retry_count}/{max_retries}): {e}")
                    
                    if retry_count >= max_retries:
                        logger.error(f"Failed to read audio after {max_retries} attempts")
                        raise Exception(f"Audio input failed: {e}")
                    
                    # Wait a moment before retrying
                    time.sleep(0.5)
                    continue
                    
        except Exception as e:
            logger.error(f"Error in listen_and_transcribe: {e}")
            print(f"Error in listen_and_transcribe: {e}")
            raise
            
        finally:
            # Safely close the stream
            try:
                if stream is not None:
                    if stream.is_active():
                        stream.stop_stream()
                    stream.close()
                    logger.info("Audio stream closed successfully")
            except Exception as e:
                logger.warning(f"Error closing stream: {e}")
            
            try:
                audio.terminate()
                logger.info("PyAudio terminated successfully")
            except Exception as e:
                logger.warning(f"Error terminating PyAudio: {e}")
