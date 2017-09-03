import tweepy #twitter API
from secrets import * #get keys from secrets.py

#OAuth authentication
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

#api.update_status("GEE WHIZ I CAN TWEET NOW")

#find a tweet with a swear word
#for now, the swear word is hard coded just to test things out
search_results = api.search("hell", "en", "en", 1)

for tweet in search_results:
    if '@' not in tweet.text:
        print(tweet.text)
