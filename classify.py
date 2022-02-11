import tensorflow.compat.v2 as tf
import tensorflow_hub as hub
import pandas as pd
import tweepy
import wget

################### Initializing Models ###################

# Link to the detector model:
detectorLink = "https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1"

# Link to the classifier model:
classifierLink = "https://tfhub.dev/google/aiy/vision/classifier/food_V1/1"

# Loading the detector and classifiers
detector = hub.load(detectorLink)
classifier = hub.load(classifierLink)

# Input information for the classifier:
height = 224
width = 224
channels = 3

# Loading the labelmap (maps the outputs of the classifier to actual names of food):
labelmap = pd.read_csv('aiy_food_V1_labelmap.csv')



################### Twitter API Setup ###################

with open("secrets.txt", "r") as f:
    CONSUMER_KEY = f.readline().strip()
    CONSUMER_SECRET = f.readline().strip()
    ACCESS_TOKEN = f.readline().strip()
    ACCESS_TOKEN_SECRET = f.readline().strip()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Printing out results of authentication:
try:
    api.verify_credentials()
    print("Twitter authentication complete")
except:
    print("Error during Twitter authentication")

# Class for stream to view tweets in real time:
class Listener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
    
    def on_status(self, tweet):
        if 'media' in tweet.entities:
            for photo in tweet.entities['media']:
                # Process image with image['media_url']
                continue
    
    def on_error(self, status):
        print("Stream Error")

tagListener = Listener(api)
tagStream = tweepy.Stream(api.auth, tagListener)




################### Twitter Liking Mentions and Posting Comment ###################


timeline = api.mentions_timeline()
for tweet in timeline:
    tweet.favorite()
    # RETWEET CODE INPUT

# Liking a tweet: Client.like(tweet_id, user_auth=True)
# Creating a tweet: Client.create_tweet(in_reply_to_tweet_id=xyz, text=blah)