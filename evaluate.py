import numpy as np
import tensorflow as tf
import csv

def evaluate_model(x_test, y_test, load_model_path, save_results_path):
    # Load the trained model
    model = tf.keras.models.load_model(load_model_path)

    # Making predictions on test images
    predictions = model.predict(x_test)
    print(predictions)

    # The predictions will be probabilities, we can use a threshold to classify them
    threshold = 0.5
    predicted_labels = np.where(predictions > threshold, 'tree', 'soil')
    
    #Calculate Loss and Accuracy
    test_loss, test_accuracy = model.evaluate(x_test, y_test)
    print(f'Loss: {test_loss} Accuracy: {test_accuracy}')

    # Save the evaluation results to a CSV file
    with open(save_results_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Image', 'Prediction'])
        for i, label in enumerate(predicted_labels):
            writer.writerow([i+1, label[0]])
