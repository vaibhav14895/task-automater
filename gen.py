import google.generativeai as genai

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Please say something...")
    audio_data = recognizer.listen(source)
    print("Recording finished!")

try:
    print("Converting audio to text...")
    if(audio_data):
        text = recognizer.recognize_google(audio_data)
        print("Text:", text)
    else:
        print("please say something for output")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")


genai.configure(api_key='AIzaSyCDLsMw3KstNyHb93Qx7xWy_MgUHn43ogA')

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(text+"convert it into json fromate of task date and time")
print(response.text)

