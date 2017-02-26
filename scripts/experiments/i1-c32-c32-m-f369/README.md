    shape: (3, 3, 1, 32)
    variable_parametes: 288
    ---
    shape: (32,)
    variable_parametes: 32
    ---
    shape: (3, 3, 32, 32)
    variable_parametes: 9216
    ---
    shape: (32,)
    variable_parametes: 32
    ---
    shape: (1024, 369)
    variable_parametes: 377856
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 387793
model_checkpoint_path: checkpoints/hasy_i1-c32-c32-m-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-c32-m-f369-9.csv
Evaluate model
i1-c32-c32-m-f369:
    train_time:    848.7 (min=809.98, max=940.23)
    test_time:    1.3 (min=1.22, max=1.59)
    acc:        63.7 (min=63.0, max=64.3)
{'i1-c32-c32-m-f369': [{'training_time': 860.5689690113068, 'testing_time': 1.5904829502105713, 'accuracy': 0.6410075329566854}, {'training_time': 915.8061089515686, 'testing_time': 1.4314239025115967, 'accuracy': 0.6433166125700797}, {'training_time': 940.228728055954, 'testing_time': 1.3198001384735107, 'accuracy': 0.6432330160231774}, {'training_time': 841.095242023468, 'testing_time': 1.269787073135376, 'accuracy': 0.6378074074074074}, {'training_time': 832.5864458084106, 'testing_time': 1.2890241146087646, 'accuracy': 0.6300629528447559}, {'training_time': 827.737734079361, 'testing_time': 1.2889771461486816, 'accuracy': 0.6340273646638905}, {'training_time': 826.396870136261, 'testing_time': 1.2929480075836182, 'accuracy': 0.6340270737670702}, {'training_time': 817.9332811832428, 'testing_time': 1.2241191864013672, 'accuracy': 0.6366244322256753}, {'training_time': 814.3793449401855, 'testing_time': 1.2151341438293457, 'accuracy': 0.6379207090669541}, {'training_time': 809.9806549549103, 'testing_time': 1.2269418239593506, 'accuracy': 0.6323750075025508}]}

real    8849,75s
user    10014,98s
sys    1707,35s
