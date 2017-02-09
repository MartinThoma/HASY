#!/usr/bin/env python

"""
Trains a simple convnet on the HASY dataset.

Gets to 76.16% test accuracy after 1 epoch.
586 seconds per epoch on a GeForce 940MX GPU.
"""

import os
import hasy_tools as ht

import tflearn
from tflearn.layers.core import input_data, fully_connected, dropout, reshape
from tflearn.layers.core import flatten
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression

batch_size = 128
nb_epoch = 1

# input image dimensions
img_rows, img_cols = 32, 32

# Load data
fold = 1
dataset_path = os.path.join(os.path.expanduser("~"), 'hasy')
hasy_data = ht.load_data(fold=fold,
                         normalize=True,
                         one_hot=True,
                         dataset_path=dataset_path)
train_x = hasy_data['train']['X']
train_y = hasy_data['train']['y']
test_x = hasy_data['test']['X']
test_y = hasy_data['test']['y']

# Define model
network = input_data(shape=[None, img_rows * img_cols], name='input')
network = reshape(network, (-1, img_rows, img_cols, 1))
network = conv_2d(network, 32, 3, activation='prelu')
network = conv_2d(network, 64, 3, activation='prelu')
network = max_pool_2d(network, 2)
network = dropout(network, keep_prob=0.25)
network = flatten(network, name='Flatten')
network = fully_connected(network, 1024, activation='tanh')
network = dropout(network, keep_prob=0.5)
network = fully_connected(network, 369, activation='softmax')

# Train model
network = regression(network, optimizer='adam', learning_rate=0.001,
                     loss='categorical_crossentropy', name='target')
model = tflearn.DNN(network, tensorboard_verbose=0)
model.fit({'input': train_x}, {'target': train_y}, n_epoch=nb_epoch,
          validation_set=({'input': test_x}, {'target': test_y}),
          snapshot_step=100, show_metric=True, run_id='convnet_mnist',
          batch_size=batch_size)
