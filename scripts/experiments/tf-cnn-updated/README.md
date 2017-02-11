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
    shape: (3, 3, 32, 64)
    variable_parametes: 18432
    ---
    shape: (64,)
    variable_parametes: 64
    ---
    shape: (3, 3, 64, 64)
    variable_parametes: 36864
    ---
    shape: (64,)
    variable_parametes: 64
    ---
    shape: (4096, 1024)
    variable_parametes: 4194304
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
total_parameters: 5688145
model_checkpoint_path: checkpoints/hasy_cnn-32-32-64-64-1024-1024-relu-30000_model.ckpt
validation_curve_path: validation-curves/validation-curve-accuracy-cnn-32-32-64-64-1024-1024-relu-30000-9.csv
Evaluate model
(16661, 1024)
cnn-32-32-64-64-1024-1024-relu-30000:
    train_time: 1135.8 (min=1132.61, max=1136.96)
    test_time:  4.2 (min=4.06, max=4.29)
    acc:        80.5 (min=80.0, max=81.3)
{'cnn-32-32-64-64-1024-1024-relu-30000': [{'training_time': 1136.4310891628265, 'testing_time': 4.285802125930786, 'accuracy': 0.8076741996233522}, {'training_time': 1132.6091017723083, 'testing_time': 4.062856197357178, 'accuracy': 0.8128061375036884}, {'training_time': 1136.0135569572449, 'testing_time': 4.161237001419067, 'accuracy': 0.8073079879382723}, {'training_time': 1135.943303823471, 'testing_time': 4.239975929260254, 'accuracy': 0.8038518518518518}, {'training_time': 1134.9670128822327, 'testing_time': 4.257091999053955, 'accuracy': 0.8000950231618957}, {'training_time': 1136.9463620185852, 'testing_time': 4.169147968292236, 'accuracy': 0.802676977989292}, {'training_time': 1136.3487660884857, 'testing_time': 4.19609808921814, 'accuracy': 0.8069652334665156}, {'training_time': 1136.9594881534576, 'testing_time': 4.112294912338257, 'accuracy': 0.802354769304327}, {'training_time': 1136.806221961975, 'testing_time': 4.175023078918457, 'accuracy': 0.8048868127919512}, {'training_time': 1135.3537499904633, 'testing_time': 4.279524803161621, 'accuracy': 0.8060140447752235}]}

real    11773,85s
user    10480,81s
sys 1081,38s
