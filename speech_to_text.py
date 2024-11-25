"""
File: speech_recognition.py
Author: Yassine El Yacoubi
Description: Contains a function to capture voice input and convert it to text using Google Speech Recognition.
Dependencies: SpeechRecognition

Function:
    - speech_to_text(): Captures audio from the microphone and converts it to text.

Returns:
    - str: Recognized text from the speech or an error message if recognition fails.
"""

import speech_recognition as sr

def speech_to_text():
    """
    Captures audio from the microphone and converts it to text using Google Speech Recognition.

    Returns:
        str: The recognized text from speech, or an error message if recognition fails.
    """
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

    # Convert speech to text
    try:
        command = recognizer.recognize_google(audio)
        return command
    except sr.UnknownValueError:
        return "Sorry, could not understand the audio."
    except sr.RequestError as e:
        return f"Request error: {e}"
