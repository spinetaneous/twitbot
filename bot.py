"""
the 'brain' of the bot
"""
import tweepy #twitter API
import re #regex
import random #used to choose swears & their replacements
from secrets import * #get keys from secrets.py
import cuss #the dictionary of cuss words

#OAuth authentication
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

def find_tweet():
    #FIXME isn't actually listening/streaming
    #FIXME tweet with mentions & links/don't use "lonely" tweets? maybe
    """
    finds a tweet to censor
    """
    tweet = None #we don't have a tweet yet
    #choose a random cuss word to censor
    swear = random.choice(list(cuss.words))
    print(swear) #FIXME DEL L8R
    #find a suitable tweet with that word
    search_results = api.search(swear, lang="en", rpp=100)
    return find_lonely_tweet(search_results)

def find_lonely_tweet(search_results):
    """
    goes through a list of tweets and finds one that isn't a mention
    it's a lonely tweet because it doesn't mention anyone or have media
    this is so that i don't bother anyone while i'm testing the bot
    @param search_results: a list of Search Results objects
    @return tweet: the original tweet with swear words that will be changed later
    """
    for tweet in search_results: #go through search_results...
        if "@" not in tweet.text and "https" not in tweet.text and "RT" not in tweet.text: #...and find a tweet that isn't a mention
            return tweet
            #FIXME what to do if can't find tweet?

def change_tweet(tweet):
    #FIXME do this with regex ? ? ?
    """
    censors tweet with a silly swear word using censor()
    @param tweet: a Search Result; the tweet to be changed
    @return tweet: a freshly censored tweet (the same tweet as before)
    """
    tweet.text = censor(tweet.text)
    return tweet

def censor(orig):
    #FIXME add variety
    """
    takes in a string with swear words, censors & capitalizes it
    @param orig: string to be censored
    @return new: censored string in all caps bc bot likes to scream
    """
    #for every key in cuss words
    for key in cuss.words.keys():
        #check original string for words to replace
        #FIXME only uses first entry in list; should be random later
        #new = re.sub(key, random.choice(cuss.words[key]), orig, flags=re.IGNORECASE)
        new = re.sub(key, cuss.words[key][0], orig, flags=re.IGNORECASE) #compatible with test suite
        orig = new #reassign orig
        #print(key, cuss.words[key][0], new)
    return new.upper()

#FIXME printing stuff here just 4 development reasonz
try:
    orig_tweet = find_tweet()
    print(orig_tweet.text)
    new_tweet = change_tweet(orig_tweet)
    print(new_tweet.text)

    #api.update_status(new_tweet.text)
except AttributeError:
    print("couldn't find a tweet")
