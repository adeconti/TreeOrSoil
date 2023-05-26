from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

def preprocess(images, labels):

    # Normalize pixel values to a range of 0 to 1
    images = images.astype('float32') / 255.0

    # Perform label encoding
    label_encoder = LabelEncoder()
    encoded_labels = label_encoder.fit_transform(labels)

    # Convert labels to one-hot encoded vectors
    one_hot_labels = to_categorical(encoded_labels)

    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(images, one_hot_labels, test_size=0.3, random_state=80)

    return x_train, x_test, y_train, y_test