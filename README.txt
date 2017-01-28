Please refer to the HASY paper for details about the dataset.
If you want to report problems of the HASY dataset, please send an email to
info@martin-thoma.de or file an issue at https://github.com/MartinThoma/HASY

Errata are listed in the git repository as well as the latest supplementary
files like `hasy_tools.py`.


## Contents

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
* `hasy_tools.py`: Various functions / command line tools
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


## hasy_tools

`hasy_tools.py` can be used in two ways: (1) as a shell script (2) as a Python
module.

If you want to get more information about the shell script options, execute

    python hasy_tools.py

If you want to use `hasy_tools.py` as a Python module, see

    python -c "import hasy_tools;help(hasy_tools)"


## Changelog

* 24.01.2017, HASYv2: Points were not rendered in HASYv1; improved hasy_tools
                      https://doi.org/10.5281/zenodo.259444
* 18.01.2017, HASYv1: Initial upload
                      https://doi.org/10.5281/zenodo.250239
