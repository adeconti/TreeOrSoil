import numpy as np
from PIL import Image
import os

def load_images_from_directory(directory_path):
    images = []
    labels = []

    for filename in os.listdir(directory_path):
        image_path = os.path.join(directory_path, filename)
        label = os.path.splitext(filename)[0].split("_")[1]
        image = Image.open(image_path)
        images.append(np.array(image))
        labels.append(label)

    return np.array(images), np.array(labels)
