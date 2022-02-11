import tensorflow.compat.v2 as tf
import tensorflow_hub as hub
import pandas as pd

classifierLink = 'https://tfhub.dev/google/aiy/vision/classifier/food_V1/1'
detectorLink = "https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1"

detector = hub.load(detectorLink)
classifier = hub.load(classifierLink)

height = 224
width = 224
channels = 3
