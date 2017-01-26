#!/usr/bin/env python

"""Train classifiers to predict HASY data."""

import numpy as np
import time
import tensorflow as tf
import tflearn
from tflearn.layers.core import input_data, flatten, fully_connected, reshape
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from sklearn.cross_validation import train_test_split

# Classifiers
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
# from sklearn.neural_network import BernoulliRBM
# from sklearn.pipeline import Pipeline
# from sklearn.linear_model import LogisticRegression
# from sklearn import cross_validation


class CNN(object):
    """CNN classifier object."""

    def __init__(self):
        self.epochs = 2 * 10**5
        self.sess = tf.Session()
        self.y_ = tf.placeholder(tf.float32, shape=[None, 369])
        net = input_data(shape=[None, 1024], name='input')
        net = reshape(net, new_shape=[-1, 32, 32, 1], name='reshape')
        net = conv_2d(net, nb_filter=3, filter_size=3)
        net = max_pool_2d(net, 2)
        net = flatten(net, name='Flatten')
        net = fully_connected(net, 369,
                              activation='softmax',
                              weights_init='truncated_normal',
                              bias_init='zeros',
                              regularizer=None,
                              weight_decay=0)
        self.net = regression(net, optimizer='adam', learning_rate=0.01,
                              loss='categorical_crossentropy', name='target')
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

    def fit(self, x, y):
        """Fit the CNN to data."""
        x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                            test_size=0.33,
                                                            random_state=42)
        self.model = tflearn.DNN(self.net, tensorboard_verbose=0)
        self.model.fit({'input': x_train}, {'target': y_train}, n_epoch=20,
                       validation_set=({'input': x_test}, {'target': y_test}),
                       snapshot_step=1000,
                       show_metric=True,
                       run_id='convnet_mnist')

    def predict(self, data):
        return self.model.predict(data)


def main():
    """Run experiment with multiple classifiers."""
    # Get classifiers
    classifiers = [
        # ('CNN', CNN()),
        ('Decision Tree', DecisionTreeClassifier(max_depth=5)),
        # ('Random Forest', RandomForestClassifier(n_estimators=50,
        #                                          n_jobs=10,
        #                                          max_features=50)),
        # ('AdaBoost', AdaBoostClassifier()),
        # ('Naive Bayes', GaussianNB()),
        # ('LDA', LinearDiscriminantAnalysis()),
        # ('QDA', QuadraticDiscriminantAnalysis()),
        # ('Random Forest 2', RandomForestClassifier(max_depth=5,
        #                                            n_estimators=10,
        #                                            max_features=1,
        #                                            n_jobs=10)),
        # ('Logistic Regression (C=1)', LogisticRegression(C=1)),
        # #('Logistic Regression (C=1000)', LogisticRegression(C=10000)),
        # ('RBM 200, n_iter=40, LR=0.01, Reg: C=1',
        #  Pipeline(steps=[('rbm', BernoulliRBM(n_components=200,
        #                                       n_iter=40,
        #                                       learning_rate=0.01,
        #                                       verbose=True)),
        #                  ('logistic', LogisticRegression(C=1))])),
        # ('RBM 200, n_iter=40, LR=0.01, Reg: C=10000',
        #  Pipeline(steps=[('rbm', BernoulliRBM(n_components=200,
        #                                       n_iter=40,
        #                                       learning_rate=0.01,
        #                                       verbose=True)),
        #                  ('logistic', LogisticRegression(C=10000))])),
        # ('RBM 100', Pipeline(steps=[('rbm', BernoulliRBM(n_components=100)),
        #                             ('logistic', LogisticRegression(C=1))])),
        # ('RBM 100, n_iter=20',
        #  Pipeline(steps=[('rbm', BernoulliRBM(n_components=100, n_iter=20)),
        #                  ('logistic', LogisticRegression(C=1))])),
        # ('RBM 256', Pipeline(steps=[('rbm', BernoulliRBM(n_components=256)),
        #                             ('logistic', LogisticRegression(C=1))])),
        # ('RBM 512, n_iter=100',
        #  Pipeline(steps=[('rbm', BernoulliRBM(n_components=512, n_iter=10)),
        #                  ('logistic', LogisticRegression(C=1))])),
        # ('NN 20:5', skflow.TensorFlowDNNClassifier(hidden_units=[20, 5],
        #                                            n_classes=data['n_classes'],
        #                                            steps=500)),
        # ('NN 500:200 dropout',
        # ('CNN', skflow.TensorFlowEstimator(model_fn=conv_model,
        #                                    n_classes=10,
        #                                    batch_size=100,
        #                                    steps=20000,
        #                                    learning_rate=0.001)),
        # ('SVM, adj.', SVC(probability=False,
        #                   kernel="rbf",
        #                   C=2.8,
        #                   gamma=.0073,
        #                   cache_size=200)),
        # ('SVM, linear', SVC(kernel="linear", C=0.025, cache_size=200)),
        # ('k nn', KNeighborsClassifier(3)),
        # ('Gradient Boosting', GradientBoostingClassifier())
    ]

    print("Start getting data.")
    data = get_data('hasy')
    print("Got data. Start.")

    # Fit them all
    classifier_data = {}
    with open('classifier-comp.md', 'w') as f:
        for clf_name, clf in classifiers:
            print(clf_name)
            classifier_data[clf_name] = []
            f.write("#" * 80)
            f.write("\n")
            f.write("Start fitting '%s' classifier.\n" % clf_name)
            for fold in range(len(data)):
                print(data[fold]['test']['X'].shape)
                print(data[fold]['test']['y'].shape)

                print("Got %i training samples and %i test samples." %
                      (len(data[fold]['train']['X']),
                       len(data[fold]['test']['X'])))
                t0 = time.time()
                examples = 10**9
                clf.fit(data[fold]['train']['X'][:examples],
                        data[fold]['train']['y'][:examples])
                t1 = time.time()
                an_data = analyze(clf,
                                  data[fold],
                                  t1 - t0, clf_name=clf_name, handle=f)
                classifier_data[clf_name].append({'training_time': t1 - t0,
                                                  'testing_time':
                                                      an_data['testing_time'],
                                                  'accuracy':
                                                      an_data['accuracy']})

    pretty_print(classifier_data)


def pretty_print(classifier_data):
    """Pretty print classifier data."""
    for clf_name, clf_data in classifier_data.items():
        print("%s:" % clf_name)
        train_times = np.array([el['training_time'] for el in clf_data])
        test_times = np.array([el['testing_time'] for el in clf_data])
        accuracy = np.array([el['accuracy'] for el in clf_data])
        print("\ttrain_time:\t%0.1f (min=%0.2f, max=%0.2f)" %
              (train_times.mean(), train_times.min(), train_times.max()))
        print("\ttest_time:\t%0.1f (min=%0.2f, max=%0.2f)" %
              (test_times.mean(), test_times.min(), test_times.max()))
        print("\tacc:\t\t%0.4f (min=%0.4f, max=%0.4f)" %
              (accuracy.mean(), accuracy.min(), accuracy.max()))
    print(classifier_data)


def analyze(clf, data, fit_time, clf_name='', handle=None):
    """
    Analyze how well a classifier performs on data.

    Parameters
    ----------
    clf : classifier object
    data : dict
    fit_time : float
    clf_name : str
    handle : write to file

    Returns
    -------
    dict
        accuracy and testing_time
    """
    results = {}

    # Get confusion matrix
    from sklearn import metrics
    t0 = time.time()
    predicted = np.array([])
    for i in range(0, len(data['test']['X']), 128):  # go in chunks of size 128
        predicted_single = clf.predict(data['test']['X'][i:(i + 128)])
        predicted = np.append(predicted, predicted_single)
    t1 = time.time()
    results['testing_time'] = t1 - t0
    results['fit_time'] = fit_time
    results['accuracy'] = metrics.accuracy_score(data['test']['y'], predicted)
    cm = (metrics.confusion_matrix(data['test']['y'], predicted)).tolist()
    write_analyzation_results(handle, clf_name, results, cm)
    return results


def write_analyzation_results(handle, clf_name, results, cm):
    """
    Write classifier results to open file handle.

    Parameters
    ----------
    handle : opened file
    clf_name : str
    results : dict
        keys: 'fit_time', 'testing_time', 'accuracy'
    """
    handle.write("Classifier: %s\n" % clf_name)
    handle.write("Accuracy: %0.4f\n" % results['accuracy'] * 100)
    handle.write("Testing time: %0.4fs\n" % results['testing_time'])
    handle.write("Training time: %0.4fs\n" % results['fit_time'])
    handle.write("Confusion matrix:\n")
    for row in cm:
        handle.write("%s\n" % row)
    handle.write("#" * 80)
    handle.write("\n")


def view_image(image, label=""):
    """
    View a single image.

    Parameters
    ----------
    image : numpy array
        Make sure this is of the shape you want.
    label : str
    """
    from matplotlib.pyplot import show, imshow, cm
    print("Label: %s" % label)
    imshow(image, cmap=cm.gray)
    show()


def get_data(dataset='iris'):
    """
    Get data ready to learn with.

    Parameters
    ----------
    dataset : str
        'iris'

    Returns
    -------
    dict
    """
    if dataset == 'iris':
        import sklearn
        from sklearn.datasets import fetch_mldata
        from sklearn.utils import shuffle
        mnist = fetch_mldata('iris')

        x = mnist.data
        y = mnist.target

        le = sklearn.preprocessing.LabelEncoder()
        le.fit(y)
        y = le.transform(y)

        x, y = shuffle(x, y, random_state=0)

        from sklearn.cross_validation import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                            test_size=0.33,
                                                            random_state=42)
        data = {'train': {'X': x_train,
                          'y': y_train},
                'test': {'X': x_test,
                         'y': y_test},
                'n_classes': len(np.unique(y_train))}
        scaler = sklearn.preprocessing.StandardScaler().fit(data['train']['X'])
        data['train']['X'] = scaler.transform(data['train']['X'])
        data['test']['X'] = scaler.transform(data['test']['X'])
    elif dataset == 'mnist_simple':
        # Load the simple, but similar digits dataset
        from sklearn.datasets import load_digits
        from sklearn.utils import shuffle
        digits = load_digits()
        x = [np.array(el).flatten() for el in digits.images]
        y = digits.target

        # Scale data to [-1, 1] - This is of mayor importance!!!
        x = x / 255.0 * 2 - 1

        x, y = shuffle(x, y, random_state=0)

        from sklearn.cross_validation import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                            test_size=0.33,
                                                            random_state=42)
        data = {'train': {'X': x_train,
                          'y': y_train},
                'test': {'X': x_test,
                         'y': y_test}}
    elif dataset == 'mnist':  # Load the original dataset
        from sklearn.datasets import fetch_mldata
        from sklearn.utils import shuffle
        mnist = fetch_mldata('MNIST original')

        x = mnist.data
        y = mnist.target

        # Scale data to [-1, 1] - This is of mayor importance!!!
        x = x / 255.0 * 2 - 1

        x, y = shuffle(x, y, random_state=0)

        from sklearn.cross_validation import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                            test_size=0.33,
                                                            random_state=42)
        data = {'train': {'X': x_train,
                          'y': y_train},
                'test': {'X': x_test,
                         'y': y_test}}
    elif dataset == 'hasy':
        import hasy_tools as ht
        dataset_path = '../'
        data_complete = []

        symbol_id2index = ht.generate_index("%s/symbols.csv" % dataset_path)
        base_ = "%s/10-fold-cross-validation/fold" % dataset_path
        for fold in range(1, 11):
            one_hot = False  # Only True for CNN
            x_train, y_train = ht.load_images('%s-%i/train.csv' %
                                              (base_, fold),
                                              symbol_id2index,
                                              one_hot=one_hot)
            # Shuffle the data
            perm = np.arange(len(y_train))
            np.random.shuffle(perm)
            x_train = x_train[perm]
            y_train = y_train[perm]
            x_test, y_test = ht.load_images('%s-%i/test.csv' %
                                            (base_, fold),
                                            symbol_id2index,
                                            one_hot=one_hot)
            data = {'train': {'X': x_train.reshape(x_train.shape[0],
                                                   x_train.shape[1] *
                                                   x_train.shape[2]),
                              'y': y_train},
                    'test': {'X': x_test.reshape(x_test.shape[0],
                                                 x_test.shape[1] *
                                                 x_test.shape[2]),
                             'y': y_test},
                    'n_classes': 369}
            data_complete.append(data)
        data = data_complete
    else:
        raise NotImplemented()
    return data


if __name__ == '__main__':
    main()
