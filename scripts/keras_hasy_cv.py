#!/usr/bin/env python

"""
Trains a simple convnet on the HASY dataset.

Gets to 77.77% test accuracy after 1 epoch.
790 seconds per epoch on a GeForce 940MX GPU.

DOES NOT WORK RIGHT NOW!
"""

from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility
import os
import hasy_tools as ht

import tensorflow as tf

from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers.advanced_activations import PReLU
from keras.optimizers import Adam
from keras import backend as K

batch_size = 128
nb_epoch = 1

# input image dimensions
img_rows, img_cols = 32, 32

accuracies = []
for fold in range(1, 11):
    tf.reset_default_graph()
    print("#" * 80)
    print("k = %i" % fold)

    # Load data
    dataset_path = os.path.join(os.path.expanduser("~"), 'hasy')
    hasy_data = ht.load_data(fold=fold,
                             normalize=True,
                             one_hot=True,
                             dataset_path=dataset_path)
    train_x = hasy_data['train']['X'][:1000]
    train_y = hasy_data['train']['y'][:1000]
    test_x = hasy_data['test']['X']
    test_y = hasy_data['test']['y']

    if K.image_dim_ordering() == 'th':
        train_x = train_x.reshape(train_x.shape[0], 1, img_rows, img_cols)
        test_x = test_x.reshape(test_x.shape[0], 1, img_rows, img_cols)
        input_shape = (1, img_rows, img_cols)
    else:
        train_x = train_x.reshape(train_x.shape[0], img_rows, img_cols, 1)
        test_x = test_x.reshape(test_x.shape[0], img_rows, img_cols, 1)
        input_shape = (img_rows, img_cols, 1)

    # Define model
    model = Sequential()
    model.add(Convolution2D(32, 3, 3,
                            border_mode='same',
                            input_shape=input_shape))
    model.add(PReLU())
    model.add(Convolution2D(64, 3, 3, border_mode='same'))
    model.add(PReLU())
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(1024, activation='tanh'))
    model.add(Dropout(0.5))
    model.add(Dense(hasy_data['n_classes'], activation='softmax'))

    # Train model
    adam = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
    model.compile(loss='categorical_crossentropy',
                  optimizer=adam,
                  metrics=['accuracy'])

    model.fit(train_x, train_y, batch_size=batch_size, nb_epoch=nb_epoch,
              verbose=1, validation_data=(test_x, test_y))

    # Serialize model
    model.save('keras-model-fold-%i.h5' % fold)

    # Evaluate model
    score = model.evaluate(test_x, test_y, verbose=0)
    print('Test accuarcy: %0.4f%%' % (score[1] * 100))

accuracies = np.array(accuracies)
print(("CV Accuracy. mean={mean:0.2f}%\t ({min:0.2f}% - {max:0.2f}%)"
       ).format(mean=accuracies.mean() * 100,
                min=accuracies.min() * 100,
                max=accuracies.max() * 100))
