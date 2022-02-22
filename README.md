# Food Compliment Bot:

## Description:

This project is a side project using pretrained classification models from TensorFlow, and it is mainly something I work on when I am procrastinating on homework and other obligations.

It works by...

## Motivation:

With a lot of my friends creating social media accounts to document the cool food that they are eating, I thought it would be a good idea to create a bot that can recognize food items and provide generated compliments, while also learning a bit about neural networks and the Twitter API.

## Phases:

There are four phases to this project:

0. Get a Twitter API account and create a bot
1. Figure out how to crop the food in the image from the rest of the image "noise"
2. Implement the pretrained Tensorflow model to classify the type of food
3. Create a recurrent neural network to generate compliments to post
4. Use the Twitter API to post compliments and the generated classification

## The Code:

[The model](https://tfhub.dev/google/aiy/vision/classifier/food_V1/1) itself takes 3-channel RGB color images 224x224 pixels scaled to `[0, 1]` as input.

### Phase 0:

The first step is to create a Twitter Bot to grab images off of posts to classify. I used [this tutorial](https://realpython.com/twitter-bot-python-tweepy/).

### Phase 1:

The first step includes image detection and possible cropping of the images so that it fits the 224x224 pixel standard size accepted by the classifier model. The goal is to isolate the food part of the image such that the classifier can run on the image of the food itself instead of other features that are present in the picture, such as people, utensils, etc.

Even though there was a [dataset of food images](https://github.com/WuXinyang2012/openimages-food-subset) that I could use to train my own image detection model to detect the food part of the image so that I could crop it out for the classifier, I decided, for the sake of simplicity, to use the [Open Images V4 pret-trained object detection model](https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1) available on TensorFlow Hub. This image detection model was trained on the subset of food images along with other categories of images, so I expected the performance to be acceptable for the food images that I will be dealing with.

### Phase 2:



### Phase 3:



### Phase 4:



## Results:


## Necessary Implementations:

- Pulling an image off of Twitter when @ed
- Detection when it comes to a picture of a person with food.


## Future Directions:

- Train my own model for image detection and image classification

## Sources:

- Google TensorFlow Hub Food Classifier - https://tfhub.dev/google/aiy/vision/classifier/food_V1/1
- TensorFlow Transfer Learning Tutorial - https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub#an_imagenet_classifier
- Building a Twitter Bot Guide - https://realpython.com/twitter-bot-python-tweepy/
- Tweepy Docs - https://docs.tweepy.org/en/stable/
- Test Image Source - https://www.delightedcooking.com/what-causes-food-likes-and-dislikes.html