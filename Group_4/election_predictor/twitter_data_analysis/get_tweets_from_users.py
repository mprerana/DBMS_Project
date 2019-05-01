import json,os
import tweepy
from tweepy import Cursor
from time import sleep

access_token = ""     
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

city="Ranchi"

no_tweet_list=[]

while(True):
    #Cursor implementation

    users=[]

    with open('users/'+city+'.txt') as f:
        users=f.readlines()
        for i in range(len(users)):
            users[i]=users[i].strip('\n')

    done_list=[]

    try:
        for folder,subfolder,files in os.walk('tweets/'+city):
            for file in files:
                done_list.append(file[:-4])
    except FileNotFoundError:
        pass

    done_list.extend(no_tweet_list)

    users=list(set(users)-set(done_list))
    print("City:",city)
    print("No. of users remaining:",len(users))
    if len(users)==0:
        break

    for user_id in users:

        tweets=Cursor(api.user_timeline,user_id=int(user_id)).items()
        last_user_id=user_id
        tweet_count=0

        try:
            print("User id:",user_id)
            for tweet in tweets:

                tweet_count+=1
                print("No. of tweets written:",tweet_count,end='\r')
                try:
                    f=open('tweets/'+city+'/'+user_id+'.txt','a+',encoding='utf-8')
                except FileNotFoundError:
                    os.mkdir('tweets/'+city)
                    f=open('tweets/'+city+'/'+user_id+'.txt','a+',encoding='utf-8')
                f.write('tweet:'+tweet.text+'\n')
                f.close()

            if tweet_count==0:
                no_tweet_list.append(user_id)

        except tweepy.error.TweepError as e:
            try:
                os.remove('tweets/'+city+'/'+last_user_id+'.txt')
            except FileNotFoundError:
                pass
            tweet_count=0
            print(e)
            if e.reason=='Twitter error response: status code = 401':
                no_tweet_list.append(user_id)
            else:
                sleep(15)

        print("No. of tweets written:",tweet_count)
