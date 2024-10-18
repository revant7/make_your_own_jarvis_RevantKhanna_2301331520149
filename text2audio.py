from gtts import gTTS
from playsound import playsound
import os

def text_to_audio(text, lang='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang, slow=False)
    
    # Save the audio to a file
    audio_file = "output.mp3"
    tts.save(audio_file)
    print(f"Audio saved as {audio_file}")



    playsound(audio_file)


