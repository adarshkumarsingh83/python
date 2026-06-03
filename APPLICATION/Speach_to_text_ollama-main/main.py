from config import AppConfig
from stt import SpeachToText
from tts import TextToSpeach
from ollma import OllamaService
from datetime import datetime
import logging
import time
import getpass 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

appConfig = AppConfig()
ollamaService = OllamaService()
speachToText = SpeachToText()
textToSpeach = TextToSpeach()

def get_time_based_greeting():
    """Return a greeting based on the current time of day with the user's name."""
    current_hour = datetime.now().hour
    username = getpass.getuser()
    
    if 5 <= current_hour < 12:
        greeting = f"Good morning, {username}!"
    elif 12 <= current_hour < 17:
        greeting = f"Good afternoon, {username}!"
    else:
        greeting = f"Good evening, {username}!"

    return greeting

def executeMain():
    try:
        logger.info("Executing main function...")
        model = appConfig.load_vosk_model()
        
        # Greet user based on time of day
        greeting = get_time_based_greeting()
        print(greeting)
        textToSpeach.speak_text(greeting)

        consecutive_errors = 0
        max_consecutive_errors = 3
        
        while True:

            # Listen to user input with error handling
            try:
                user_input = speachToText.listen_and_transcribe(model, timeout=30)
                
                # Reset error counter on successful input
                if user_input:
                    consecutive_errors = 0
                    print(f"You said: {user_input}")

                    # Check for exit commands
                    exit_keywords = ["bye", "stop", "good bye", "i am done"]
                    if any(keyword in user_input.lower() for keyword in exit_keywords):
                        username = getpass.getuser()
                        textToSpeach.speak_text(f"Goodbye, {username}! Have a great time ahead!")
                        logger.info(f"Goodbye! Exiting the application. {username}")
                        time.sleep(2)
                        break

                    # Query Ollama API
                    response = ollamaService.query_ollama(user_input)
                    print(f"Ollama: {response}")

                    # Speak Ollama's response
                    textToSpeach.speak_text(response)
                else:
                    # Empty input, just continue
                    logger.info("No speech detected, continuing...")
                    consecutive_errors = 0
                    
            except Exception as e:
                consecutive_errors += 1
                logger.error(f"Error during speech recognition (attempt {consecutive_errors}/{max_consecutive_errors}): {e}")
                print(f"Error: {e}")
                
                if consecutive_errors >= max_consecutive_errors:
                    logger.error("Too many consecutive errors. Please check your Bluetooth headphone connection and try again.")
                    textToSpeach.speak_text("There seems to be an issue with the audio input. Please check your Bluetooth headphone connection and restart the application.")
                    break
                
                # Wait before retrying
                print("Retrying in 2 seconds...")
                time.sleep(2)

    except KeyboardInterrupt:
        logger.error("\nExiting. Goodbye!")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logger.info("Starting the application...")
    executeMain()
    logger.info("Application has exited.")