from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    os.system("start output.mp3")  # For Windows
    # os.system("mpg321 output.mp3")  # For Linux

text = ""
text_to_speech(text)
