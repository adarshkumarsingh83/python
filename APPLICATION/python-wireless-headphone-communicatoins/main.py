import speech_recognition as sr
import subprocess

# Initialize recognizer
recognizer = sr.Recognizer()

# OPTIONAL: Uncomment to find the exact ID of your Bluetooth Mic
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with name \"{name}\" found at index {index}")

# Replace this with the numeric index from the list above, or leave as None
# to use the system default input device.
BLUETOOTH_MIC_INDEX = None

try:
    with sr.Microphone(device_index=BLUETOOTH_MIC_INDEX) as source:
        print("Calibrating background noise... please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)

        while True:
            print("Speak now! Say 'stop' to exit.")
            audio = recognizer.listen(source, timeout=10)

            try:
                # Using Google's Web Speech API for transcription
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")

                normalized_text = text.strip().lower()
                if normalized_text in {"stop", "exit", "quit"}:
                    print("Stop command received. Exiting.")
                    subprocess.run(["say", "Goodbye."])
                    break

                # Speak the recognized text back through the default audio output device
                print("Speaking back through headphones...")
                subprocess.run(["say", text])

            except sr.UnknownValueError:
                print("Google Web Speech API could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except OSError as e:
                print(f"Could not access microphone: {e}")
            except Exception as e:
                print(f"Unexpected error during recognition: {e}")

except KeyboardInterrupt:
    print("Interrupted by user.")
except OSError as e:
    print(f"Could not access microphone: {e}")