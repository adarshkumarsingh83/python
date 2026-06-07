# Speach_to_text_ollama
---
* brew install portaudio
* pip install -r requirements.txt
* ollama run llama3.1
	* https://ollama.com/library/llama3.1

```
adarshkumar@adarshs-MacBook-Pro-16-new ~ % ollama run llama3.1
pulling manifest 
pulling 667b0c1932bc: 100% ▕██████████████████▏ 4.9 GB                         
pulling 948af2743fc7: 100% ▕██████████████████▏ 1.5 KB                         
pulling 0ba8f0e314b4: 100% ▕██████████████████▏  12 KB                         
pulling 56bb8bd477a5: 100% ▕██████████████████▏   96 B                         
pulling 455f34728c9b: 100% ▕██████████████████▏  487 B                         
verifying sha256 digest 
writing manifest 
success 
>>> Send a message (/? for help)

```
* to stop ollma 
	* /bye


```
https://alphacephei.com/vosk/

go to model left hand side -> select the langaude model 

https://alphacephei.com/vosk/models

add the downlladed model in model dir in code 

brew install portaudio

python3 -m pip install pyaudio

/usr/local/bin/python3 -m pip install vosk requests pyttsx3 pyaudio

ollama run llama3.1

pip install -r requirements.txt

```