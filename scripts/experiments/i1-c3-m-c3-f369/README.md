Evaluate model
i1-c3-m-c3-f369:
    train_time:    2501.2 (min=2458.60, max=2543.73)
    test_time:    1.9 (min=1.86, max=1.94)
    acc:        68.1 (min=68.0, max=68.3)
{'i1-c3-m-c3-f369': [{'training_time': 2458.6010291576385, 'testing_time': 1.9363279342651367, 'accuracy': 0.67984934086629}, {'training_time': 2543.7295010089874, 'testing_time': 1.8588979244232178, 'accuracy': 0.6830333431690764}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (3, 3, 1, 3)
    variable_parametes: 27
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
    shape: (768, 369)
    variable_parametes: 283392
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 283875
