#!/usr/bin/env python3

# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
from playsound import playsound


def speak(mytext, language='en'):
    '''
    Speaks a text input

            Parameters:
                    mytext (str): the text to be spoken
                    languadge (str): the languadge of the text

            Returns:
                    None
    '''
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("song.mp3")

    playsound("song.mp3")

def sing(name, age):
    '''
    sings Happy Birthday

            Parameters:
                    name (str): the text to be spoken
                    age (int): how many repetitions of "hip hip hooray"

            Returns:
                    None
    '''
    speak('happy birthday to you')
    speak('happy birthday to you')
    speak(f'happy birthday to {name}')
    speak('happy birthday to you')

    for i in range(age):
        speak('hip hip hooray')
    speak('and one for luck')
    speak('hip hip hooray')


sing('Dave', 42)

