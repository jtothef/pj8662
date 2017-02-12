import tweepy
import keys

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status
#api.update_status('Test3!')

def sendmessage(message):
    api.send_direct_message(screen_name="", text=message)
