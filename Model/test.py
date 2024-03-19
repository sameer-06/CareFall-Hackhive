import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Define paths
image_path = 'lam.jpg'
saved_model_path = 'model.h5'

# Load the saved model
model = load_model(saved_model_path)

# Load and preprocess the test image
img = load_img(image_path, target_size=(150, 150))
img_array = img_to_array(img) / 255.0  # Rescale pixel values to [0, 1]
img_array = tf.expand_dims(img_array, 0)  # Add batch dimension

# Make prediction
prediction = model.predict(img_array)

# Print prediction
if prediction[0][0] > 0.5:
    print("The model predicts that the person is falling.")
else:
    print("The model predicts that the person is not falling.")
