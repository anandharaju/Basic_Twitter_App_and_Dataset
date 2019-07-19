import tweepy

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = '157737769-jbJOYQOkKls8Ee7cN7mwfy2F5LObdkcdQ6GYQmrQ'
ACCESS_SECRET = 'aeApp4inU9w7t6eLgFo13sILBAsb9zffkFZZdCeFzmqir'
CONSUMER_KEY = '1jnaeJN7lsuC0QS2pjOvoHTqO'
CONSUMER_SECRET = 'IxEY0RXKwzsWkCnMOnRXIeF9ScJR4135qct7vNRt9vFvXgA6ig'


# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api


