import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream,Cursor

access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
print('authed')
api = tweepy.API(auth)
#places = api.geo_search(query=city)
#place_id = places[0].id
#coords=(places[0].bounding_box.coordinates)[0]
#location=coords[0]+coords[2]


#Cursor implementation
hashtag = '#humnibhayenge'
tweets=Cursor(api.search,q=hashtag,lang = 'en').items()
i = 0
for tweet in tweets:
#    print(i)
    i+=1
    with open('tweets/'+hashtag+'.txt','a+') as f:
        f.write('TWEET_TEXT: '+tweet.text + '\n')


#Stream implementation
