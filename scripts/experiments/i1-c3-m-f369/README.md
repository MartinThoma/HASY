I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (3, 3, 1, 3)
    variable_parametes: 27
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
total_parameters: 283791
model_checkpoint_path: checkpoints/hasy_i1-c3-m-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c3-m-f369-9.csv
Evaluate model
i1-c3-m-f369:
    Runs:    10
    train_time:    1210.1 (min=1041.03, max=1335.73)
    test_time:    1.6 (min=1.54, max=1.75)
    acc:        55.5 (min=55.0, max=56.3)
{'i1-c3-m-f369': [{'training_time': 1041.0314610004425, 'testing_time': 1.610569953918457, 'accuracy': 0.5577330508474576}, {'training_time': 1073.4451820850372, 'testing_time': 1.5753870010375977, 'accuracy': 0.5630569489524934}, {'training_time': 1263.592553138733, 'testing_time': 1.5829200744628906, 'accuracy': 0.5586826701353989}, {'training_time': 1262.5201559066772, 'testing_time': 1.5510280132293701, 'accuracy': 0.5556148148148148}, {'training_time': 1318.9975559711456, 'testing_time': 1.5605559349060059, 'accuracy': 0.5513718968998693}, {'training_time': 1238.8889801502228, 'testing_time': 1.5577309131622314, 'accuracy': 0.5535990481856038}, {'training_time': 1335.732300043106, 'testing_time': 1.543532133102417, 'accuracy': 0.5543562526089808}, {'training_time': 1259.0088829994202, 'testing_time': 1.5512120723724365, 'accuracy': 0.5550442266316041}, {'training_time': 1144.088084936142, 'testing_time': 1.7521679401397705, 'accuracy': 0.5536591208527968}, {'training_time': 1163.8421618938446, 'testing_time': 1.7116820812225342, 'accuracy': 0.5496668867414921}]}

real    12895,99s
user    9160,82s
sys    4702,54s
