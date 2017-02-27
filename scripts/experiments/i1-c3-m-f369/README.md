Evaluate model
i1-c3-m-f369:
    train_time:    694.0 (min=651.70, max=724.29)
    test_time:    2.0 (min=1.65, max=2.80)
    acc:        54.9 (min=54.5, max=55.6)
{'i1-c3-m-f369': [{'training_time': 664.5655269622803, 'testing_time': 2.7999751567840576, 'accuracy': 0.550376647834275}, {'training_time': 667.5361440181732, 'testing_time': 2.015876054763794, 'accuracy': 0.5563293006786663}, {'training_time': 722.4725329875946, 'testing_time': 2.0145809650421143, 'accuracy': 0.5519422929107787}, {'training_time': 706.056343793869, 'testing_time': 1.653944969177246, 'accuracy': 0.5469037037037037}, {'training_time': 723.9421689510345, 'testing_time': 2.020960807800293, 'accuracy': 0.544898443995724}, {'training_time': 664.0689470767975, 'testing_time': 1.6848468780517578, 'accuracy': 0.5477096966091612}, {'training_time': 651.6989870071411, 'testing_time': 1.9888949394226074, 'accuracy': 0.5484525016399309}, {'training_time': 721.0904111862183, 'testing_time': 1.9830060005187988, 'accuracy': 0.5491871862299785}, {'training_time': 724.290235042572, 'testing_time': 1.9198927879333496, 'accuracy': 0.5469517307461972}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (3, 3, 1, 3)
    variable_parametes: 27
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (768, 369)
    variable_parametes: 283392
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 283791
