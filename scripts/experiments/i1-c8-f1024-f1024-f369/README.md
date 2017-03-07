I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX TITAN Black, pci bus id: 0000:01:00.0)
    shape: (3, 3, 1, 8)
    variable_parametes: 72
    ---
    shape: (8,)
    variable_parametes: 8
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
total_parameters: 9817537
model_checkpoint_path: checkpoints/hasy_i1-c8-f1024-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c8-f1024-f1024-f369-9.csv
Evaluate model
i1-c8-f1024-f1024-f369:
    Runs:    10
    train_time:    784.5 (min=770.45, max=793.95)
    test_time:    1.9 (min=1.90, max=1.95)
    acc:        78.0 (min=77.5, max=78.8)
{'i1-c8-f1024-f1024-f369': [{'training_time': 770.4507038593292, 'testing_time': 1.9542319774627686, 'accuracy': 0.7851341807909604}, {'training_time': 781.6293358802795, 'testing_time': 1.949517011642456, 'accuracy': 0.7884331661257008}, {'training_time': 786.2117340564728, 'testing_time': 1.9351708889007568, 'accuracy': 0.7840714243481346}, {'training_time': 781.8115530014038, 'testing_time': 1.9429500102996826, 'accuracy': 0.7787259259259259}, {'training_time': 793.9504270553589, 'testing_time': 1.9403600692749023, 'accuracy': 0.7754483905451954}, {'training_time': 784.8968150615692, 'testing_time': 1.925264835357666, 'accuracy': 0.7775133848899465}, {'training_time': 791.2668249607086, 'testing_time': 1.9481449127197266, 'accuracy': 0.7747033216053432}, {'training_time': 782.9372718334198, 'testing_time': 1.9304308891296387, 'accuracy': 0.7795242648816639}, {'training_time': 792.1279191970825, 'testing_time': 1.9267749786376953, 'accuracy': 0.7784165768355492}, {'training_time': 779.9533641338348, 'testing_time': 1.9021809101104736, 'accuracy': 0.7768441270031811}]}

real    8096,95s
user    7063,22s
sys    959,18s
