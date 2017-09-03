import tweepy #twitter API
import re #regex library
from secrets import * #get keys from secrets.py

#OAuth authentication
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

#api.update_status("GEE WHIZ I CAN TWEET NOW")

#find a tweet with a swear word
#for now, the swear word is hard coded just to test things out
search_results = api.search("hell", "en", "en", 1)

#create re object so tweets will exclude @'s
#re_obj = re.compile('[@]')

#prints first tweet
print(search_results[0].text)
