import tensorflow as tf
from keras import layers
import optuna
from preparing_image import load_images_from_directory
from preprocess_data import preprocess

directory_path = input("Escreva o diretório contendo o conjunto de dados de treinamento: ")

def main():

    # Load images and labels using the load_images_from_directory function
    images, labels = load_images_from_directory(directory_path)

    # Preprocess the images and labels using the preprocess function
    x_train, x_test, y_train, y_test = preprocess(images, labels)

    return  x_train, x_test, y_train, y_test
    
x_train, x_test, y_train, y_test = main()

def objective(trial):
    # Define the hyperparameters to tune
    learning_rate = trial.suggest_loguniform('learning_rate', 1e-5, 1e-2)
    num_filters = trial.suggest_int('num_filters', 16, 128)
    dropout_rate = trial.suggest_uniform('dropout_rate', 0.0, 0.5)

    # Define the CNN model with hyperparameters
    model = tf.keras.Sequential([
        layers.Conv2D(num_filters, (3, 3), activation='relu', input_shape=(50, 50, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(num_filters, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(num_filters, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(num_filters, activation='relu'),
        layers.Dropout(dropout_rate),
        layers.Dense(1, activation='sigmoid'),
        layers.Dense(2,activation='sigmoid')
    ])

    # Compile the model with a specific learning rate
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer,
                  loss=tf.keras.losses.BinaryCrossentropy(),
                  metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=0)

    # Evaluate the model
    loss, accuracy = model.evaluate(x_test, y_test)

    return accuracy


def optimize_hyperparameters():
    study = optuna.create_study(direction='maximize')
    study.optimize(objective, n_trials=100)

    # Get the best hyperparameters and accuracy
    best_params = study.best_params
    best_accuracy = study.best_value

    print(f"Best Hyperparameters: {best_params}")
    print(f"Best Accuracy: {best_accuracy}")

optimize_hyperparameters()
