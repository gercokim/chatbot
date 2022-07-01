import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os

print(sr.Microphone.list_microphone_names())

# Creating chatbot class
class ChatBot():
    def __init__(self, name):
        print("------ booting up ------")
        self.name = name.upper()

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("my speech ---> ", self.text) 
        except:
            print("my speech ---> ERROR")
    
    def text_to_speech(self, text):
        print(self.name + " ---> ", text)
        speech = gTTS(text=text, lang='en')
        speech.save("speech.mp3")
        os.system("afplay speech.mp3")
        os.remove("speech.mp3")
        
    def start(self, text):
        return True if self.name in text.upper() else False
    
    
    
# Execution
if __name__ == "__main__":
    chatbot = ChatBot("Sam")
    while True:
        chatbot.speech_to_text()
        print(chatbot.name, chatbot.start(chatbot.text))
        # Starting up the bot
        if chatbot.start(chatbot.text) is True:
            tts = "Hello, I am " + chatbot.name + " the AI, how can I assist you?"
            chatbot.text_to_speech(tts)