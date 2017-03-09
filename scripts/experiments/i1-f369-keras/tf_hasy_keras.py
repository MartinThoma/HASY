#!/usr/bin/env python

"""Train a NN on the HASY dataset with Tensorflow."""


import tensorflow as tf
tf.set_random_seed(0)  # make sure results are reproducible
import os
import numpy as np
np.random.seed(0)  # make sure results are reproducible
import keras
from keras.models import Sequential
from keras.layers import Flatten, Dense
from keras.layers import Convolution2D
import time
import sys
sys.path.append('/home/moose/GitHub/HASY/scripts')
from hasy_tools import generate_index, load_images
from classifier_comp import write_analyzation_results, pretty_print

batch_size = 128
epochs = 10  # 200000
MODEL_NAME = 'i3-f369'
model_checkpoint_path = 'checkpoints/hasy_%s_model.ckpt' % MODEL_NAME


def eval_network(model, dataset):
    """Evaluate the network."""
    correct_sum = 0
    total_test = 0
    batch_size = 1000
    for i in range(dataset.labels.shape[0] / batch_size):
        xs = dataset.images[i * batch_size:(i + 1) * batch_size]
        ys = dataset.labels[i * batch_size:(i + 1) * batch_size]
        print("xs.shape=%s" % str(xs.shape))
        ys_pred = model.predict(xs)
        print(ys_pred)
        test_correct = sum(ys_pred == ys)
        # test_correct = correct_prediction.eval(feed_dict=feed_dict)
        correct_sum += sum(test_correct)
        total_test += len(test_correct)
    return float(correct_sum) / total_test


def log_score(model, filename, data, epoch):
    """Write the score to in CSV format to a file."""
    with open(filename, "a") as myfile:
        train = eval_network(model, data.train)
        test = eval_network(model, data.test)
        myfile.write("%i;%0.6f;%0.6f\n" % (epoch, train, test))


class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))


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
    print("#" * 80)
    print("Fold %i" % fold)
    directory = os.path.join(dataset_path,
                             'classification-task/fold-%i/' % fold)
    train_labels_csv = os.path.join(directory, 'train.csv')
    test_labels_csv = os.path.join(directory, 'test.csv')
    symbol_id2index = generate_index(os.path.join(dataset_path, 'symbols.csv'))
    print("\tLoad images ....")
    test_images, test_labels, _ = load_images(test_labels_csv,
                                              symbol_id2index)
    train_images, train_labels, _ = load_images(train_labels_csv,
                                                symbol_id2index)
    print("\t... done loading images")
    results = {}

    model_checkpoint_path = get_nonexisting_path(model_checkpoint_path)
    validation_curve_path = get_nonexisting_path('validation'
                                                 '-curve-accuracy-%s.csv' %
                                                 MODEL_NAME)
    print("model_checkpoint_path: %s" % model_checkpoint_path)
    print("validation_curve_path: %s" % validation_curve_path)
    t0 = time.time()
    # for i in range(epochs):
    #     batch = hasy.train.next_batch(batch_size)
    #     if i % 500 == 0:
    #         log_score(model,
    #                   validation_curve_path,
    #                   hasy, i)
    #     x = batch[0]
    #     y = batch[1]
    history = LossHistory()

    model = Sequential()
    model.add(Convolution2D(64, 3, 3, border_mode='same', input_shape=(32, 32, 1)))
    # model.add(Dense(1024, input_shape=(32, 32,)))
    model.add(Flatten())
    model.add(Dense(369, activation='softmax'))
    opt = keras.optimizers.Adamax(lr=0.002,
                                  beta_1=0.9,
                                  beta_2=0.999,
                                  epsilon=1e-08,
                                  decay=0.0)
    model.compile(optimizer=opt,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    print(model.summary())
    print("Total parameter: %i" % model.count_params())

    model.fit(train_images, train_labels,
              batch_size=batch_size, nb_epoch=epochs, verbose=1,
              callbacks=[history],
              validation_split=0.0,
              validation_data=None,
              shuffle=True,
              class_weight=None,
              sample_weight=None,
              initial_epoch=0)
    t1 = time.time()
    results['fit_time'] = t1 - t0

    # log_score(model, validation_curve_path, hasy, epochs)

    # Evaluate model
    print("Evaluate model")
    cm = np.zeros((369, 369), dtype=int)
    t0 = time.time()
    predicted = model.predict(test_images)
    print(predicted)
    predicted = np.argmax(predicted, 1)
    print(predicted)
    actual = np.argmax(test_labels, 1)
    for pred, act in zip(predicted, actual):
        cm[act][pred] += 1
    results['accuracy'] = (float(sum([cm[i][i] for i in range(369)])) /
                           len(test_images))
    print("accuracy: %0.4f" % results['accuracy'])
    # loops = int(len(hasy.test.images) / batch_size)
    # if loops * batch_size < len(hasy.test.images):
    #     loops += 1

    # for i in range(loops):
    #     data = hasy.test.images[i * batch_size:(i + 1) * batch_size]
    #     data = data.reshape((-1, 32 * 32))
    #     predicted = model.predict(data)
    #     predicted = predicted.argmax(1)
    #     actual = np.argmax(hasy.test.labels[i * batch_size:
    #                                         (i + 1) * batch_size], 1)
    #     for pred, act in zip(predicted, actual):
    #         cm[act][pred] += 1
    t1 = time.time()
    results['testing_time'] = t1 - t0
    # results['accuracy'] = (float(sum([cm[i][i] for i in range(369)])) /
    #                        len(hasy.test.images))
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
