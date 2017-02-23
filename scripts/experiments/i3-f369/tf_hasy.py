#!/usr/bin/env python

"""Train a NN on the HASY dataset with Tensorflow."""


import tensorflow as tf
tf.set_random_seed(0)  # make sure results are reproducible
import tflearn
from tflearn.layers.core import fully_connected
import os
import numpy as np
np.random.seed(0)  # make sure results are reproducible
import sys
sys.path.append('/home/moose/GitHub/HASY/scripts')
import input_data

batch_size = 128
epochs = 1000  # 30000  # 200000
MODEL_NAME = 'i3-f369'
model_checkpoint_path = 'checkpoints/hasy_%s_model.ckpt' % MODEL_NAME

dataset_path = os.path.join(os.path.expanduser("~"), 'hasy')
for fold in range(1, 11):
    directory = os.path.join(dataset_path,
                             'classification-task/fold-%i/' % fold)
    hasy = input_data.read_data_sets(os.path.join(directory, 'train.csv'),
                                     os.path.join(directory, 'test.csv'),
                                     dataset_path=dataset_path,
                                     one_hot=True)

    tf.reset_default_graph()  # Don't influence the other folds
    tf.set_random_seed(0)  # make sure results are reproducible
    with tf.Session() as sess:
        x = tf.placeholder(tf.float32, shape=[None, 1024])
        y_ = tf.placeholder(tf.float32, shape=[None, 369])
        y_conv = fully_connected(x, 369,
                                 activation='softmax',
                                 weights_init='truncated_normal',
                                 bias_init='zeros',
                                 regularizer=None,
                                 weight_decay=0)

        single_errors = y_ * tf.log(y_conv + 10**(-7))
        cross_entropy = tf.reduce_mean(-tf.reduce_sum(single_errors,
                                                      reduction_indices=[1]))
        train_step = tf.train.AdamOptimizer(1e-0).minimize(cross_entropy)
        correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        tf.summary.scalar("training_accuracy", accuracy)
        tf.summary.scalar("loss", cross_entropy)

        sess.run(tf.global_variables_initializer())
        for i in range(epochs):
            batch = hasy.train.next_batch(batch_size)
            train_step.run(feed_dict={x: batch[0], y_: batch[1]})

        print("Evaluate model")
        cm = np.zeros((369, 369), dtype=int)
        loops = int(len(hasy.test.images) / batch_size)
        if loops * batch_size < len(hasy.test.images):
            loops += 1

        for i in range(loops):
            data = hasy.test.images[i * batch_size:(i + 1) * batch_size]
            data = data.reshape((-1, 32 * 32))
            predicted = tf.argmax(y_conv, 1).eval(feed_dict={x: data})
            actual = np.argmax(hasy.test.labels[i * batch_size:
                                                (i + 1) * batch_size], 1)
            for pred, act in zip(predicted, actual):
                cm[act][pred] += 1
            print(cm)
