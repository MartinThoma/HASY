## 1e-2
i3-c3-m-f369:
    train_time: 295.3 (min=294.43, max=296.23)
    test_time:  1.3 (min=1.30, max=1.34)
    acc:        58.9 (min=58.8, max=59.1)
{'i3-c3-m-f369': [{'training_time': 296.2313199043274, 'testing_time': 1.3381319046020508, 'accuracy': 0.5876883239171374}, {'training_time': 294.43039894104004, 'testing_time': 1.3006761074066162, 'accuracy': 0.5910888167601063}]}
    shape: (3, 3, 1, 3)
    variable_parametes: 27
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (1024, 369)
    variable_parametes: 377856
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 378255
[2]    3320 segmentation fault  python tf_hasy.py

real    684,01s
user    4181,00s
sys 223,63s

## 1e-1

Evaluate model
i3-c3-m-f369:
    train_time: 294.8 (min=294.16, max=295.47)
    test_time:  1.3 (min=1.30, max=1.35)
    acc:        63.4 (min=63.4, max=63.4)
{'i3-c3-m-f369': [{'training_time': 294.16494607925415, 'testing_time': 1.3504610061645508, 'accuracy': 0.6338865348399246}, {'training_time': 295.4726040363312, 'testing_time': 1.3015968799591064, 'accuracy': 0.6336972558276778}]}
    shape: (3, 3, 1, 3)
    variable_parametes: 27
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (1024, 369)
    variable_parametes: 377856
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 378255
[2]    3631 segmentation fault  python tf_hasy.py
