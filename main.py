from preparing_image import load_images_from_directory
from preprocess_data import preprocess
from train import train_model
from evaluate import evaluate_model

def main():
    # Call the functions from other files here
    directory_path = input("Escreva o diretório do conjunto de imagens: ")

    # Load images and labels using the load_images_from_directory function
    images, labels = load_images_from_directory(directory_path)

    # Preprocess the images and labels using the preprocess function
    x_train, x_test, y_train, y_test = preprocess(images, labels)

    #train the model
    train_model( x_train, y_train, "model.h5" )

    #evaluate_model
    evaluate_model( x_test, y_test, "model.h5", "results.csv" )

if __name__ == '__main__':
    main()
