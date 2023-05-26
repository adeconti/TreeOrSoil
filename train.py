import tensorflow as tf
from keras import layers


def train_model(x_train, y_train, save_model_path):
    # Define the CNN model
    model = tf.keras.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(50, 50, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid'),
        layers.Dense(2,activation='sigmoid')
    ])


    optimizer = tf.keras.optimizers.Adam(learning_rate=0.002)

    # Compile the model
    model.compile(optimizer= optimizer,
                  loss=tf.keras.losses.BinaryCrossentropy(),
                  metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, epochs=12, batch_size=32)

    # Save the trained model to a file
    model.save(save_model_path)
