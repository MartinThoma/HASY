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
    train_time:    977.3 (min=964.12, max=982.97)
    test_time:    2.5 (min=2.51, max=2.61)
    acc:        80.4 (min=80.0, max=81.0)
{'i1-c32-m-f1024-d0.5-f1024-d0.5-f369': [{'training_time': 964.1195380687714, 'testing_time': 2.5716001987457275, 'accuracy': 0.8074976459510358}, {'training_time': 982.0585088729858, 'testing_time': 2.5793488025665283, 'accuracy': 0.8096783712009442}, {'training_time': 975.2040770053864, 'testing_time': 2.5308220386505127, 'accuracy': 0.8051203216460711}, {'training_time': 976.3920481204987, 'testing_time': 2.5159199237823486, 'accuracy': 0.8061037037037037}, {'training_time': 977.7679040431976, 'testing_time': 2.524982213973999, 'accuracy': 0.7997980757809716}, {'training_time': 978.5226690769196, 'testing_time': 2.553678035736084, 'accuracy': 0.8049375371802499}, {'training_time': 982.9693419933319, 'testing_time': 2.614657163619995, 'accuracy': 0.8007633132566044}, {'training_time': 979.8103759288788, 'testing_time': 2.531787872314453, 'accuracy': 0.8037293808271575}, {'training_time': 979.300194978714, 'testing_time': 2.5059900283813477, 'accuracy': 0.8014732303269853}, {'training_time': 977.1249921321869, 'testing_time': 2.5647671222686768, 'accuracy': 0.8019926775103535}]}

real    10058,18s
user    8587,72s
sys    1174,46s
