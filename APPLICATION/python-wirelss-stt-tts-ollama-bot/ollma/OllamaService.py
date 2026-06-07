import requests  # pip install requests
import json 

class OllamaService:
    def __init__(self):
        pass

    # Send the transcribed text to Ollama and get a response
    def query_ollama(self, input_text):
        url = "http://localhost:11434/api/generate"  # 
        payload = {"model": "llama3.1", "prompt": input_text}  # The input prompt provided by the user.
        try:
            response = requests.post(url, json=payload, stream=True)  # Stream the response, Enables streaming the response incrementally instead of loading it all at once.
            response.raise_for_status() # Raises an exception 

            full_response = ""    #Accumulates the complete response from the API.
            done = False           #

            # Iterate over the response in chunks
            for line in response.iter_lines(decode_unicode=True):            #It reads the response line by line
                if line:
                    data = json.loads(line) #function takes a JSON-formatted string (the line) and converts it into a Python dictionary
                    full_response += data.get("response", "")
                    if data.get("done", False):   #Checks if the "done" field in the JSON is True, signaling the end of the response.
                        done = True
                        break

            if done:
                return full_response
            else:
                return "Ollama could not generate a valid response."

        except Exception as e:
            return f"Error: {e}"