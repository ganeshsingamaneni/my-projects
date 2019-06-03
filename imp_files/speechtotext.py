import speech_recognition as sr
import os
r  = sr.Recognizer()
dirname, filename = os.path.split(os.path.abspath(__file__))
print(dirname,filename)
with sr.Microphone() as source:
    print("tell me")
    audio = r.listen(source)
    print("done") 
    print("Text: ",r.recognize_google(audio))  
