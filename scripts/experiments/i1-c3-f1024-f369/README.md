Evaluate model
i3-c3-f1024-f369:
    train_time:    5941.0 (min=5941.00, max=5941.00)
    test_time:    2.6 (min=2.57, max=2.57)
    acc:        77.7 (min=77.7, max=77.7)
{'i3-c3-f1024-f369': [{'training_time': 5941.004289865494, 'testing_time': 2.568735122680664, 'accuracy': 0.7774835216572504}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (3, 3, 1, 3)
    variable_parametes: 27
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (3, 3, 3, 3)
    variable_parametes: 81
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (3072, 1024)
    variable_parametes: 3145728
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
total_parameters: 3525091
model_checkpoint_path: checkpoints/hasy_i3-c3-f1024-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i3-c3-f1024-f369-1.csv
^CTraceback (most recent call last):
  File "tf_hasy.py", line 152, in <module>
    y_: batch[1]
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/ops.py", line 1588, in run
    _run_using_default_session(self, feed_dict, self.graph, session)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/ops.py", line 3832, in _run_using_default_session
    session.run(operation, feed_dict)
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

real    6043,65s
user    4856,13s
sys    962,66s
