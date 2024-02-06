import speech_recognition as sr
from typing import Union

def transcribe_audio(audio_file_path: str) -> str:
    """
    Transcribes speech from an audio file to text using the Google Web Speech API.

    Functionality:
    - Loads an audio file using the SpeechRecognition library.
    - Uses the Google Web Speech API to transcribe the speech in the audio file to text.
    - Handles exceptions for unintelligible speech or API request errors.
    
    Input:
    - audio_file_path: A string representing the file system path to the audio file that needs to be transcribed.
      The audio file should be in a format supported by the SpeechRecognition library (WAV, AIFF, AIFF-C, or FLAC).
    
    Output:
    - A string containing the transcribed text from the audio file. If the speech is unintelligible or an API error occurs,
      the function returns an empty string.
    """

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # Record the audio data from the file

    # Try to recognize the speech in the audio
    try:
        # Transcribe the audio to text using the Google Web Speech API (no API key required for basic usage)
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        # Speech was unintelligible
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        # API request failed
        print(f"Could not request results from Google Speech Recognition service; {e}")

    return ""  # Return an empty string if transcription fails

# Example usage
if __name__ == "__main__":
    audio_file = "path_to_your_audio_file.wav"  # Replace this with the actual path to your audio file
    text = transcribe_audio(audio_file)
    print(f"Transcribed Text: {text}")
