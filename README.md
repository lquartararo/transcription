## transcription
uses your microphone to look for specific words **in real time** and runs a function as the word is detected.

## setup
1. Make sure you have [Python 3 installed](https://www.python.org/downloads/)
2. Clone this repo using `git clone https://github.com/lquartararo/transcription.git` OR [just download](https://github.com/lquartararo/transcription/archive/refs/heads/main.zip) and unzip
3. Run `pip install -r requirements.txt` in the install location
4. Run the program with `python main.py`
5. *Optional*: configure **wordlist.txt**. Put each word/phrase on a separate line

## technical details for nerds
This is how it generally works:
1. we use [python-sounddevice](https://github.com/spatialaudio/python-sounddevice) in order to get real-time audio from the user's microphone
2. then we pipe the data over to [vosk](https://github.com/alphacep/vosk-api) in order to do ASR and transcribe the audio
3. as the audio is transcribed, the script checks the wordlist for matches in its wordlist
4. if there is a match, a function is run
