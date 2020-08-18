[![PyPI version](https://badge.fury.io/py/hasy.svg)](https://badge.fury.io/py/hasy)
[![Python Support](https://img.shields.io/pypi/pyversions/hasy.svg)](https://pypi.org/project/hasy/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub last commit](https://img.shields.io/github/last-commit/MartinThoma/HASY)
![GitHub commits since latest release (by SemVer)](https://img.shields.io/github/commits-since/MartinThoma/HASY/0.3.1)
[![CodeFactor](https://www.codefactor.io/repository/github/martinthoma/HASY/badge/master)](https://www.codefactor.io/repository/github/martinthoma/HASY/overview/master)

Please refer to the [HASY paper](https://arxiv.org/abs/1701.08380) for details
about the dataset. If you want to report problems of the HASY dataset, please
send an email to info@martin-thoma.de or file an issue at
https://github.com/MartinThoma/HASY

Errata are listed in the git repository as well as the actual `hasy` package.


## Contents

The contents of the [HASYv2 dataset](https://zenodo.org/record/259444) are:

* `hasy-data`: 168236 png images, each 32px x 32px
* `hasy-data-labels.csv`: Labels for all images.
* `classification-task`: 10 folders (fold-1, fold-2, ..., fold-10) which
  contain a `train.csv` and a `test.csv` each. Every line of the csv files
  points to one of the png images (relative to itself). If those files are
  used, then the `hasy-data-labels.csv` is not necessary.
* `verification-task`: A `train.csv` and three different test files. All files
  should be used in exactly the same way, but the accuracy should be reported
  for each one.
  The task is to decide for a pair of two 32px x 32px images if they belong
  to the same symbol (binary classification).
* `symbols.csv`: All classes
* `README.txt`: This file


## How to evaluate

### Classification Task

Use the pre-defined 10 folds for 10-fold cross-validation. Report the
average accuracy as well as the minumum and maximum accuracy.


### Verification Task

Use the `train.csv` for training. Use `test-v1.csv`, test-v2.csv`,
`test-v3.csv` for evaluation. Report TP, TN, FP, FN and accuracy for each
of the three test groups.


## hasy package

`hasy` can be used in two ways: (1) as a shell script (2) as a Python
module.

If you want to get more information about the shell script options, execute

```
$ hasy --help
usage: hasy [-h] [--dataset DATASET] [--verify] [--overview] [--analyze_color]
            [--class_distribution] [--distances] [--pca] [--variance]
            [--correlation] [--count-users] [--analyze-cm CM]

optional arguments:
  -h, --help            show this help message and exit
  --dataset DATASET     specify which data to use (default: None)
  --verify              verify PNG files (default: False)
  --overview            Get overview of data (default: False)
  --analyze_color       Analyze the color distribution (default: False)
  --class_distribution  Analyze the class distribution (default: False)
  --distances           Analyze the euclidean distance distribution (default:
                        False)
  --pca                 Show how many principal components explain 90% / 95% /
                        99% of the variance (default: False)
  --variance            Analyze the variance of features (default: False)
  --correlation         Analyze the correlation of features (default: False)
  --count-users         Count how many different users have created the
                        dataset (default: False)
  --analyze-cm CM       Analyze a confusion matrix in JSON format. (default:
                        False)
```


If you want to use `hasy` as a Python package, see

    python -c "import hasy.hasy_tools;help(hasy.hasy_tools)"


## Changelog

* 14.05.2020, hasy Python package: Major refactoring of this repository
* 24.01.2017, HASYv2: Points were not rendered in HASYv1; improved hasy_tools
                      https://doi.org/10.5281/zenodo.259444
* 18.01.2017, HASYv1: Initial upload
                      https://doi.org/10.5281/zenodo.250239
