"""
the 'brain' of the bot
"""
import tweepy #twitter API
from secrets import * #get keys from secrets.py

#OAuth authentication
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

#api.update_status("GEE WHIZ I CAN TWEET NOW")

#find a tweet with a swear word
#for now, the swear word is hard coded just to test things out #FIXME
search_results = api.search("hell", "en", "en", 1)

"""
goes through a list of tweets and finds one that isn't a mention
it's a lonely tweet because it doesn't mention anyone or have media
this is so that i don't bother anyone while i'm testing the bot
@param search_results: a list of Search Results objects
@return tweet: the original tweet with swear words that will be changed later
""" #FIXME be able to tweet with mentions and links
def find_lonely_tweet(search_results):
    for tweet in search_results: #go through search_results...
        if '@' and 'https' not in tweet.text: #...and find a tweet that isn't a mention
            return tweet

"""
censors tweet with a silly swear word using censor()
@param tweet: a Search Result; the tweet to be changed
@return tweet: a freshly censored tweet (the same tweet as before)
""" #FIXME do this with regex ? ? ?
def change_tweet(tweet):
    tweet.text = censor(tweet.text)
    return tweet

"""
takes in a string with swear words, censors & capitalizes it
@param orig: string to be censored
@return new: censored string in all caps bc bot likes to scream
"""
#FIXME censorship erases punctuation e.g. hell!!!! -> HECK
def censor(orig):
    orig_words = orig.lower().split() #list of words in original string
    new_words = ["" for x in range(len(orig_words))] #words that will comprise new string

    for _ in range(len(orig_words)):
        if "hell" in orig_words[_]:
            new_words[_] = "heck" #replace hell with heck
        else:
            new_words[_] = orig_words[_] #otherwise don't change the word
        new_words[_] = new_words[_].upper() #capitalize word

    new = " ".join(new_words) #create new string
    return new

orig_tweet = find_lonely_tweet(search_results)
new_tweet = change_tweet(orig_tweet)
print(new_tweet.text)

#api.update_status(new_tweet.text.upper())
