    shape: (3, 3, 1, 32)
    variable_parametes: 288
    ---
    shape: (32,)
    variable_parametes: 32
    ---
    shape: (3, 3, 32, 64)
    variable_parametes: 18432
    ---
    shape: (64,)
    variable_parametes: 64
    ---
    shape: (16384, 1024)
    variable_parametes: 16777216
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
total_parameters: 17175281
model_checkpoint_path: checkpoints/hasy_i1-c32-m-c64-f1024-d0.5-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-m-c64-f1024-d0.5-f369-9.csv
Evaluate model
i1-c32-m-c64-f1024-d0.5-f369:
    train_time:    1672.9 (min=1665.57, max=1685.31)
    test_time:    2.7 (min=2.64, max=2.76)
    acc:        79.2 (min=78.9, max=79.8)
{'i1-c32-m-c64-f1024-d0.5-f369': [{'training_time': 1667.236479997635, 'testing_time': 2.734893798828125, 'accuracy': 0.7959039548022598}, {'training_time': 1680.0274150371552, 'testing_time': 2.7643308639526367, 'accuracy': 0.7976984361168487}, {'training_time': 1669.9604768753052, 'testing_time': 2.680663824081421, 'accuracy': 0.7912848105007982}, {'training_time': 1665.5662569999695, 'testing_time': 2.6791188716888428, 'accuracy': 0.7885037037037037}, {'training_time': 1673.889631986618, 'testing_time': 2.6488919258117676, 'accuracy': 0.7896424753533674}, {'training_time': 1673.4201829433441, 'testing_time': 2.7242770195007324, 'accuracy': 0.791017251635931}, {'training_time': 1669.6256868839264, 'testing_time': 2.667342185974121, 'accuracy': 0.7912218975490488}, {'training_time': 1672.8090510368347, 'testing_time': 2.6513350009918213, 'accuracy': 0.792254362897442}, {'training_time': 1671.0265572071075, 'testing_time': 2.6395070552825928, 'accuracy': 0.7929692178704036}, {'training_time': 1685.3120880126953, 'testing_time': 2.648765802383423, 'accuracy': 0.7926294940279696}]}

real    17017,59s
user    13817,39s
sys    1953,98s
