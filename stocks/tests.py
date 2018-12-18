from django.test import TestCase
from django.utils import timezone
from stocks.models import Tweet
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from time import sleep
import time

# Create your tests here.
class TestTweets(TestCase):
    def test_getFromDatabase(self):
        t=Tweet(tweet_text='Test data', pub_date=timezone.now())
        t.save()
        tweets = Tweet.objects.all()
        self.assertGreater(len(tweets), 0, "Can't get any tweets from database")

class TestTwitterConnection(TestCase):
    def test_getInstance(self):
        from stocks.views import StdOutListener
        consumer_key = "XXdVWTaTgOkR0AHaE1SOG1fWa"
        consumer_secret = "MH7ZWKMoiSjnw0kZweLpKzTlSXjpVE27aZfuJsI8twC3Jm7VOH"
        access_token = "28985708-GTz8sReJqi039EaadKljnbxQYu6gPk4n810bCjFDa"
        access_token_secret = "J4cOQ4KZwOtyN9LUIBz2h69F56fGnWWyNV3OXLaRt0MuS"
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l, tweet_mode='extended')
        stream.filter(track=['asels','gerel','bist'], is_async=True)
        time.sleep(5)
        stream.disconnect()
        tweets= Tweet.objects.all()
        print(tweets)
        self.assertIsNotNone(len(tweets), "Can't get a Tweets")

    