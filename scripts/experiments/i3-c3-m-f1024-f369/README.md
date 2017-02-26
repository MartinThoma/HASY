    shape: (3, 3, 1, 3)
    variable_parametes: 27
    ---
    shape: (3,)
    variable_parametes: 3
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
total_parameters: 1427855
model_checkpoint_path: checkpoints/hasy_i3-c3-m-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i3-c3-m-f1024-f369-9.csv
Evaluate model
i3-c3-m-f1024-f369:
    train_time:    916.2 (min=835.20, max=1195.36)
    test_time:    1.5 (min=1.27, max=2.19)
    acc:        63.7 (min=63.0, max=64.3)
{'i3-c3-m-f1024-f369': [{'training_time': 875.8160290718079, 'testing_time': 1.2710678577423096, 'accuracy': 0.641066384180791}, {'training_time': 869.0229051113129, 'testing_time': 1.3357131481170654, 'accuracy': 0.6432575981115374}, {'training_time': 937.0396950244904, 'testing_time': 1.6803030967712402, 'accuracy': 0.6432921421391828}, {'training_time': 948.2216739654541, 'testing_time': 2.1932289600372314, 'accuracy': 0.6377481481481482}, {'training_time': 950.9654808044434, 'testing_time': 1.7252261638641357, 'accuracy': 0.6300629528447559}, {'training_time': 867.4567787647247, 'testing_time': 1.3095190525054932, 'accuracy': 0.6340273646638905}, {'training_time': 840.3434500694275, 'testing_time': 1.2976861000061035, 'accuracy': 0.6339674399188979}, {'training_time': 1195.3632998466492, 'testing_time': 1.3070881366729736, 'accuracy': 0.6366841979440593}, {'training_time': 835.2008891105652, 'testing_time': 1.297593116760254, 'accuracy': 0.6380404838902862}, {'training_time': 842.6198718547821, 'testing_time': 1.3064110279083252, 'accuracy': 0.6323750075025508}]}

real    9673,54s
user    10189,30s
sys    1779,55s