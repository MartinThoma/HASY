I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX TITAN Black, pci bus id: 0000:01:00.0)
    shape: (3, 3, 1, 32)
    variable_parametes: 288
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
    shape: (4096, 1024)
    variable_parametes: 4194304
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
total_parameters: 4592369
model_checkpoint_path: checkpoints/hasy_tf-cnn-relu_model.ckpt
validation_curve_path: validation-curves/validation-curve-accuracy-tf-cnn-relu-10.csv
Evaluate model
(16661, 1024)
tf-cnn-relu:
    train_time: 1749.4 (min=1736.00, max=1753.90)
    test_time:  2.9 (min=2.82, max=2.94)
    acc:        78.1 (min=77.2, max=78.6)
{'tf-cnn-relu': [{'training_time': 1736.0045192241669, 'testing_time': 2.913490056991577, 'accuracy': 0.7864289077212806}, {'training_time': 1748.2647750377655, 'testing_time': 2.891223907470703, 'accuracy': 0.7854824431985836}, {'training_time': 1750.905138015747, 'testing_time': 2.9194350242614746, 'accuracy': 0.7845444332761781}, {'training_time': 1751.3890450000763, 'testing_time': 2.8845691680908203, 'accuracy': 0.7821037037037037}, {'training_time': 1751.788318157196, 'testing_time': 2.8665521144866943, 'accuracy': 0.7853664330680603}, {'training_time': 1750.928134918213, 'testing_time': 2.8873870372772217, 'accuracy': 0.7823319452706722}, {'training_time': 1753.89679479599, 'testing_time': 2.929692029953003, 'accuracy': 0.7765519708986821}, {'training_time': 1753.3940169811249, 'testing_time': 2.9446418285369873, 'accuracy': 0.7789863734162085}, {'training_time': 1748.415538072586, 'testing_time': 2.8176820278167725, 'accuracy': 0.7806922984788598}, {'training_time': 1748.84761095047, 'testing_time': 2.8899190425872803, 'accuracy': 0.7721025148550508}]}

real    17859,42s
user    17581,12s
sys 1695,28s
