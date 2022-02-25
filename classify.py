import tensorflow.compat.v2 as tf
import tensorflow_hub as hub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tweepy
import os
import wget
import config

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

# Reading secrets from config file

bearer_token = config.bearer_token
api_key = config.api_key
api_key_secret = config.api_key_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# Setting up authentication handler and access token
client = tweepy.Client(bearer_token=bearer_token,
                        access_token=access_token,
                        access_token_secret=access_token_secret,
                        consumer_key=api_key,
                        consumer_secret=api_key_secret)


################### Image Detection, Cropping, and Processing ###################

# Confirm image to tensor usable by the pretrained models
def reshapeImage(image):
    imageData = plt.imread(image)
    tensor = tf.image.convert_image_dtype(imageData, tf.float32)[tf.newaxis, ...]
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



##### HERE ####

    # api.create_tweet(in_reply_to_tweet_id=tweet, text=f"Nice .........")



################### Listener Declaration and Creation ###################


# # Class for stream to view tweets in real time
# class Listener(tweepy.StreamListener):
#     def __init__(self, api):
#         self.api = api
#         self.me = api.me()
    
#     def on_status(self, tweet):
#         api.like(tweet)
#         if 'media' in tweet.entities:
#             finalImages = []
#             for photo in tweet.entities['media']:
#                 # print(photo['media_url'])
#                 converted = convertImage(photo['media_url'])
#                 imageMetaData = detectFood(converted)
#                 if len(imageMetaData) > 0:
#                     for data in imageMetaData:
                        


#     def on_error(self, status):
#         print("Stream Error")
#         return False

# # Declaring listener object and stream
# tagListener = Listener(api)
# tagStream = tweepy.Stream(api.auth, tagListener)

# tagStream.filter(track=['@FoodComplimentBot'])