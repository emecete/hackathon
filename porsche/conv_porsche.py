
from keras import Sequential
from keras.layers import Conv2D, Dropout, Flatten, Dense
from PIL import Image
import numpy as np
import pandas as pd
from keras.layers import MaxPooling2D, BatchNormalization
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def read_data():
    x = []
    filenames_and_labels = pd.read_csv('dataset.csv', delimiter=";")
    filenames = filenames_and_labels['archivo']
    y = filenames_and_labels['valor'].tolist()
    for filename in filenames:
        x.append(np.array(Image.open('dataset_imagenes_instagram/' + filename)))
    return x, y

def data_augmentation():
    images, labels = read_data()
    for i in range(0, len(images)):
        # Basic Data Augmentation - Horizontal Flipping
        flip_img = np.fliplr(images[i])
        images.append(flip_img)
        labels.append(labels[i])
    return images, labels  # augmented

def main():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(612, 612, 3)))
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

    optimizer = Adam(lr=0.001)
    a = model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    x, y = data_augmentation()
    x = np.array(x)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=10)

    model.fit(x_train, y_train, batch_size=50, epochs=20, verbose=1)

    loss, acc = model.evaluate(x_test, y_test, verbose=0)
    print(acc * 100)

main()