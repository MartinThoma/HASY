Evaluate model
i1-c32-c32-f369:
    train_time:    1844.3 (min=1819.72, max=1856.94)
    test_time:    2.3 (min=2.27, max=2.35)
    acc:        72.5 (min=70.7, max=73.4)
{'i1-c32-c32-f369': [{'training_time': 1819.7227370738983, 'testing_time': 2.3501009941101074, 'accuracy': 0.7311087570621468}, {'training_time': 1856.9359118938446, 'testing_time': 2.3178608417510986, 'accuracy': 0.733726763056949}, {'training_time': 1852.2989590168, 'testing_time': 2.318290948867798, 'accuracy': 0.733163838467451}, {'training_time': 1843.5788009166718, 'testing_time': 2.2962470054626465, 'accuracy': 0.7246814814814815}, {'training_time': 1843.0347309112549, 'testing_time': 2.300877809524536, 'accuracy': 0.7278180306449697}, {'training_time': 1844.2575681209564, 'testing_time': 2.274635076522827, 'accuracy': 0.7157644259369423}, {'training_time': 1839.9413290023804, 'testing_time': 2.3324198722839355, 'accuracy': 0.7243127198998152}, {'training_time': 1845.1928730010986, 'testing_time': 2.3476669788360596, 'accuracy': 0.7066698541716472}, {'training_time': 1854.0218391418457, 'testing_time': 2.2779219150543213, 'accuracy': 0.7264941909210684}]}
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
    shape: (32768, 369)
    variable_parametes: 12091392
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 12101329
model_checkpoint_path: checkpoints/hasy_i1-c32-c32-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-c32-f369-9.csv
Evaluate model
i1-c32-c32-f369:
    train_time:    1845.3 (min=1819.72, max=1856.94)
    test_time:    2.3 (min=2.27, max=2.35)
    acc:        72.5 (min=70.7, max=73.4)
{'i1-c32-c32-f369': [{'training_time': 1819.7227370738983, 'testing_time': 2.3501009941101074, 'accuracy': 0.7311087570621468}, {'training_time': 1856.9359118938446, 'testing_time': 2.3178608417510986, 'accuracy': 0.733726763056949}, {'training_time': 1852.2989590168, 'testing_time': 2.318290948867798, 'accuracy': 0.733163838467451}, {'training_time': 1843.5788009166718, 'testing_time': 2.2962470054626465, 'accuracy': 0.7246814814814815}, {'training_time': 1843.0347309112549, 'testing_time': 2.300877809524536, 'accuracy': 0.7278180306449697}, {'training_time': 1844.2575681209564, 'testing_time': 2.274635076522827, 'accuracy': 0.7157644259369423}, {'training_time': 1839.9413290023804, 'testing_time': 2.3324198722839355, 'accuracy': 0.7243127198998152}, {'training_time': 1845.1928730010986, 'testing_time': 2.3476669788360596, 'accuracy': 0.7066698541716472}, {'training_time': 1854.0218391418457, 'testing_time': 2.2779219150543213, 'accuracy': 0.7264941909210684}, {'training_time': 1853.8000240325928, 'testing_time': 2.317633867263794, 'accuracy': 0.7312286177300282}]}

real    18748,46s
user    15021,00s
sys    2087,99s