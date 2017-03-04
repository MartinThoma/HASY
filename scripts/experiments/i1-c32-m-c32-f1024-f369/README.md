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
    shape: (8192, 1024)
    variable_parametes: 8388608
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
total_parameters: 8777425
model_checkpoint_path: checkpoints/hasy_i1-c32-m-c32-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-m-c32-f1024-f369-9.csv
Evaluate model
i1-c32-m-c32-f1024-f369:
    train_time:    1129.3 (min=1100.77, max=1144.90)
    test_time:    2.2 (min=2.12, max=2.24)
    acc:        79.1 (min=78.5, max=79.6)
{'i1-c32-m-c32-f1024-f369': [{'training_time': 1100.773561000824, 'testing_time': 2.2001869678497314, 'accuracy': 0.7929025423728814}, {'training_time': 1120.703742980957, 'testing_time': 2.1214139461517334, 'accuracy': 0.7952198288580702}, {'training_time': 1126.9990420341492, 'testing_time': 2.1797380447387695, 'accuracy': 0.7935907290250104}, {'training_time': 1123.9655830860138, 'testing_time': 2.237478017807007, 'accuracy': 0.7905185185185185}, {'training_time': 1131.3201270103455, 'testing_time': 2.2216758728027344, 'accuracy': 0.7878014015916379}, {'training_time': 1133.479824066162, 'testing_time': 2.136320114135742, 'accuracy': 0.7892920880428317}, {'training_time': 1144.898192167282, 'testing_time': 2.138895034790039, 'accuracy': 0.7958733377064822}, {'training_time': 1144.2502200603485, 'testing_time': 2.210908889770508, 'accuracy': 0.7851422424097537}, {'training_time': 1135.537250995636, 'testing_time': 2.1173930168151855, 'accuracy': 0.7915918074020841}, {'training_time': 1131.497311115265, 'testing_time': 2.13188099861145, 'accuracy': 0.7908889022267571}]}

real    11587,74s
user    9709,22s
sys    1322,66s
