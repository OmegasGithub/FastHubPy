from pydub import AudioSegment
from pydub.playback import play
import io
import requests



# ______   ______     ______     ______      __  __     __  __     ______    
#/\  ___\ /\  __ \   /\  ___\   /\__  _\    /\ \_\ \   /\ \/\ \   /\  == \   
#\ \  __\ \ \  __ \  \ \___  \  \/_/\ \/    \ \  __ \  \ \ \_\ \  \ \  __<   
# \ \_\    \ \_\ \_\  \/\_____\    \ \_\     \ \_\ \_\  \ \_____\  \ \_____\ 
#  \/_/     \/_/\/_/   \/_____/     \/_/      \/_/\/_/   \/_____/   \/_____/ 
 
# This is a python module for interacting with FastHub.net's TTS service.                                                                            

AvailableVoiceTypes = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'f1', 'f2', 'f3', 'f4', 'regular', 'croak', 'whisper']



def TTS(Text  = "Welcome to Fast Hub. \n Record, Translate and Speak. \n I would like to order a Pizza.", voiceType = 0, amplitude = 100, pitch =  50, speed = 125):
    """
    Raw TTS Function - Do not use.
    AvailableVoiceTypes = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'f1', 'f2', 'f3', 'f4', 'regular', 'croak', 'whisper']
    """
    if amplitude > 200:
        amplitude = 200
    if amplitude < 0:
        amplitude = 0   
    if pitch > 99:
        pitch = 99
    if pitch < 0:
        pitch = 0  
    if speed > 450:
        speed = 450
    if speed < 80:
        speed = 80
    
    payload = {
        "text": Text,
        "lang": "en-us+en+en-US",
        "langTrans": "en-us+en+en-US",
        "voiceType": AvailableVoiceTypes[voiceType%len(AvailableVoiceTypes)],
        "amplitude": amplitude,
        "pitch": pitch,
        "speed": speed,
        "repeat": "0"
    }

    response = requests.post("https://fasthub.net/plauder", data=payload)
    url = "https://fasthub.net/speak/" + response.text.split('#')[0] + ".mp3"
    response = requests.get(url)
    return response



def PlayTTS(Text  = "Welcome to Fast Hub. \n Record, Translate and Speak. \n I would like to order a Pizza.", voiceType = 0, amplitude = 100, pitch =  50, speed = 125):
    """
    Plays Text To Speech Out Loud With Given Params 
    AvailableVoiceTypes = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'f1', 'f2', 'f3', 'f4', 'regular', 'croak', 'whisper']
    """

    response = TTS(Text, voiceType, amplitude, pitch, speed)
    audio_data = AudioSegment.from_file(io.BytesIO(response.content), format="mp3")
    play(audio_data)

def TTStoMP3(Text  = "Welcome to Fast Hub. \n Record, Translate and Speak. \n I would like to order a Pizza.", voiceType = 0, amplitude = 100, pitch =  50, speed = 125 , filename = "output"):
    """
    Saves Text To Speech To Specified Filename With Given Params 
    AvailableVoiceTypes = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'f1', 'f2', 'f3', 'f4', 'regular', 'croak', 'whisper']
    """

    response = TTS(Text, voiceType, amplitude, pitch, speed)
    with open( filename + ".mp3", "wb") as file:
        file.write(response.content)
