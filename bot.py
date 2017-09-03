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

"""
goes through a list of tweets and finds one that isn't a mention
it's a lonely tweet because it doesn't mention anyone
this is so that i don't bother anyone while i'm testing the bot
@return tweet: the original tweet with swear words that will be changed later
"""
def find_lonely_tweet(search_results):
    #go through search_results...
    for tweet in search_results:
        if '@' not in tweet.text:
            #...and find a tweet that isn't a mention
            return tweet


orig_tweet = find_lonely_tweet(search_results)
print(orig_tweet.text)
