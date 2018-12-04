from django.http import HttpResponse

# Import modules
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import dataset
from sqlalchemy.exc import ProgrammingError
import asyncio
from threading import Thread
from stocks.models import Tweet


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import dataset
from sqlalchemy.exc import ProgrammingError
import asyncio
from threading import Thread

from multiprocessing import Process
from time import sleep
from django.utils import timezone




# Your credentials go here
consumer_key = "a"
consumer_secret = "b"
access_token = "c"
access_token_secret = "d"

"""
The code for our listener class above goes here!
"""
class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self, status):
        print(status.text)
        t = Tweet(tweet_text=status.text, pub_date=timezone.now())
        t.save()
        print(Tweet.objects.all())
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False


def nested():
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l, tweet_mode='extended')
   
    stream.filter(track=['gerel', 'asels','bist'], is_async=True)
    
   




def index(request): 
    nested()

    return HttpResponse("Hello, world. Yow You're at the polls index.")



