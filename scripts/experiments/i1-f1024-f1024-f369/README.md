I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX TITAN Black, pci bus id: 0000:01:00.0)
    shape: (1024, 1024)
    variable_parametes: 1048576
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
total_parameters: 2477425
model_checkpoint_path: checkpoints/hasy_i1-f1024-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-f1024-f1024-f369-9.csv
Evaluate model
i1-f1024-f1024-f369:
    Runs:    10
    train_time:    294.5 (min=291.65, max=296.21)
    test_time:    1.3 (min=1.24, max=1.35)
    acc:        74.2 (min=73.8, max=74.8)
{'i1-f1024-f1024-f369': [{'training_time': 291.64603090286255, 'testing_time': 1.336259126663208, 'accuracy': 0.7448210922787194}, {'training_time': 295.348895072937, 'testing_time': 1.2585320472717285, 'accuracy': 0.7477131897314843}, {'training_time': 295.51010513305664, 'testing_time': 1.2575600147247314, 'accuracy': 0.7458759534086206}, {'training_time': 295.25428318977356, 'testing_time': 1.272313117980957, 'accuracy': 0.7424}, {'training_time': 296.21237993240356, 'testing_time': 1.2664940357208252, 'accuracy': 0.7383299679296829}, {'training_time': 294.91037797927856, 'testing_time': 1.3456549644470215, 'accuracy': 0.74098750743605}, {'training_time': 295.4981679916382, 'testing_time': 1.2631268501281738, 'accuracy': 0.7404138589063152}, {'training_time': 293.8412301540375, 'testing_time': 1.2437639236450195, 'accuracy': 0.7385249820702845}, {'training_time': 293.70529794692993, 'testing_time': 1.2375988960266113, 'accuracy': 0.7396095340759372}, {'training_time': 293.440034866333, 'testing_time': 1.2484779357910156, 'accuracy': 0.7398715563291519}]}

real    3197,01s
user    3062,02s
sys    344,67s
