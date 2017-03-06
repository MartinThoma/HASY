    shape: (3, 3, 1, 8)
    variable_parametes: 72
    ---
    shape: (8,)
    variable_parametes: 8
    ---
    shape: (2048, 1024)
    variable_parametes: 2097152
    ---
    shape: (1024,)
    variable_parametes: 1024
    ---
    shape: (1024, 1024)
    variable_parametes: 1048576
    ---
    shape: (1024,)
    variable_parametes: 1024
    ---
    shape: (1024, 369)
    variable_parametes: 377856
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 3526081
model_checkpoint_path: checkpoints/hasy_i1-c8-m-f1024-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c8-m-f1024-f1024-f369-9.csv
Evaluate model
i1-c8-m-f1024-f1024-f369:
    Runs:    10
    train_time:    532.1 (min=523.36, max=540.39)
    test_time:    1.7 (min=1.57, max=1.85)
    acc:        79.7 (min=78.9, max=80.4)
{'i1-c8-m-f1024-f1024-f369': [{'training_time': 536.0666151046753, 'testing_time': 1.8373210430145264, 'accuracy': 0.7971398305084746}, {'training_time': 523.6539430618286, 'testing_time': 1.5661470890045166, 'accuracy': 0.7990557686633225}, {'training_time': 529.0730018615723, 'testing_time': 1.5810229778289795, 'accuracy': 0.8038786732099569}, {'training_time': 523.3576099872589, 'testing_time': 1.5844430923461914, 'accuracy': 0.8008888888888889}, {'training_time': 540.3948380947113, 'testing_time': 1.8267810344696045, 'accuracy': 0.7948687492576315}, {'training_time': 532.037435054779, 'testing_time': 1.832521915435791, 'accuracy': 0.7893515764425937}, {'training_time': 533.504312992096, 'testing_time': 1.8269648551940918, 'accuracy': 0.79474029459121}, {'training_time': 534.9536318778992, 'testing_time': 1.8119759559631348, 'accuracy': 0.7930910829548171}, {'training_time': 538.5109248161316, 'testing_time': 1.8473310470581055, 'accuracy': 0.8011139058569888}, {'training_time': 529.47483086586, 'testing_time': 1.5937700271606445, 'accuracy': 0.7924494328071544}]}

real    5601,52s
user    5014,19s
sys    655,56s