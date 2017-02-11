#!/usr/bin/env python

"""Train classifiers to predict HASY data."""

import time

# Classifiers
from sklearn.neighbors import KNeighborsClassifier

# HASY scripts
from classifier_comp import pretty_print, analyze
from classifier_comp import get_data
# from classifier_comp import write_analyzation_results, view_image


def max_k_samples(xs, ys, max_val=20):
    """
    Reduce the data to max_val elements per class.

    Parameters
    ----------
    xs : iterable of features
    ys : iterable of class labels (indices)
    max_val : int, optional (default: 20)
    """
    assert max_val >= 1
    from collections import defaultdict
    counter = defaultdict(int)
    xs_new = []
    ys_new = []
    for x, y in zip(xs, ys):
        if counter[y] < max_val:
            xs_new.append(x)
            ys_new.append(y)
            counter[y] += 1
    return xs_new, ys_new


def main():
    """Run experiment with multiple classifiers."""
    # Get classifiers
    classifiers = [
        ('k nn', KNeighborsClassifier(3)),
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
            for fold in data:
                tmp = max_k_samples(fold['train']['X'], fold['train']['y'], 50)
                fold['train']['X'], fold['train']['y'] = tmp
                print("Got %i training samples and %i test samples." %
                      (len(fold['train']['X']),
                       len(fold['test']['X'])))
                t0 = time.time()
                examples = 10**9
                clf.fit(fold['train']['X'][:examples],
                        fold['train']['y'][:examples])
                t1 = time.time()
                an_data = analyze(clf,
                                  fold,
                                  t1 - t0, clf_name=clf_name, handle=f)
                classifier_data[clf_name].append({'training_time': t1 - t0,
                                                  'testing_time':
                                                      an_data['testing_time'],
                                                  'accuracy':
                                                      an_data['accuracy']})
                pretty_print(classifier_data)

    pretty_print(classifier_data)


if __name__ == '__main__':
    main()
