import tensorflow.compat.v2 as tf
import tensorflow_hub as hub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tweepy
import os
import wget
import sys
import time
import logging

################### Initializing Logging ###################

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

################### Initializing Models ###################

# https://www.tensorflow.org/hub/migration_tf2 Since models are TF1

# Link to the classifier model
classifierLink = "https://tfhub.dev/google/aiy/vision/classifier/food_V1/1"

# Loading the detector and classifiers
classifier = hub.load(classifierLink)
classifier = classifier.signatures['default']

# Input information for the classifier
height = 224
width = 224
channels = 3

# Loading the labelmap (maps the outputs of the classifier to actual names of food)
labelmap = pd.read_csv('/content/gdrive/MyDrive/Colab Notebooks/FoodBot/aiy_food_V1_labelmap.csv')

print("Models initialized.")

################### Twitter API Setup ###################

# Authentication with elevated access to get more than just v2 endpoints

# Reading secrets from config file

bearer_token = config.bearer_token
api_key = config.api_key
api_key_secret = config.api_key_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# Authentication data
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Trying authentication
try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")


################### Image Detection, Cropping, and Processing ###################

# Confirm image to tensor usable by the pretrained models
def reshapeImage(image):
    imageData = plt.imread(image)
    tensor = tf.image.convert_image_dtype(imageData, tf.float32)[tf.newaxis, ...]
    box_indices = tf.zeros(shape=(1,), dtype=tf.int32)
    reshaped = tf.image.resize(tensor, [height, width])
    return reshaped


converted = reshapeImage('/content/gdrive/MyDrive/Colab Notebooks/FoodBot/2_food_test.jpg')
minThresh = 0.15
classification = classifier(converted)
mostLikely = np.argmax(classification["default"])
probability = round(np.max(classification["default"])*100,2)
foodClass = str(labelmap[labelmap.id==mostLikely]).split()[-1]

if probability > minThresh:
  print(f"Nice {foodClass}! Looks yummy.\nConfidence: {probability}%.")
else:
  print(f"Model prediction certainty does not exceed minimum threshold.")

postContent = f"Nice {foodClass}! Looks yummy.\nConfidence: {probability}%."

################### Tweepy Functions ###################

user = api.get_user(screen_name='omdaot')
print(user.id)

# Get most recent tweet ID that was replied to
def get_last_tweet(file):
    f = open(file, 'r')
    lastId = int(f.read().strip())
    f.close()
    return lastId

# Write tweet ID of tweet that was most recently replied to
def put_last_tweet(file, Id):
    f = open(file, 'w')
    f.write(str(Id))
    f.close()
    logger.info("Updated the file with the latest tweet Id")
    return

# Respond to tweet
def respondToTweet(file='tweet_ID.txt'):

    # Get last tweet ID
    last_id = get_last_tweet(file)

    # Look through all mentions
    mentions = api.mentions_timeline(last_id, tweet_mode='extended')
    if len(mentions) == 0:
        return

    new_id = 0
    logger.info("someone mentioned me...")

    for mention in reversed(mentions):
        # Log each mention Tweet ID and data
        logger.info(str(mention.id) + '-' + mention.full_text)

        # Update mention ID counter
        new_id = mention.id

        # Reply function
        # Need to get image, run the classifier and 
        try:
            tweet = # UNIMPLEMENTED
            media = api.media_upload("created_image.png") # Get image before uploading it
            logger.info("liking and replying to tweet")

            api.create_favorite(mention.id) # Liking the tweet
            api.update_status('@' + mention.user.screen_name + " Here's your Quote", mention.id, media_ids=[media.media_id]) # Posting the tweet reply
        except:
            logger.info("Already replied to {}".format(mention.id))

    put_last_tweet(file, new_id)

if __name__=="__main__":
    respondToTweet()