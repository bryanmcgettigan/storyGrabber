from kittentts import (
    KittenTTS, 
)


def generateAudio(text):
    m =  KittenTTS(
        model_name="KittenML/kitten-tts-nano-0.1",

    )
    audio = m.generate(text, voice='expr-voice-3-m' )

    return audio

