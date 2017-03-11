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
model_checkpoint_path: checkpoints/hasy_i1-c32-m-f1024-d0.5-f1024-d0.5-f369-relu-all_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-m-f1024-d0.5-f1024-d0.5-f369-relu-all-9.csv
Evaluate model
i1-c32-m-f1024-d0.5-f1024-d0.5-f369-relu-all:
    Runs:    10
    train_time:    980.2 (min=971.28, max=982.68)
    test_time:    2.6 (min=2.52, max=2.61)
    acc:        79.6 (min=79.1, max=80.4)
{'i1-c32-m-f1024-d0.5-f1024-d0.5-f369-relu-all': [{'training_time': 971.2775208950043, 'testing_time': 2.5701029300689697, 'accuracy': 0.8014948210922788}, {'training_time': 977.9225039482117, 'testing_time': 2.6024649143218994, 'accuracy': 0.8041900265565064}, {'training_time': 980.1166250705719, 'testing_time': 2.5321969985961914, 'accuracy': 0.7989712055815054}, {'training_time': 980.3558850288391, 'testing_time': 2.528424024581909, 'accuracy': 0.794725925925926}, {'training_time': 981.6579699516296, 'testing_time': 2.5670220851898193, 'accuracy': 0.7911866017341727}, {'training_time': 981.9522340297699, 'testing_time': 2.5840580463409424, 'accuracy': 0.7934562760261749}, {'training_time': 981.7292790412903, 'testing_time': 2.6102259159088135, 'accuracy': 0.7936072514759377}, {'training_time': 982.3257429599762, 'testing_time': 2.52850079536438, 'accuracy': 0.7909395170929955}, {'training_time': 982.3015880584717, 'testing_time': 2.5189759731292725, 'accuracy': 0.7949455024553839}, {'training_time': 982.6777019500732, 'testing_time': 2.5490550994873047, 'accuracy': 0.7931096572834764}]}

real    10093,00s
user    8650,40s
sys    1173,75s
