Evaluate model
i1-c3-c3-f1024-f369:
    train_time:    3938.8 (min=3938.80, max=3938.80)
    test_time:    3.3 (min=3.32, max=3.32)
    acc:        75.2 (min=75.2, max=75.2)
{'i1-c3-c3-f1024-f369': [{'training_time': 3938.799903869629, 'testing_time': 3.3160600662231445, 'accuracy': 0.7517655367231638}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (3, 3, 1, 3)
    variable_parametes: 27
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (3, 3, 3, 3)
    variable_parametes: 81
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (3072, 1024)
    variable_parametes: 3145728
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
total_parameters: 3525097
model_checkpoint_path: checkpoints/hasy_i1-c3-c3-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c3-c3-f1024-f369-1.csv
