f
rom spo2 import *
from heartbeat import *
from onewire_temp import *
import urllib.requestA
import requests
import threading
import json
import random
import serial
import time

import google.generativeai as genai

# Load Gemini AI model
genai.configure(api_key='AIzaSyCOgfZwbgOWApgdoYkD3YDqMLqBVRXZb5w')
gemini_model = genai.GenerativeModel('gemini-2.0-flash')
chat = gemini_model.start_chat(history=[])

import pygame
import time
from gtts import gTTS
from mutagen.mp3 import MP3
import time


def Play(text1):
    print(text1)
    myobj = gTTS(text=text1, lang='en-us', tld='com', slow=False)
    myobj.save("voice.mp3")
    print('\n------------Playing--------------\n')
    song = MP3("voice.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load('voice.mp3')
    pygame.mixer.music.play()
    time.sleep(song.info.length)
    pygame.quit()

import speech_recognition as sr
import sounddevice as sd
import wave
import numpy as np

duration = 5
fs = 44100
channels=2
filename="input_audio.wav"

while True:
    print("Recording...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype=np.int16)
    sd.wait()
    print("Recording complete.")

    # Save the recorded audio to a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(audio_data.tobytes())

    # Perform speech recognition
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language='IN-en')
            print("Recognized text:", text)
            if text == 'emergency':
                Capture()
            elif text == 'what is primary functions of this device':
                Play('health monitoring and emergency alerts')
            else:
                gemini_response = chat.send_message('Title: Women saftey device, query = '+x+' (response should be in one paragraph)')
                data = gemini_response.text
                Play(data)
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        
    hb = HEART_BEAT()
    try:
        bp, spo2 = OBP()
    except:
        bp = 0
        spo2 = 0
    temp_c, temp_f =  read_temp()
    print('Temperature ',temp_c, 'C')
    Emergency()
    api_key = "Y7DSN6SAR9YHIO4U"
    URL='https://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={}&field4={}'.format(api_key,hb,temp_c,bp,spo2)
    data=urllib.request.urlopen(URL)
    print(data)
    time.sleep(1)
    
    
    
