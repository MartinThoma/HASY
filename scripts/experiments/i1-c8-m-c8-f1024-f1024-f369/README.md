I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX TITAN Black, pci bus id: 0000:01:00.0)
    shape: (3, 3, 1, 8)
    variable_parametes: 72
    ---
    shape: (8,)
    variable_parametes: 8
    ---
    shape: (3, 3, 8, 8)
    variable_parametes: 576
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
total_parameters: 3526665
model_checkpoint_path: checkpoints/hasy_i1-c8-m-c8-f1024-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c8-m-c8-f1024-f1024-f369-9.csv
Evaluate model
i1-c8-m-c8-f1024-f1024-f369:
    Runs:    10
    train_time:    610.3 (min=603.03, max=615.20)
    test_time:    2.1 (min=2.02, max=2.11)
    acc:        78.3 (min=76.9, max=79.8)
{'i1-c8-m-c8-f1024-f1024-f369': [{'training_time': 603.029718875885, 'testing_time': 2.0393099784851074, 'accuracy': 0.7709510357815442}, {'training_time': 608.4000680446625, 'testing_time': 2.109786033630371, 'accuracy': 0.7864856889938034}, {'training_time': 608.3185579776764, 'testing_time': 2.0321359634399414, 'accuracy': 0.79489150357713}, {'training_time': 614.7609031200409, 'testing_time': 2.082200050354004, 'accuracy': 0.7976296296296296}, {'training_time': 610.8709800243378, 'testing_time': 2.087230920791626, 'accuracy': 0.7740824325929445}, {'training_time': 614.0779008865356, 'testing_time': 2.1058201789855957, 'accuracy': 0.7690065437239738}, {'training_time': 608.3647518157959, 'testing_time': 2.094428062438965, 'accuracy': 0.7788776909773988}, {'training_time': 609.9535810947418, 'testing_time': 2.050330877304077, 'accuracy': 0.7817355964618695}, {'training_time': 609.6920440196991, 'testing_time': 2.077549934387207, 'accuracy': 0.7894957479937718}, {'training_time': 615.2014169692993, 'testing_time': 2.023513078689575, 'accuracy': 0.7888482083908529}]}

real    6372,32s
user    5845,22s
sys    729,30s
