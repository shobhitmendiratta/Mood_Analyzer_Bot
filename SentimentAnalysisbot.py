from textblob import TextBlob 
from dataclasses import dataclass 

@dataclass 
class Mood:
  emoji: str 
  sentiment: float 


def get_mood (input_yourtext: str, * , sensitivity: float) -> Mood:

  polarity: float = TextBlob(input_yourtext).sentiment.polarity

  friendly_threshold: float = sensitivity
  hostile_threshold: float = -sensitivity
  if polarity >= friendly_threshold: 
    return Mood('Good mood', polarity)

  elif polarity <= hostile_threshold:
    return Mood('Angry mood', polarity)
  else: 
    return Mood('Sad mood', polarity) 

def running_bot():
  print('Hello! I am a Sentiment analysis bot:')
  while True:
    user_inputtext: str = input('Enter your text to receive sentiment analysis: ')
    mood: Mood = get_mood(user_inputtext, sensitivity= 0.3)
    print(f'Bot: {mood.emoji} ({mood.sentiment})')

if __name__ =='__main__':
  running_bot()