#!/usr/bin/env python

"""Trains a simple convnet on the HASY dataset."""

import os
import hasy_tools as ht

import tensorflow as tf
import tflearn
from tflearn.layers.core import input_data, fully_connected, dropout, reshape
from tflearn.layers.core import flatten
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from keras.utils import np_utils

epochs = 100000  # 200000

dataset_path = os.path.join(os.path.expanduser("~"), 'hasy')

# Load data
fold = 1
dataset_path = os.path.join(os.path.expanduser("~"), 'hasy')
hasy_data = ht.load_data(fold=fold, normalize=True, dataset_path=dataset_path)
train_x = hasy_data['train']['X']
train_y = hasy_data['train']['y']
test_x = hasy_data['test']['X']
test_y = hasy_data['test']['y']

tf.reset_default_graph()  # Don't influence the other folds

# convert class vectors to binary class matrices
train_y = np_utils.to_categorical(train_y, hasy_data['n_classes'])
test_y = np_utils.to_categorical(test_y, hasy_data['n_classes'])

# Define model
network = input_data(shape=[None, 1024], name='input')
network = reshape(network, (-1, 32, 32, 1))
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
model.fit({'input': train_x}, {'target': train_y}, n_epoch=1,
          validation_set=({'input': test_x}, {'target': test_y}),
          snapshot_step=100, show_metric=True, run_id='convnet_mnist',
          batch_size=128)
