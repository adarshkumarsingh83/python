#!/usr/bin/env python3
"""
Free, offline speech examples in Python.

  TTS (text-to-speech): pyttsx3   -> no internet, no API key
  STT (speech-to-text): Vosk      -> no internet, no API key

------------------------------------------------------------------
Install:
    pip install pyttsx3 vosk sounddevice

    # Linux only: pyttsx3 needs espeak, and sounddevice needs PortAudio
    sudo apt install espeak libportaudio2

Download a Vosk model (small English ~50 MB) and unzip it next to this file:
    https://alphacephei.com/vosk/models
    e.g. vosk-model-small-en-us-0.15
------------------------------------------------------------------

Usage:
    python speech_examples.py tts          # speak a sentence
    python speech_examples.py stt          # listen and transcribe live
    python speech_examples.py echo         # repeat back what you say (say "exit"/"stop" to quit)
"""

import sys
import logging
from config.ApplicationConfig import ApplicationConfig
from service.McpService import McpService
import logging
import asyncio
import json
import json  # Duplicate import preserved from screenshot
import ollama
import sys
from config import AppConfig
from service import SearchService

OLLAMA_MODEL = "llama3.2"
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app_config = AppConfig()
search_service = SearchService(app_config)
appConfig = ApplicationConfig()
mcpService = McpService(appConfig)
# ---------------------------------------------------------------------------
# TEXT-TO-SPEECH  (pyttsx3)
# ---------------------------------------------------------------------------
def text_to_speech(text="Hello, this is offline text to speech in Python."):
    import pyttsx3

    engine = pyttsx3.init()
    engine.setProperty("rate", 175)     # words per minute
    engine.setProperty("volume", 1.0)   # 0.0 to 1.0

    # Optional: pick a different installed voice
    # voices = engine.getProperty("voices")
    # engine.setProperty("voice", voices[1].id)

    engine.say(text)
    engine.runAndWait()

    # To save to a file instead of speaking aloud:
    # engine.save_to_file(text, "output.wav")
    # engine.runAndWait()


# ---------------------------------------------------------------------------
# SPEECH-TO-TEXT  (Vosk, live from the microphone)
# ---------------------------------------------------------------------------
def speech_to_text(model_path="./model/vosk-model-en-us-0.22"):
    import json
    import queue

    import sounddevice as sd
    from vosk import KaldiRecognizer, Model

    try:
        model = Model(model_path)
    except Exception:
        sys.exit(
            f"Could not load Vosk model at '{model_path}'.\n"
            "Download one from https://alphacephei.com/vosk/models and unzip it here."
        )

    samplerate = 16000
    recognizer = KaldiRecognizer(model, samplerate)
    audio_q = queue.Queue()

    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        audio_q.put(bytes(indata))

    print("Listening... speak into the mic. Press Ctrl+C to stop.")
    with sd.RawInputStream(samplerate=samplerate, blocksize=8000,
                           dtype="int16", channels=1, callback=callback):
        try:
            while True:
                data = audio_q.get()
                if recognizer.AcceptWaveform(data):
                    # A full phrase was recognized
                    result = json.loads(recognizer.Result())
                    if result.get("text"):
                        print("You said:", result["text"])
                else:
                    # Words recognized so far in the current phrase
                    partial = json.loads(recognizer.PartialResult())
                    if partial.get("partial"):
                        print("...", partial["partial"], end="\r")
        except KeyboardInterrupt:
            print("\nStopped.")


# ---------------------------------------------------------------------------
# ECHO  (listen on the mic, then speak back whatever you said)
# ---------------------------------------------------------------------------
def echo(model_path="./model/vosk-model-en-us-0.22"):
    import json
    import queue
    import shutil
    import subprocess
    import time

    import sounddevice as sd
    from vosk import KaldiRecognizer, Model
    tools_details_list = asyncio.run(tool_list(mcpService))

    try:
        model = Model(model_path)
    except Exception:
        sys.exit(
            f"Could not load Vosk model at '{model_path}'.\n"
            "Download one from https://alphacephei.com/vosk/models and unzip it here."
        )

    # TTS: prefer the macOS `say` command (reliable for repeated calls);
    # fall back to pyttsx3 on other platforms. pyttsx3 reused across many
    # runAndWait() calls goes silent after the first utterance on macOS.
    mac_say = shutil.which("say")
    engine = None
    if not mac_say:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("rate", 175)
        engine.setProperty("volume", 1.0)

    def speak(text):
        if mac_say:
            subprocess.run([mac_say, text])
        else:
            engine.say(text)
            engine.runAndWait()

    samplerate = 16000
    recognizer = KaldiRecognizer(model, samplerate)
    audio_q = queue.Queue()

    # Phrases that end the session. "good bye" / "goodbye" covers how Vosk
    # may transcribe it as one or two words.
    stop_phrases = ("stop it", "exit now", "good bye", "goodbye")

    # Single filler words Vosk tends to hallucinate from silence/room noise.
    # If a whole phrase is just one of these, ignore it (don't print or echo).
    noise_words = {"the"}

    def callback(indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        audio_q.put(bytes(indata))

    def say(text):
        """Speak text with the mic paused so we don't hear ourselves."""
        stream.stop()
        speak(text)
        with audio_q.mutex:
            audio_q.queue.clear()
        stream.start()

    def clear_line():
        # Erase the current (partial) line so leftover text isn't left behind.
        print("\r\033[K", end="")

    def prompt_speak_now():
        nonlocal recognizer
        print('\nSpeak now... (say "stop it" or "exit now" to quit)')
        say("input command now")
        # Let the speaker echo of "Speak now" decay, then discard whatever the
        # mic picked up during that window. Otherwise Vosk decodes the echo as
        # a stray filler word (e.g. "the") at the start of the next phrase.
        time.sleep(0.4)
        with audio_q.mutex:
            audio_q.queue.clear()
        # Fresh recognizer for each turn so leftover audio isn't carried over.
        recognizer = KaldiRecognizer(model, samplerate)

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000,
                           dtype="int16", channels=1, callback=callback) as stream:
        prompt_speak_now()
        try:
            while True:
                data = audio_q.get()
                if not recognizer.AcceptWaveform(data):
                    # Still mid-phrase; show progress and keep listening.
                    partial = json.loads(recognizer.PartialResult())
                    if partial.get("partial"):
                        clear_line()
                        print("...", partial["partial"], end="\r")
                    continue

                # A full phrase was recognized.
                text = json.loads(recognizer.Result()).get("text", "").strip()
                if not text:
                    continue

                # Strip a leading filler word Vosk invents from silence/noise
                # (e.g. "the"). Only the first word is removed.
                words = text.split()
                if words and words[0] in noise_words:
                    text = " ".join(words[1:])
                if not text:
                    continue

                clear_line()
                print("You said:", text)

                # Stop if the phrase contains an exit command.
                if any(phrase in text for phrase in stop_phrases):
                    logger.info("Stopping.")
                    say("Goodbye")
                    break
                # Process the recognized text with the available tools.
                # todo anythigns related to mcp and local model call 
                results = search_service.search(text)
                logger.info("Search results for query %r: %s", text, results)

                # ChromaDB returns `documents` as a list-of-lists (one inner
                # list per query). We sent a single query, so unwrap the first
                # inner list to get the matched document strings.
                docs = results[0] if results else []
                answer = docs[0] if docs else "Sorry, I couldn't find anything relevant."

                logger.info("Search results:")
                for i, doc in enumerate(docs, start=1):
                    logger.info(f"{i}. {doc}")

                if answer == "Sorry, I couldn't find anything relevant.":
                    answer = text
               
                # Send to Ollama with tools available
                try:
                    response = ollama.chat(
                        model=OLLAMA_MODEL,
                        messages=[{"role": "user", "content": answer+" "+text}],
                        tools=tools_details_list,  # <- AI now knows these tools exist!
                        stream=False,
                    )

                except Exception as e:
                    print(f"❌ ERROR calling Ollama: {e}")
                    print(f"\nMake sure:")
                    print(f"  1. Ollama is running (ollama serve)")
                    print(f"  2. Model is installed (ollama pull {OLLAMA_MODEL})")
                    sys.exit(1)

                # Check: Did AI want to use tools?
                if not response.get("message", {}).get("tool_calls"):
                    print("🤖 AI answered directly (no tools needed):")
                    print(response["message"]["content"])
                    return

                # Process tool calls
                messages = [
                    {"role": "user", "content": answer},
                    response["message"],
                ]

                for tool_call in response["message"]["tool_calls"]:
                        tool_name = tool_call["function"]["name"]
                        try:
                            args = tool_call["function"]["arguments"]

                            # Parse if arguments are JSON string
                            if isinstance(args, str):
                                args = json.loads(args)

                            # Find the server name from tool_details_list
                            server_name = None
                            for tool in tools_details_list:
                                if tool.get("function", {}).get("name") == tool_name:
                                    server_name = tool.get("function", {}).get("serverName")
                                    break

                            if not server_name:
                                raise ValueError(f"Tool '{tool_name}' not found in available tools")

                            print(f"🔧 Tool requested: {tool_name}")
                            print(f"📝 Arguments: {args}")

                            # Execute the tool
                            tool_result = asyncio.run(mcpService.call_tool(server_name, tool_name, args))
                            print(f"✅ Tool result: {tool_result}\n")
                        except Exception as exc:
                            logger.error(f"Tool '{tool_name}' failed: {exc}")
                            print(f"⚠️ Tool '{tool_name}' failed: {exc}\n")
                            tool_result = {"error": f"Tool '{tool_name}' failed: {exc}"}

                        # Add tool response to conversation
                        messages.append({
                            "role": "tool",
                            "content": (
                                json.dumps(tool_result)
                                if isinstance(tool_result, dict)
                                else str(tool_result)
                            ),
                        })

                # Send tool results back to AI for final answer
                final = ollama.chat(
                    model=OLLAMA_MODEL,
                    messages=messages,
                )

                print("🤖 Final AI response:")
                print(final["message"]["content"])


                # Speak the matched document back, then ask for the next phrase.
                say(final["message"]["content"])
                prompt_speak_now()
        except KeyboardInterrupt:
            logger.info("\nStopped.")

# ---------------------------------------------------------------------------

async def tool_list(mcpService):
    tools_details_list = await mcpService.get_tool_details()
    for tool in tools_details_list:
        logging.info(
            "ServerName: %s | ServerURL: %s | ServerTransport: %s | Tool: %s | Description: %s | Parameters: %s",
            tool.get("function", {}).get("serverName"),
            tool.get("function", {}).get("url"),
            tool.get("function", {}).get("transport"),
            tool.get("function", {}).get("name"),
            tool.get("function", {}).get("description"),
            json.dumps(tool.get("function", {}).get("parameters", {})),
        )
    return tools_details_list

# ---------------------------------------------------------------------------
def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "tts":
        text_to_speech()
    elif mode == "stt":
        speech_to_text()
    elif mode == "echo":
        echo()
    else:
        logger.error("Usage: python speech_examples.py [tts|stt|echo]")


if __name__ == "__main__":
    main()
