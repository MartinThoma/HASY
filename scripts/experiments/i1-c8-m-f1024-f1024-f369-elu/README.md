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
model_checkpoint_path: checkpoints/hasy_i1-c8-m-f1024-f1024-f369-elu_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c8-m-f1024-f1024-f369-elu-9.csv
Evaluate model
i1-c8-m-f1024-f1024-f369-elu:
    Runs:    10
    train_time:    534.3 (min=524.69, max=543.05)
    test_time:    1.8 (min=1.81, max=1.88)
    acc:        79.5 (min=79.0, max=80.1)
{'i1-c8-m-f1024-f1024-f369-elu': [{'training_time': 533.2238280773163, 'testing_time': 1.859450101852417, 'accuracy': 0.7983757062146892}, {'training_time': 526.3178999423981, 'testing_time': 1.8758349418640137, 'accuracy': 0.8010032457952199}, {'training_time': 525.6047768592834, 'testing_time': 1.8268699645996094, 'accuracy': 0.7990303316975108}, {'training_time': 524.687548160553, 'testing_time': 1.8109140396118164, 'accuracy': 0.7957925925925926}, {'training_time': 537.4871578216553, 'testing_time': 1.8183841705322266, 'accuracy': 0.7896424753533674}, {'training_time': 541.5058391094208, 'testing_time': 1.825495958328247, 'accuracy': 0.7958358120166568}, {'training_time': 536.7668480873108, 'testing_time': 1.8385999202728271, 'accuracy': 0.7945613930466933}, {'training_time': 539.2500691413879, 'testing_time': 1.807352066040039, 'accuracy': 0.7908199856562276}, {'training_time': 534.7781050205231, 'testing_time': 1.8139100074768066, 'accuracy': 0.7933884297520661}, {'training_time': 543.0455560684204, 'testing_time': 1.883037805557251, 'accuracy': 0.7949702898985656}]}

real    5608,80s
user    5129,94s
sys    648,05s
