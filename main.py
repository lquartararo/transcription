import json
import sys
import sounddevice as sd
from vosk import Model, KaldiRecognizer

# defines what to do when a target word is recognized
# TODO: implement some sort of punishment
def reaction():
    print("POTTY MOUTH DETECTED!!!")

def load_wordlist(filepath):
    with open(filepath, 'r') as f:
        # Read each non-empty line from the file
        return [line.strip() for line in f if line.strip()]

# load target words from an external file
target_words = load_wordlist("wordlist.txt")

# set model
model = Model("vosk-model-small-en-us-0.15")

# set sample rate to 16000 Hz (do not change!)
rec = KaldiRecognizer(model, 16000)

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    # convert CFFI buffer to bytes before passing to Vosk
    if rec.AcceptWaveform(bytes(indata)):
        result = json.loads(rec.Result())
        recognized_text = result.get("text", "")
        print("Final:", recognized_text)
        # check for any target word in the recognized text
        detected = [word for word in recognized_text.split() if word in target_words]
        if detected:
            reaction()
            
    else:
        partial_result = json.loads(rec.PartialResult())
        print("Partial:", partial_result.get("partial", ""))

# open an input stream with SoundDevice for real time audio streaming
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print("Listening...")
    try:
        # run until crtl + c is pressed
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopped.")