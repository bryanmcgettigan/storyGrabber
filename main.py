from dotenv import load_dotenv
from scraper.app import authenticate,grabStory
from kittenTTS.app import generateAudio
import os
import random
import sounddevice as sd

def load_env():
    load_dotenv()
    global CLIENT_ID, SECRET_ID , PASSWORD,  REDDIT_USERNAME
    PASSWORD = os.getenv('PASSWORD')
    CLIENT_ID = os.getenv('CLIENT_ID')
    SECRET_ID = os.getenv('SECRET_ID')
    REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')

def main():
    load_env()#Load environmental values

    postNumber = random.randint(1, 10) #pick a random number between 1-10 of the top posts of the last week

    headers = authenticate(CLIENT_ID,SECRET_ID,PASSWORD,REDDIT_USERNAME)
    subreddit="TwoSentenceHorror" #Reads out a two sentence horror story from reddit
    story = grabStory(headers,postNumber,subreddit)

    
    audio = generateAudio(story)

    sd.play(audio, samplerate=24500)
    sd.wait()


if __name__ == '__main__':
    main()