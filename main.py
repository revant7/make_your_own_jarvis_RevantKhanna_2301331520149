import speech_recognition as sr


recognizer = sr.Recognizer()


with sr.Microphone() as source:
    print("Please say something:")

    audio_data = recognizer.listen(source)
    print("Recognizing...")

    try:
        text = recognizer.recognize_google(audio_data)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")


