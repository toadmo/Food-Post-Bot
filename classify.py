import tensorflow.compat.v2 as tf
import tensorflow_hub as hub
import pandas as pd

classifierLink = 'https://tfhub.dev/google/aiy/vision/classifier/food_V1/1'
# detectorLink = 

classifier = hub.load(classifierLink)

height = 224
width = 224
channels = 3
