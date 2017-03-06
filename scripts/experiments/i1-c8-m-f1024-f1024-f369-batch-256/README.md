I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX TITAN Black, pci bus id: 0000:01:00.0)
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
model_checkpoint_path: checkpoints/hasy_i1-c8-m-f1024-f1024-f369-batch-256_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c8-m-f1024-f1024-f369-batch-256-9.csv
Evaluate model
i1-c8-m-f1024-f1024-f369-batch-256:
    Runs:    10
    train_time:    727.9 (min=719.82, max=732.45)
    test_time:    0.9 (min=0.92, max=0.95)
    acc:        79.4 (min=79.0, max=80.2)
{'i1-c8-m-f1024-f1024-f369-batch-256': [{'training_time': 719.8235189914703, 'testing_time': 0.9437389373779297, 'accuracy': 0.7931379472693032}, {'training_time': 725.4660220146179, 'testing_time': 0.9422919750213623, 'accuracy': 0.7990557686633225}, {'training_time': 731.0173399448395, 'testing_time': 0.9475030899047852, 'accuracy': 0.8019275113817773}, {'training_time': 729.0657241344452, 'testing_time': 0.9421229362487793, 'accuracy': 0.7975111111111111}, {'training_time': 728.5847318172455, 'testing_time': 0.9458608627319336, 'accuracy': 0.7932058439244566}, {'training_time': 727.8922069072723, 'testing_time': 0.9335010051727295, 'accuracy': 0.7904818560380725}, {'training_time': 727.0133421421051, 'testing_time': 0.9457042217254639, 'accuracy': 0.790208122130121}, {'training_time': 732.44602394104, 'testing_time': 0.9247560501098633, 'accuracy': 0.792194597179058}, {'training_time': 727.0571839809418, 'testing_time': 0.9331278800964355, 'accuracy': 0.7926098934004072}, {'training_time': 730.8742489814758, 'testing_time': 0.9312942028045654, 'accuracy': 0.7919692695516476}]}

real    7531,79s
user    6476,68s
sys    905,02s
