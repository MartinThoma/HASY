Evaluate model
i1-c3-c3-c3-m-c3-f369:
    train_time:    4371.1 (min=4371.08, max=4371.08)
    test_time:    4.0 (min=4.00, max=4.00)
    acc:        74.3 (min=74.3, max=74.3)
{'i1-c3-c3-c3-m-c3-f369': [{'training_time': 4371.08199596405, 'testing_time': 4.000731945037842, 'accuracy': 0.7432909604519774}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (3, 3, 1, 3)
    variable_parametes: 27
    ---
    shape: (3,)
    variable_parametes: 3
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
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (3, 3, 3, 3)
    variable_parametes: 81
    ---
    shape: (3,)
    variable_parametes: 3
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
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (768, 369)
    variable_parametes: 283392
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 284055
model_checkpoint_path: checkpoints/hasy_i1-c3-c3-c3-m-c3-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c3-c3-c3-m-c3-f369-1.csv
^CTraceback (most recent call last):
  File "tf_hasy.py", line 173, in <module>
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

real    4771,36s
user    3637,33s
sys    713,60s