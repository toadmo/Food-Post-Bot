import tensorflow.compat.v2 as tf
import tensorflow_hub as hub
import pandas as pd
import matplotlib.pyplot as plt
import tweepy
import os
import wget

################### Initializing Models ###################

# Link to the detector model
detectorLink = "https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1"

# Link to the classifier model
classifierLink = "https://tfhub.dev/google/aiy/vision/classifier/food_V1/1"

# Loading the detector and classifiers
detector = hub.load(detectorLink)
classifier = hub.load(classifierLink)

# Input information for the classifier
height = 224
width = 224
channels = 3

# Loading the labelmap (maps the outputs of the classifier to actual names of food)
labelmap = pd.read_csv('aiy_food_V1_labelmap.csv')

print("Models initialized")

################### Twitter API Setup ###################

# Reading secrets from extenal file
with open("secrets.txt", "r") as f:
    CONSUMER_KEY = f.readline().strip()
    CONSUMER_SECRET = f.readline().strip()
    ACCESS_TOKEN = f.readline().strip()
    ACCESS_TOKEN_SECRET = f.readline().strip()

# Setting up authentication handler and access token
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Printing out results of authentication
try:
    api.verify_credentials()
    print("Twitter authentication complete")
except:
    print("Error during Twitter authentication")


################### Twitter Liking Mentions and Posting Comment Functions ###################

# def convertImage(url):
#     wget.download(url, 'image.png')
#     tfImage = tf.image.convert_image_dtype('image.png')
#     return tfImage

# Confirm image to tensor usable by the pretrained models
def convertImageTest(image):
    tfImage = tf.image.convert_image_dtype(image)
    return tfImage

# Run detection model on the image to find food/box where food is
def detectFood(convertedImage): 
    foodImages = []
    detectResults = detector(convertedImage)
    # Use a for loop so that if there are multiple foods in the picture
    for entity, score, box in zip(detectResults['detection_class_entities'], detectResults['detection_scores'], detectResults['detection_boxes']):
        if entity == 'Food' and score > 0.25:
            foodImages.append((entity, score, box))
    return foodImages

# Crop the image based on the box from the detection model and resize to 224x224
def cropImage(image, data):
    box_indices = tf.zeros(shape=len(data))
    cropped = tf.image.crop_and_resize(image, data[1], box_indices, [224,224])
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    display = cropped.eval(session=sess)

    plt.imshow(display[0])
    plt.imshow(display[1])

# Run previous functions together to get cropped image of isolated food
converted = convertImageTest('image.png')
foodList = detectFood(converted)
cropImage(converted, foodList)


##### HERE ####

    # api.create_tweet(in_reply_to_tweet_id=tweet, text=f"Nice .........")


################### OFFLINE API TEST ###################




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