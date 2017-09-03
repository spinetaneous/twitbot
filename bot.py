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
it's a lonely tweet because it doesn't mention anyone or have media
this is so that i don't bother anyone while i'm testing the bot
@param search_results: a list of Search Results objects
@return tweet: the original tweet with swear words that will be changed later
"""
def find_lonely_tweet(search_results):
    for tweet in search_results: #go through search_results...
        if '@' and 'https' not in tweet.text: #...and find a tweet that isn't a mention
            return tweet

"""
censors tweet with a silly swear word
i know that there are better ways to do this but i just want to see if it works
also it's almost 3AM sue me
jk don't do that i'm a poor college student
@param tweet: a Search Result; the tweet to be changed
@return new_tweet: a freshly censored tweet
""" #FIXME do this with regex ? ? ?
def change_tweet(tweet):
    new_tweet = tweet #create copy of tweet
    words = tweet.text.split() #words in the current original tweet
    new_words = ["" for x in range(len(words))] #the words that will comprise the new tweet
    for _ in range(len(words)):
        if "hell" in words[_]:
            new_words[_] = "h-e-double-hockey-sticks"
        else:
            new_words[_] = words[_]
    new_tweet.text = " ".join(new_words)
    return new_tweet

orig_tweet = find_lonely_tweet(search_results)
new_tweet = change_tweet(orig_tweet)
print(new_tweet.text)

api.update_status(new_tweet.text.upper())
