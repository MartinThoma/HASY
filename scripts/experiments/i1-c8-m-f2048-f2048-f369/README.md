I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX TITAN Black, pci bus id: 0000:01:00.0)
    shape: (3, 3, 1, 8)
    variable_parametes: 72
    ---
    shape: (8,)
    variable_parametes: 8
    ---
    shape: (2048, 2048)
    variable_parametes: 4194304
    ---
    shape: (2048,)
    variable_parametes: 2048
    ---
    shape: (2048, 2048)
    variable_parametes: 4194304
    ---
    shape: (2048,)
    variable_parametes: 2048
    ---
    shape: (2048, 369)
    variable_parametes: 755712
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 9148865
model_checkpoint_path: checkpoints/hasy_i1-c8-m-f2048-f2048-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c8-m-f2048-f2048-f369-9.csv
Evaluate model
i1-c8-m-f2048-f2048-f369:
    Runs:    10
    train_time:    761.8 (min=757.21, max=766.17)
    test_time:    1.9 (min=1.91, max=1.97)
    acc:        79.3 (min=78.1, max=79.9)
{'i1-c8-m-f2048-f2048-f369': [{'training_time': 757.2070660591125, 'testing_time': 1.9090309143066406, 'accuracy': 0.7951388888888888}, {'training_time': 762.9189310073853, 'testing_time': 1.944640874862671, 'accuracy': 0.7988197108291532}, {'training_time': 760.587424993515, 'testing_time': 1.915320873260498, 'accuracy': 0.7987347011174836}, {'training_time': 764.8651521205902, 'testing_time': 1.9387259483337402, 'accuracy': 0.7806222222222222}, {'training_time': 764.105406999588, 'testing_time': 1.9401471614837646, 'accuracy': 0.7907114859246941}, {'training_time': 761.3982131481171, 'testing_time': 1.9651439189910889, 'accuracy': 0.7930398572278405}, {'training_time': 766.1749560832977, 'testing_time': 1.9298510551452637, 'accuracy': 0.7903273898264656}, {'training_time': 762.4326388835907, 'testing_time': 1.9126060009002686, 'accuracy': 0.7921348314606742}, {'training_time': 758.5607948303223, 'testing_time': 1.9202499389648438, 'accuracy': 0.7950053898670499}, {'training_time': 759.3276960849762, 'testing_time': 1.9737122058868408, 'accuracy': 0.7974911469899766}]}

real    7865,87s
user    6835,39s
sys    1035,28s
