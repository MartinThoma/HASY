I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX TITAN Black, pci bus id: 0000:01:00.0)
    shape: (3, 3, 1, 32)
    variable_parametes: 288
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
total_parameters: 9817777
model_checkpoint_path: checkpoints/hasy_i1-c32-m-f1024-d0.5-f1024-d0.5-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-m-f1024-d0.5-f1024-d0.5-f369-9.csv
Evaluate model
i1-c32-m-f1024-d0.5-f1024-d0.5-f369:
    Runs:    10
    train_time:    960.2 (min=949.20, max=969.48)
    test_time:    2.5 (min=2.45, max=2.56)
    acc:        77.9 (min=77.2, max=79.1)
{'i1-c32-m-f1024-d0.5-f1024-d0.5-f369': [{'training_time': 949.2034299373627, 'testing_time': 2.558634042739868, 'accuracy': 0.785193032015066}, {'training_time': 955.3959300518036, 'testing_time': 2.4812660217285156, 'accuracy': 0.7905576866332251}, {'training_time': 964.2739100456238, 'testing_time': 2.4810848236083984, 'accuracy': 0.7819428841719387}, {'training_time': 964.8020849227905, 'testing_time': 2.5164408683776855, 'accuracy': 0.7822814814814815}, {'training_time': 969.4845249652863, 'testing_time': 2.4858241081237793, 'accuracy': 0.7720631904026607}, {'training_time': 959.3370358943939, 'testing_time': 2.472001791000366, 'accuracy': 0.7723973825104105}, {'training_time': 962.5118420124054, 'testing_time': 2.4914941787719727, 'accuracy': 0.7734510107937265}, {'training_time': 957.0700941085815, 'testing_time': 2.469107151031494, 'accuracy': 0.7792254362897442}, {'training_time': 962.8753008842468, 'testing_time': 2.470763921737671, 'accuracy': 0.7787160138938795}, {'training_time': 956.7986578941345, 'testing_time': 2.450092077255249, 'accuracy': 0.7721025148550508}]}

real    9891,51s
user    8415,25s
sys    1158,09s
