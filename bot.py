import tweepy
import time

# Autentication variable

# PUT YOUR API KEY AND API SECRET KEY HERE
# auth = tweepy.OAuthHandler('','')

#PUT YOUR ACESS TOKEN AND SECRET TOKEN HERE
# auth.set_access_token('','')

# API variable
# 'wait_on_rate_limit' is a method that mesure the limits of retweets

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# This part is optional: tReceive informations from the account on Twitter
# user = api.me()

# This part is optional: Print the data of the account
# print(user)

search0 = 'Ciência' 
#search0 = 'Science'
search1 = 'Tecnologia'
#search1 = 'Tecnology'

# There is a maximum for this value, don't make it too big
max_Tweets = 1

while 1
    for tweet in tweepy.Cursor(api.search, search0).items(max_Tweets)
        try
            print('SCIENCE, ITS WORKING!')
            tweet.retweet()
            tweet.favorite()
            time.sleep(60)
        except tweepy.TweepError as e
            print(e.reason)
        except StopIteration
            break
        
    for tweet in tweepy.Cursor(api.search, search1).items(max_Tweets)
        try
            print('TECNOLOGY, ITS WORKING!')
            tweet.retweet()
            tweet.favorite()
            time.sleep(60)
        except tweepy.TweepError as e
            print(e.reason)
        except StopIteration
            break