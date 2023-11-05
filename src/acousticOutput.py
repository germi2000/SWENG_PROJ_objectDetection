from gtts import gTTS
import os

class TextToSpeech:
    def __init__(self, text, lang='de'):
        self.text = text
        self.lang = lang

    def generate_and_play_audio(self):
        tts = gTTS(self.text, lang=self.lang)
        tts.save("output.mp3")
        os.system("start output.mp3")


# acoustic call
#tts_converter = TextToSpeech("hallo")
#tts_converter.generate_and_play_audio()


