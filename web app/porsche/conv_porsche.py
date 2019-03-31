
from keras import Sequential, optimizers
from keras.layers import Conv2D, Dropout, Flatten, Dense
from PIL import Image
import numpy as np
import pandas as pd
from keras.layers import MaxPooling2D, BatchNormalization
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

IMG_SIZE = 612


def read_data(images_folder_path, labels_file_path):
    x = []
    filenames_and_labels = pd.read_csv(labels_file_path, delimiter=";")
    filenames = filenames_and_labels['archivo']
    y = filenames_and_labels['valor'].tolist()
    for filename in filenames:
        x.append(np.array(Image.open(images_folder_path + '/' + filename)))
    return x, y


def data_augmentation(images, labels):
    for i in range(0, len(images)):
        # Basic Data Augmentation - Horizontal Flipping
        flip_img = np.fliplr(images[i])
        images.append(flip_img)
        labels.append(labels[i])
    return images, labels  # augmented


def train(x, y):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Conv2D(96, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    # model.add(Dropout(0.3))
    model.add(Dense(1, activation='softmax'))

    model.summary()

    optimizer = optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0)
    a = model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    print(a)

    x = np.array(x)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=10)

    model.fit(x_train, y_train, batch_size=10, epochs=2, verbose=1)

    loss, acc = model.evaluate(x_test, y_test, verbose=0)
    print(acc * 100)

    return model, {"test_acc": acc}


def classify(model, img):
    """
    Make class prediction depending on a model for an image
    :param model: Keras model
    :param img: an RGB image (already resized) to be classified (numpy array)
    :return: predicted class (1-> Porsche, 0->Not-Porsche) (STRING)
    """
    output = model.predict(img, batch_size=128)
    if output == 1:
        return "Porsche"
    else:
        return "Not-Porsche"
