#!/usr/bin/env python

"""Train a NN on the HASY dataset with Tensorflow."""


import tensorflow as tf
tf.set_random_seed(0)  # make sure results are reproducible
import tflearn
from tflearn.layers.core import fully_connected
import os
import numpy as np
np.random.seed(0)  # make sure results are reproducible
import time
import sys
sys.path.append('/home/moose/GitHub/HASY/scripts')
import input_data
from classifier_comp import write_analyzation_results, pretty_print

batch_size = 128
epochs = 50000  # 200000
MODEL_NAME = 'i1-c32-m-c64-f1024-d0.5-f369'
model_checkpoint_path = 'checkpoints/hasy_%s_model.ckpt' % MODEL_NAME


def eval_network(sess, summary_writer, dataset, correct_prediction, epoch,
                 mode):
    """Evaluate the network."""
    correct_sum = 0
    total_test = 0
    batch_size = 1000
    for i in range(dataset.labels.shape[0] / batch_size):
        feed_dict = {x: dataset.images[i * batch_size:(i + 1) * batch_size],
                     y_: dataset.labels[i * batch_size:(i + 1) * batch_size]}
        test_correct = correct_prediction.eval(feed_dict=feed_dict)
        correct_sum += sum(test_correct)
        total_test += len(test_correct)
    return float(correct_sum) / total_test


def log_score(sess, summary_writer, filename, data, scoring, epoch):
    """Write the score to in CSV format to a file."""
    with open(filename, "a") as myfile:
        train = eval_network(sess, summary_writer, data.train, scoring, epoch,
                             "train")
        test = eval_network(sess, summary_writer, data.test, scoring, epoch,
                            "test")
        myfile.write("%i;%0.6f;%0.6f\n" % (epoch, train, test))


def get_nonexisting_path(model_checkpoint_path):
    """Get a path which no other file uses."""
    if not os.path.isfile(model_checkpoint_path):
        return model_checkpoint_path
    else:
        folder = os.path.dirname(model_checkpoint_path)
        filename = os.path.basename(model_checkpoint_path)
        filename, ext = os.path.splitext(filename)
        i = 1
        gen_filename = os.path.join(folder, "%s-%i%s" % (filename, i, ext))
        while os.path.isfile(gen_filename):
            i += 1
            gen_filename = os.path.join(folder, "%s-%i%s" % (filename, i, ext))
        return gen_filename

classifier_data = {}
classifier_data[MODEL_NAME] = []
dataset_path = os.path.join(os.path.expanduser("~"), 'hasy')
for fold in range(1, 11):
    directory = os.path.join(dataset_path,
                             'classification-task/fold-%i/' % fold)
    hasy = input_data.read_data_sets(os.path.join(directory, 'train.csv'),
                                     os.path.join(directory, 'test.csv'),
                                     dataset_path=dataset_path,
                                     one_hot=True)
    results = {}

    tf.reset_default_graph()  # Don't influence the other folds
    tf.set_random_seed(0)  # make sure results are reproducible
    with tf.Session() as sess:
        x = tf.placeholder(tf.float32, shape=[None, 1024])
        y_ = tf.placeholder(tf.float32, shape=[None, 369])
        net = tf.reshape(x, [-1, 32, 32, 1])
        net = tflearn.layers.conv.conv_2d(net,
                                          nb_filter=32,
                                          filter_size=3,
                                          activation='relu',
                                          strides=1,
                                          weight_decay=0.0)
        net = tflearn.layers.conv.max_pool_2d(net,
                                              kernel_size=2,
                                              strides=2,
                                              padding='same',
                                              name='MaxPool2D')
        net = tflearn.layers.conv.conv_2d(net,
                                          nb_filter=64,
                                          filter_size=3,
                                          activation='relu',
                                          strides=1,
                                          weight_decay=0.0)
        net = tflearn.layers.core.flatten(net, name='Flatten')
        net = fully_connected(net, 1024,
                              activation='tanh',
                              weights_init='truncated_normal',
                              bias_init='zeros',
                              regularizer=None,
                              weight_decay=0)
        net = tflearn.layers.core.dropout(net, keep_prob=0.5)
        y_conv = fully_connected(net, 369,
                                 activation='softmax',
                                 weights_init='truncated_normal',
                                 bias_init='zeros',
                                 regularizer=None,
                                 weight_decay=0)

        # for op in y_conv.get_operations():
        #     flops = ops.get_stats_for_node_def(g, op.node_def, 'flops').value
        #     print("FLOPS: %s" % str(flops))

        total_parameters = 0
        for variable in tf.trainable_variables():
            # shape is an array of tf.Dimension
            shape = variable.get_shape()
            print("    shape: %s" % str(shape))
            variable_parametes = 1
            for dim in shape:
                variable_parametes *= dim.value
            print("    variable_parametes: %i" % variable_parametes)
            total_parameters += variable_parametes
            print("    ---")
        print("total_parameters: %i" % total_parameters)

        single_errors = y_ * tf.log(y_conv + 10**(-7))
        cross_entropy = tf.reduce_mean(-tf.reduce_sum(single_errors,
                                                      reduction_indices=[1]))
        step = tf.Variable(0, trainable=False)
        rate = tf.train.exponential_decay(1e-3, step, 1, 0.9999)
        train_step = tf.train.AdamOptimizer(rate).minimize(cross_entropy,
                                                           global_step=step)
        correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        # tf.summary.scalar("training_accuracy", accuracy)
        # tf.summary.scalar("loss", cross_entropy)
        # Add ops to save and restore all the variables.
        saver = tf.train.Saver()
        summary_writer = tf.summary.FileWriter('summary_dir', sess.graph)

        sess.run(tf.global_variables_initializer())
        model_checkpoint_path = get_nonexisting_path(model_checkpoint_path)
        validation_curve_path = get_nonexisting_path('validation'
                                                     '-curve-accuracy-%s.csv' %
                                                     MODEL_NAME)
        print("model_checkpoint_path: %s" % model_checkpoint_path)
        print("validation_curve_path: %s" % validation_curve_path)
        t0 = time.time()
        for i in range(epochs):
            batch = hasy.train.next_batch(batch_size)
            if i % 500 == 0:
                log_score(sess, summary_writer,
                          validation_curve_path,
                          hasy, correct_prediction, i)
            train_step.run(feed_dict={x: batch[0],
                                      y_: batch[1]
                                      })
        t1 = time.time()
        results['fit_time'] = t1 - t0

        log_score(sess, summary_writer, validation_curve_path,
                  hasy, correct_prediction, epochs)

        # Evaluate model
        print("Evaluate model")
        cm = np.zeros((369, 369), dtype=int)
        t0 = time.time()
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
        t1 = time.time()
        results['testing_time'] = t1 - t0
        results['accuracy'] = (float(sum([cm[i][i] for i in range(369)])) /
                               len(hasy.test.images))
        classifier_data[MODEL_NAME].append({'training_time':
                                            results['fit_time'],
                                            'testing_time':
                                                results['testing_time'],
                                            'accuracy':
                                                results['accuracy']})
        with open("cnn-comp.md", "a") as handle:
            write_analyzation_results(handle,
                                      'CNN %s' % MODEL_NAME,
                                      results,
                                      cm)
    pretty_print(classifier_data)
    # Save the variables to disk.
    # save_path = saver.save(sess, model_checkpoint_path)
    # print("Model saved in file: %s" % save_path)
