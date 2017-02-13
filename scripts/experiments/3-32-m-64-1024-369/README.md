Evaluate model
(16875, 1024)
tf-cnn-3-32-m-64-1024-369-relu:
    train_time: 2545.0 (min=2532.77, max=2552.44)
    test_time:  3.1 (min=3.07, max=3.14)
    acc:        77.7 (min=77.5, max=77.9)
{'tf-cnn-3-32-m-64-1024-369-relu': [{'training_time': 2532.7650158405304, 'testing_time': 3.1364870071411133, 'accuracy': 0.776777306967985}, {'training_time': 2552.443300962448, 'testing_time': 3.0861690044403076, 'accuracy': 0.7788138093832989}, {'training_time': 2548.1829268932343, 'testing_time': 3.0987019538879395, 'accuracy': 0.7786909477916396}, {'training_time': 2546.4463608264923, 'testing_time': 3.071932077407837, 'accuracy': 0.7754666666666666}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX TITAN Black, pci bus id: 0000:01:00.0)
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
model_checkpoint_path: checkpoints/hasy_tf-cnn-3-32-m-64-1024-369-relu_model.ckpt
validation_curve_path: validation-curves/validation-curve-accuracy-tf-cnn-3-32-m-64-1024-369-relu-4.csv