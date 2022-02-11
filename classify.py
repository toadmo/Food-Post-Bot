import tensorflow.compat.v2 as tf
import tensorflow_hub as hub
import pandas as pd
import tweepy

################### Initializing Models ###################

# Link to the detector model:
detectorLink = "https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1"

# Link to the classifier model:
classifierLink = 'https://tfhub.dev/google/aiy/vision/classifier/food_V1/1"

# Loading the detector and classifiers
detector = hub.load(detectorLink)
classifier = hub.load(classifierLink)

# Input information for the classifier:
height = 224
width = 224
channels = 3

# Loading the labelmap (maps the outputs of the classifier to actual names of food):
labelmap = pd.read_csv('aiy_food_V1_labelmap.csv')






################### Pulling Picture From Twitter API ###################
with open("secrets.txt", "r") as f:
    CONSUMER_KEY = f.readline().strip()
    CONSUMER_SECRET = f.readline().strip()
    ACCESS_TOKEN = f.readline().strip()
    ACCESS_TOKEN_SECRET = f.readline().strip()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Liking a tweet: Client.like(tweet_id, user_auth=True)
# Creating a tweet: Client.create_tweet(in_reply_to_tweet_id=xyz, text=blah)