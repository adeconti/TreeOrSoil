import numpy as np
import tensorflow as tf
from PIL import Image
import os
import csv

images = []
filenames = []

directory_path = input("Informe o diretório que contém as imagens: ")

for filename in os.listdir (directory_path):
    image_path = os.path.join(directory_path, filename)
    image = Image.open(image_path)
    images.append(np.array(image))
    filenames.append(filename)

images_array = np.array(images) ; filenames_array = np.array(filenames)

#Normalize pixel values
images_array = images_array.astype('float32') / 255.0

# Load the trained model
model = tf.keras.models.load_model("model.h5")

# Making predictions
predictions = model.predict(images_array)

# The predictions will be probabilities, we can use a threshold to classify them
threshold = 0.5
predicted_labels = np.where(predictions > threshold, 'solo', 'árvore')

# Save the evaluation results to a CSV file
with open("resultados.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Image', 'Prediction'])
    for i, label in enumerate(predicted_labels):
        writer.writerow([filenames[i], label[0]])

