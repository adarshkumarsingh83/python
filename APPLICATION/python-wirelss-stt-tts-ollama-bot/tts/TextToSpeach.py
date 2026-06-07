import pyttsx3  

class TextToSpeach:
    
    def __init__(self):
        self.engine = pyttsx3.init()  # This function initializes the text-to-speech engine

    # Convert Ollama's response to speech
    def speak_text(self, text):
        self.engine.say(text)  # The say() method takes the string passed as an argument (in this case, text) and adds it to the speech queue.
        self.engine.runAndWait()  # Tells the engine to start processing the queued text and actually speak it out loud.

