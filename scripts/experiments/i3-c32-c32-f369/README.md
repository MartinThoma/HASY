Evaluate model
i3-c32-c32-f369:
    train_time:    1094.4 (min=1094.42, max=1094.42)
    test_time:    1.4 (min=1.36, max=1.36)
    acc:        64.1 (min=64.1, max=64.1)
{'i3-c32-c32-f369': [{'training_time': 1094.422107219696, 'testing_time': 1.359382152557373, 'accuracy': 0.641066384180791}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
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
