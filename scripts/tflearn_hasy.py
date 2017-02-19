#!/usr/bin/env python

"""
Trains a simple convnet on the HASY dataset.

Gets to 76.78% test accuracy after 1 epoch.
573 seconds per epoch on a GeForce 940MX GPU.
"""

import os

import tensorflow as tf
tf.set_random_seed(0)  # make sure results are reproducible
import tflearn
from tflearn.layers.core import input_data, fully_connected, dropout
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression

import hasy_tools as ht

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
                         dataset_path=dataset_path,
                         flatten=False)
train_x = hasy_data['train']['X']
train_y = hasy_data['train']['y']
test_x = hasy_data['test']['X']
test_y = hasy_data['test']['y']

# Define model
net = input_data(shape=[None, img_rows, img_cols, 1], name='input')
net = conv_2d(net, 32, 3, activation='prelu')
net = conv_2d(net, 64, 3, activation='prelu')
net = max_pool_2d(net, 2)
net = dropout(net, keep_prob=0.25)
net = fully_connected(net, 1024, activation='tanh')
net = dropout(net, keep_prob=0.5)
net = fully_connected(net, hasy_data['n_classes'], activation='softmax')

# Train model
net = regression(net, optimizer='adam', learning_rate=0.001,
                 loss='categorical_crossentropy', name='target')
model = tflearn.DNN(net, tensorboard_verbose=0)
model.fit({'input': train_x}, {'target': train_y}, n_epoch=nb_epoch,
          validation_set=({'input': test_x}, {'target': test_y}),
          snapshot_step=100, show_metric=True, run_id='convnet_mnist',
          batch_size=batch_size)

# Serialize model
model.save('my_model.tflearn')

# Evaluate model
score = model.evaluate(test_x, test_y)
print('Test accuarcy: %0.4f%%' % (score[0] * 100))

# Run the model on one example
prediction = model.predict([test_x[0]])
print("Prediction: %s" % str(prediction[0][:3]))  # only show first 3 probas
