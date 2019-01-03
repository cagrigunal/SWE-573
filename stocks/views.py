from django.http import HttpResponse
from django.template import loader
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
import requests
import json

      



# Your credentials go here
consumer_key = "xxx"
consumer_secret = "xxx"
access_token = "xxx"
access_token_secret = "xxx"

"""
The code for our listener class above goes here!
"""
class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self, status):
        text = ''
        # Try for extended text of an original tweet, if RT'd (REST API)
        try: text = status.retweeted_status['full_text']
        except:
            # Try for extended text of an original tweet (streamer)
            try: text = status.extended_tweet['full_text']
            except:
                # Try for extended text of an original tweet (REST API)
                try: text = status.full_text
                except:
                    # Try for basic text of original tweet if RT'd 
                    try: text = status.retweeted_status['text']
                    except:
                        # Try for basic text of an original tweet
                        try: text = status.text
                        except: 
                            # Nothing left to check for
                            text = ''
        
        
        if(status.lang!='de'):
            #print(status.lang)
            
            t = Tweet(tweet_text=status.text, pub_date=timezone.now())
            t.save()
            print(t.tweet_text)
            
       
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False


def nested():
    #response = json.loads(requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=OMBGDV75LSVPD38K").text)
    #print(response)
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l, tweet_mode='extended')
   
    stream.filter(track=['asels','gerel','bist','avod','isctr','pkart'], is_async=True)
    
   
def posTweet(tweets,date,stock):
    tweetList=[]
    for tweet in tweets:
        if(stock!=''):
            low=stock.lower()
        else:
            low=stock
        if(date!=''):
            dateN=date
        else:
            dateN=timezone.now().strftime("%Y-%m-%d")
        if tweet.pub_date.strftime("%Y-%m-%d")==dateN:
            print(tweet.pub_date.strftime("%Y-%m-%d"))
            OKlist = (stock,low,'günler','güzel','hayrola','yükşeliş','paragirişi','PARAGİRİŞİ','+','yukari','alacagim','kazan','kazanir','harika','iyi','yeşil','yemyeşil','YEŞİL','İYİ')
            if any(s in tweet.tweet_text for s in OKlist):
                    #print(tweet.tweet_text)
                tweetList.append(tweet)
    return tweetList



def index(request): 
    nested()
    tweets=Tweet.objects.all()
    
    posTweets=posTweet(tweets,'','')
    hourly=[]
    for tweet in posTweets:
        hourly.append(tweet.pub_date.strftime("%H"))
    tweetData = {x:hourly.count(x) for x in hourly}
    
    tweetDataFinal=[]
    
        
    for key in tweetData:
        print(key)
        data = [int(key), tweetData[key]]
       
        tweetDataFinal.append(data)
       
    


    
    
    
        
        #print(print(tweet.tweet_text.split()))
    template = loader.get_template("stocks/index.html")
    context = {
        'tweets' :posTweets,
        'tweetData' : tweetDataFinal
    }
    
    return HttpResponse(template.render(context, request))


def indexQuery(request):
    date=request.POST.get('date')
    print(date) 
    stock =request.POST.get('stock')
    print(stock) 
    nested()
    tweets=Tweet.objects.all()
    
    posTweets=posTweet(tweets,date,stock)
    hourly=[]
    for tweet in posTweets:
        hourly.append(tweet.pub_date.strftime("%H"))
    tweetData = {x:hourly.count(x) for x in hourly}
    
    tweetDataFinal=[]
    
        
    for key in tweetData:
        print(key)
        data = [int(key), tweetData[key]]
       
        tweetDataFinal.append(data)
       
    


    
    
    
        
        #print(print(tweet.tweet_text.split()))
    template = loader.get_template("stocks/index.html")
    context = {
        'tweets' :posTweets,
        'tweetData' : tweetDataFinal
    }
    
    return HttpResponse(template.render(context, request))

    



