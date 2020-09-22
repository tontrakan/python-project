import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
#import important library
def speak(text):
    tts = gTTS(text=text, lang='en') # execute text with lang do you need
    filename = 'voice.mp3' # to save files type for playsound
    tts.save(filename) # to save files name
    playsound.playsound(filename) # execute the sound that you need to play following text data input

speak("test play sound")  # function to play sound 
