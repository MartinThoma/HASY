model_checkpoint_path: checkpoints/hasy_tf-cnn-3-32-m-64-1024-369-relu_model.ckpt
validation_curve_path: validation-curves/validation-curve-accuracy-tf-cnn-3-32-m-64-1024-369-relu-8.csv
Evaluate model
(16698, 1024)
tf-cnn-3-32-m-64-1024-369-relu:
    train_time: 2552.2 (min=2532.77, max=2565.35)
    test_time:  3.1 (min=2.99, max=3.14)
    acc:        77.4 (min=76.7, max=77.9)
{'tf-cnn-3-32-m-64-1024-369-relu': [{'training_time': 2532.7650158405304, 'testing_time': 3.1364870071411133, 'accuracy': 0.776777306967985}, {'training_time': 2552.443300962448, 'testing_time': 3.0861690044403076, 'accuracy': 0.7788138093832989}, {'training_time': 2548.1829268932343, 'testing_time': 3.0987019538879395, 'accuracy': 0.7786909477916396}, {'training_time': 2546.4463608264923, 'testing_time': 3.071932077407837, 'accuracy': 0.7754666666666666}, {'training_time': 2553.8617050647736, 'testing_time': 3.1344211101531982, 'accuracy': 0.76897493764105}, {'training_time': 2553.1900198459625, 'testing_time': 3.0482399463653564, 'accuracy': 0.7691850089232599}, {'training_time': 2557.976940870285, 'testing_time': 3.0863120555877686, 'accuracy': 0.7666527521020932}, {'training_time': 2559.4708001613617, 'testing_time': 3.045802116394043, 'accuracy': 0.7762969160889314}, {'training_time': 2565.347053050995, 'testing_time': 2.992043972015381, 'accuracy': 0.7770990537788957}]}
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
validation_curve_path: validation-curves/validation-curve-accuracy-tf-cnn-3-32-m-64-1024-369-relu-9.csv
Evaluate model
(16661, 1024)
tf-cnn-3-32-m-64-1024-369-relu:
    train_time: 2553.9 (min=2532.77, max=2569.62)
    test_time:  3.1 (min=2.99, max=3.14)
    acc:        77.4 (min=76.7, max=77.9)
{'tf-cnn-3-32-m-64-1024-369-relu': [{'training_time': 2532.7650158405304, 'testing_time': 3.1364870071411133, 'accuracy': 0.776777306967985}, {'training_time': 2552.443300962448, 'testing_time': 3.0861690044403076, 'accuracy': 0.7788138093832989}, {'training_time': 2548.1829268932343, 'testing_time': 3.0987019538879395, 'accuracy': 0.7786909477916396}, {'training_time': 2546.4463608264923, 'testing_time': 3.071932077407837, 'accuracy': 0.7754666666666666}, {'training_time': 2553.8617050647736, 'testing_time': 3.1344211101531982, 'accuracy': 0.76897493764105}, {'training_time': 2553.1900198459625, 'testing_time': 3.0482399463653564, 'accuracy': 0.7691850089232599}, {'training_time': 2557.976940870285, 'testing_time': 3.0863120555877686, 'accuracy': 0.7666527521020932}, {'training_time': 2559.4708001613617, 'testing_time': 3.045802116394043, 'accuracy': 0.7762969160889314}, {'training_time': 2565.347053050995, 'testing_time': 2.992043972015381, 'accuracy': 0.7770990537788957}, {'training_time': 2569.6175878047943, 'testing_time': 3.0746641159057617, 'accuracy': 0.769641678170578}]}

real    25919,67s
user    22956,63s
sys 2494,01s
