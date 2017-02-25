    shape: (3, 3, 1, 3)
    variable_parametes: 27
    ---
    shape: (3,)
    variable_parametes: 3
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
total_parameters: 1427855
model_checkpoint_path: checkpoints/hasy_i3-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i3-f1024-f369-9.csv
Evaluate model
i3-f1024-f369:
    train_time:    258.3 (min=255.70, max=261.80)
    test_time:    1.3 (min=1.24, max=1.40)
    acc:        62.8 (min=62.2, max=63.4)
{'i3-f1024-f369': [{'training_time': 261.80369901657104, 'testing_time': 1.2494940757751465, 'accuracy': 0.6338865348399246}, {'training_time': 257.50035405158997, 'testing_time': 1.2786400318145752, 'accuracy': 0.6335792269105931}, {'training_time': 257.15393900871277, 'testing_time': 1.2991249561309814, 'accuracy': 0.633891089694318}, {'training_time': 256.44603300094604, 'testing_time': 1.2502667903900146, 'accuracy': 0.6260148148148148}, {'training_time': 255.69913816452026, 'testing_time': 1.252737045288086, 'accuracy': 0.6220453735598052}, {'training_time': 260.51990699768066, 'testing_time': 1.2924468517303467, 'accuracy': 0.6242712671029149}, {'training_time': 261.022155046463, 'testing_time': 1.4002649784088135, 'accuracy': 0.6260957719601646}, {'training_time': 258.5351469516754, 'testing_time': 1.2534339427947998, 'accuracy': 0.6286158259622281}, {'training_time': 256.29395294189453, 'testing_time': 1.23884916305542, 'accuracy': 0.6245059288537549}, {'training_time': 257.91274905204773, 'testing_time': 1.2646799087524414, 'accuracy': 0.6224716403577216}]}

real    2847,60s
user    3139,42s
sys    534,88s
