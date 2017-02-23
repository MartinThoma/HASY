    shape: (32, 32, 1, 3)
    variable_parametes: 3072
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (1024, 369)
    variable_parametes: 377856
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 381300
model_checkpoint_path: checkpoints/hasy_i3-c32-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i3-c32-f369-9.csv
Evaluate model
i3-c32-f369:
    train_time: 854.9 (min=820.29, max=916.85)
    test_time:  1.3 (min=1.24, max=1.34)
    acc:        43.0 (min=40.1, max=44.9)
{'i3-c32-f369': [{'training_time': 885.5917661190033, 'testing_time': 1.3365821838378906, 'accuracy': 0.400894538606403}, {'training_time': 859.1452760696411, 'testing_time': 1.3134779930114746, 'accuracy': 0.4384184125110652}, {'training_time': 856.6606829166412, 'testing_time': 1.3052690029144287, 'accuracy': 0.4350499615680246}, {'training_time': 841.9807360172272, 'testing_time': 1.2947769165039062, 'accuracy': 0.4318222222222222}, {'training_time': 820.2871210575104, 'testing_time': 1.2394189834594727, 'accuracy': 0.44880627152868513}, {'training_time': 874.8119258880615, 'testing_time': 1.2723770141601562, 'accuracy': 0.41540749553837003}, {'training_time': 916.8540351390839, 'testing_time': 1.322195053100586, 'accuracy': 0.4109368477547856}, {'training_time': 827.4725179672241, 'testing_time': 1.3355348110198975, 'accuracy': 0.445792493425771}, {'training_time': 832.0409519672394, 'testing_time': 1.2723259925842285, 'accuracy': 0.44418493232722484}, {'training_time': 834.3242089748383, 'testing_time': 1.3330860137939453, 'accuracy': 0.43322729728107556}]}

real    8814,68s
user    83605,26s
sys 986,70s
