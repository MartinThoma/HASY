#!/usr/bin/env python

"""
Trains a simple convnet on the HASY dataset.

Gets to 76.78% test accuracy after 1 epoch.
673 seconds per epoch on a GeForce 940MX GPU.
"""

import numpy as np
import tensorflow as tf
import hasy.hasy_tools as ht


np.random.seed(0)  # make sure results are reproducible
tf.random.set_seed(0)  # make sure results are reproducible

if __name__ == "__main__":
    import tflearn
    from tflearn.layers.core import input_data, fully_connected, dropout
    from tflearn.layers.conv import conv_2d, max_pool_2d
    from tflearn.layers.estimator import regression

    batch_size = 128
    nb_epoch = 1

    # input image dimensions
    img_rows, img_cols = ht.img_rows, ht.img_cols

    # Load data
    fold = 1
    hasy_data = ht.load_data(mode="fold-{}".format(fold), image_dim_ordering="tf")

    x_train = hasy_data["x_train"]
    y_train = hasy_data["y_train"]
    x_test = hasy_data["x_test"]
    y_test = hasy_data["y_test"]

    # One-Hot encoding
    y_train = np.eye(ht.n_classes)[y_train.squeeze()]
    y_test = np.eye(ht.n_classes)[y_test.squeeze()]

    # Preprocessing
    x_train = ht.preprocess(x_train)
    x_test = ht.preprocess(x_test)

    # Define model
    net = input_data(shape=[None, img_rows, img_cols, 1], name="input")
    net = conv_2d(net, 32, 3, activation="prelu")
    net = conv_2d(net, 64, 3, activation="prelu")
    net = max_pool_2d(net, 2)
    net = dropout(net, keep_prob=0.25)
    net = fully_connected(net, 1024, activation="tanh")
    net = dropout(net, keep_prob=0.5)
    net = fully_connected(net, ht.n_classes, activation="softmax")

    # Train model
    net = regression(
        net,
        optimizer="adam",
        learning_rate=0.001,
        loss="categorical_crossentropy",
        name="target",
    )
    model = tflearn.DNN(net, tensorboard_verbose=0)
    model.fit(
        {"input": x_train},
        {"target": y_train},
        n_epoch=nb_epoch,
        validation_set=({"input": x_test}, {"target": y_test}),
        snapshot_step=100,
        show_metric=True,
        run_id="convnet_mnist",
        batch_size=batch_size,
    )

    # Serialize model
    model.save("my_model.tflearn")

    # Evaluate model
    score = model.evaluate(x_test, y_test)
    print("Test accuarcy: {:0.2f}%".format(score[0] * 100))

    # Run the model on one example
    prediction = model.predict([x_test[0]])
    # only show first 3 probabilities
    print("Prediction: {}".format(str(prediction[0][:3])))
