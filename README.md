# Food Compliment Bot:

## Description:

This project is a side project using pretrained classification models from TensorFlow, and it is mainly something I work on when I am procrastinating on homework and other obligations.

## Motivation:

With a lot of my friends creating social media accounts to document the cool food that they are eating, I thought it would be a good idea to create a bot that can recognize food items and provide generated compliments, while also learning a bit about neural networks and the Twitter API.

## Phases:

There are four phases to this project:

1. Figure out how to crop the food in the image from the rest of the image
2. Implement the pretrained Tensorflow model to classify the type of food
3. Create a recurrent neural network to generate compliments to post
4. Use the Twitter API to post compliments and the generated classification

## The Code:

[The model](https://tfhub.dev/google/aiy/vision/classifier/food_V1/1) itself takes 3-channel RGB color images 224x224 pixels scaled to `[0, 1]` as input.

### Phase 1:

The first step includes image detection and possible cropping of the images so that it fits the 224x224 pixel standard size accepted by the classifier model. Even though there was a dataset of food that I could use to 

I decided to use a pretrained model for image detection


### Phase 2:



### Phase 3:



### Phase 4:



## Results:



## Sources:

- Google TensorFlow Hub Food Classifier - https://tfhub.dev/google/aiy/vision/classifier/food_V1/1
- TensorFlow Transfer Learning Tutorial - https://www.tensorflow.org/tutorials/images/transfer_learning_with_hub#an_imagenet_classifier