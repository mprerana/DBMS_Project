import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream,Cursor

users=[]

city="Delhi"


access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
print('authed')
api = tweepy.API(auth)
places = api.geo_search(query=city)
place_id = places[0].id
coords=(places[0].bounding_box.coordinates)[0]
location=coords[0]+coords[2]
#Cursor implementation
tweets=Cursor(api.search,q='place:'+place_id).items()
i = 0
for tweet in tweets:
    with open('tweets/location/'+city+'.txt','a+') as f:
        f.write('TWEET_TEXT: '+tweet.text + '\n')

#Stream implementation

'''class StdOutListener(StreamListener):

    def on_data(self, tweet):
        tweet=json.loads(tweet)

        try:

            #print(tweet['place']['name'],tweet['user']['name'])

            if tweet['place']['name'] in [city,'Jharkhand','Ratu']:

                tweet['user']['id']=str(tweet['user']['id'])

                if tweet['user']['id'] not in users:
                    print(tweet['user']['id'])
                    users.append(tweet['user']['id'])
                    with open('users/'+city+'.txt','a+') as f:
                        f.write(tweet['user']['id']+'\n')
                    global user_count
                    user_count+=1

                    if user_count==max_user_count:
                        print(user_count,"users found!")
                        return False

        except KeyError:
            print(tweet)

    def on_error(self, status):
        print("Error:",status)

if user_count<max_user_count:
    print('yes')
    l = StdOutListener()
    stream = Stream(auth, l)
    print('stream')
    stream.filter(locations=location)
    print('ranchi')
'''