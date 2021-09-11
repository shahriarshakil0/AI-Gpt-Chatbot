from gtts import gTTS
from playsound import playsound

language = 'en'

# text = input("Enter your text :")
def tts(text):
    tts = gTTS(text,lang=language,slow=False)
    tts.save('./Output/speech.wav')
    playsound('./Output/speech.wav')

    return playsound

# tts('Hi there how can i help you')