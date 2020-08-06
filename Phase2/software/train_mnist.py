import numpy as np
import matplotlib.pyplot as plt
from lib.load_mnist import load_mnist
import keras
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


x_train, x_test, y_train, y_test = load_mnist('mnist_data/')

#x_trian = x_train.reshape((-1,28*28))
#x_test = x_test.reshape((-1,28*28))


model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[28,28]))
model.add(keras.layers.Dense(300, activation = 'relu'))
model.add(keras.layers.Dense(100, activation='relu'))
model.add(keras.layers.Dense(len(class_names), activation='softmax'))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics =['accuracy'])


history = model.fit(x_train, y_train, epochs=4, validation_data=(x_val, y_val))
