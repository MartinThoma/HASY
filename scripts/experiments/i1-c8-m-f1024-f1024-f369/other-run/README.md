The results in this directory are from the same architecture, although the name does not contain "m"

I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX TITAN Black, pci bus id: 0000:01:00.0)
    shape: (3, 3, 1, 8)
    variable_parametes: 72
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
total_parameters: 3526081
model_checkpoint_path: checkpoints/hasy_i1-c8-f1024-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c8-f1024-f1024-f369-9.csv
Evaluate model
i1-c8-f1024-f1024-f369:
    Runs:    10
    train_time:    524.5 (min=518.12, max=534.46)
    test_time:    1.7 (min=1.53, max=1.89)
    acc:        79.7 (min=78.9, max=80.4)
{'i1-c8-f1024-f1024-f369': [{'training_time': 518.1730260848999, 'testing_time': 1.5315501689910889, 'accuracy': 0.79719868173258}, {'training_time': 522.1702959537506, 'testing_time': 1.5713300704956055, 'accuracy': 0.7973443493655946}, {'training_time': 521.1714189052582, 'testing_time': 1.5674359798431396, 'accuracy': 0.8044699343700112}, {'training_time': 525.1712110042572, 'testing_time': 1.8502998352050781, 'accuracy': 0.8012444444444444}, {'training_time': 519.1417798995972, 'testing_time': 1.5354039669036865, 'accuracy': 0.7951656966385556}, {'training_time': 533.2836759090424, 'testing_time': 1.8108210563659668, 'accuracy': 0.7889946460440214}, {'training_time': 518.1197130680084, 'testing_time': 1.549103021621704, 'accuracy': 0.7949788299838989}, {'training_time': 530.5423970222473, 'testing_time': 1.806518793106079, 'accuracy': 0.7929715515180492}, {'training_time': 534.462317943573, 'testing_time': 1.8921639919281006, 'accuracy': 0.8014732303269853}, {'training_time': 522.6804349422455, 'testing_time': 1.605881929397583, 'accuracy': 0.7915491267030791}]}

real    5482,11s
user    4955,76s
sys    628,18s
