import auth.oauth as oauth
import pandas as pd


# function to extract data from tweet object
def extract_tweet_attributes(tweet_object):
    # create empty list
    tweet_list = []
    print(type(tweet_list))
    # loop through tweet objects
    for tweet in tweet_object:
        tweet_id = tweet.id  # unique integer identifier for tweet
        text = tweet.text  # utf-8 text of tweet
        created_at = tweet.created_at  # utc time tweet created
        source = tweet.source  # utility used to post tweet
        reply_to_status = tweet.in_reply_to_status_id  # if reply int of original tweet id
        reply_to_user = tweet.in_reply_to_screen_name  # if reply original tweets screen name
        retweets = tweet.retweet_count # number of times this tweet retweeted
        favorites = tweet.favorite_count # number of time this tweet liked
        # append attributes to list
        tweet_list.append({'tweet_id':tweet_id,
                          'text':text,
                          'created_at':created_at,
                          'source':source,
                          'reply_to_status':reply_to_status,
                          'reply_to_user':reply_to_user,
                          'retweets':retweets,
                          'favorites':favorites})
    # create dataframe
    df = pd.DataFrame(tweet_list, columns=['tweet_id',
                                           'text',
                                           'created_at',
                                           'source',
                                           'reply_to_status',
                                           'reply_to_user',
                                           'retweets',
                                           'favorites'])
    return df


# Create API object
api = oauth.connect_to_twitter_OAuth()

# tweets from my stream
# tweets = api.home_timeline()
tweets = api.user_timeline('realdonaldtrump')
# for tweet in tweets:
#    print(tweet.text)

df = extract_tweet_attributes(tweets)
print(df.describe())
print(df.head())
print(df.shape)