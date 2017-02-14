from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API

from tweepy.streaming import StreamListener

import messageHandler
import keys

threads = []

def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


class StdOutListener( StreamListener ):

    def __init__(self):
        super().__init__()
        self.tweetCount = 0

    def on_connect( self ):
        print("Connection established!!")

    def on_disconnect( self, notice ):
        print("Connection lost!! : ", notice)

    def on_data( self, status ):
        # print("Entered on_data()")
        print(status)
        if '"screen_name":"'+keys.twitter_username+'"' in status:
            text = find_between(status,'text":"', '"')
            print("Text: " + text, flush = True)
            messageHandler.handlemessage(text)

        #print(status, flush = True)
        return True

    def on_direct_message( self, status ):
        print("Entered on_direct_message()")
        try:
            print(status, flush = True)
            return True
        except BaseException as e:
            print("Failed on_direct_message()", str(e))

    def on_error( self, status ):
        print(status)


def main():

    try:
        auth = OAuthHandler(keys.consumer_key, keys.consumer_secret)
        auth.secure = True
        auth.set_access_token(keys.access_token, keys.access_token_secret)

        api = API(auth)

        # If the authentication was successful, you should
        # see the name of the account print out
        print(api.me().name)

        stream = Stream(auth, StdOutListener())

        stream.userstream()

    except BaseException as e:
        print("Error in main()", e)

if __name__ == '__main__':
    main()


