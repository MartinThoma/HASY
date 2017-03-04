Evaluate model
i1-c32-m-c32-f1024-f369:
    train_time:    1120.8 (min=1100.77, max=1131.32)
    test_time:    2.2 (min=2.12, max=2.24)
    acc:        79.2 (min=78.8, max=79.5)
{'i1-c32-m-c32-f1024-f369': [{'training_time': 1100.773561000824, 'testing_time': 2.2001869678497314, 'accuracy': 0.7929025423728814}, {'training_time': 1120.703742980957, 'testing_time': 2.1214139461517334, 'accuracy': 0.7952198288580702}, {'training_time': 1126.9990420341492, 'testing_time': 2.1797380447387695, 'accuracy': 0.7935907290250104}, {'training_time': 1123.9655830860138, 'testing_time': 2.237478017807007, 'accuracy': 0.7905185185185185}, {'training_time': 1131.3201270103455, 'testing_time': 2.2216758728027344, 'accuracy': 0.7878014015916379}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX TITAN Black, pci bus id: 0000:01:00.0)
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
    shape: (8192, 1024)
    variable_parametes: 8388608
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
total_parameters: 8777425
model_checkpoint_path: checkpoints/hasy_i1-c32-m-c32-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-m-c32-f1024-f369-