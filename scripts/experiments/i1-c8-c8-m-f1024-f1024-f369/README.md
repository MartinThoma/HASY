Evaluate model
i1-c8-c8-m-f1024-f1024-f369:
    Runs:    1
    train_time:    4101.0 (min=4101.01, max=4101.01)
    test_time:    3.2 (min=3.24, max=3.24)
    acc:        79.8 (min=79.8, max=79.8)
{'i1-c8-c8-m-f1024-f1024-f369': [{'training_time': 4101.007228136063, 'testing_time': 3.242034912109375, 'accuracy': 0.7977283427495292}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (3, 3, 1, 8)
    variable_parametes: 72
    ---
    shape: (8,)
    variable_parametes: 8
    ---
    shape: (3, 3, 8, 8)
    variable_parametes: 576
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
total_parameters: 3526665
model_checkpoint_path: checkpoints/hasy_i1-c8-c8-m-f1024-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c8-c8-m-f1024-f1024-f369-1.csv
^CTraceback (most recent call last):
  File "tf_hasy.py", line 165, in <module>
    hasy, correct_prediction, i)
  File "tf_hasy.py", line 44, in log_score
    "train")
  File "tf_hasy.py", line 34, in eval_network
    test_correct = correct_prediction.eval(feed_dict=feed_dict)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/ops.py", line 581, in eval
    return _eval_using_default_session(self, feed_dict, self.graph, session)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/ops.py", line 3797, in _eval_using_default_session
    return session.run(tensors, feed_dict)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.py", line 767, in run
    run_metadata_ptr)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.py", line 965, in _run
    feed_dict_string, options, run_metadata)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.py", line 1015, in _do_run
    target_list, options, run_metadata)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.py", line 1022, in _do_call
    return fn(*args)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.py", line 1004, in _run_fn
    status, run_metadata)
KeyboardInterrupt
su
real    4650,76s
user    3543,60s
sys    709,50s
