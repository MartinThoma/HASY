Evaluate model
i1-c8-c8-f369:
    train_time:    3974.4 (min=3974.43, max=3974.43)
    test_time:    3.6 (min=3.57, max=3.57)
    acc:        72.8 (min=72.8, max=72.8)
{'i1-c8-c8-f369': [{'training_time': 3974.4325120449066, 'testing_time': 3.566685914993286, 'accuracy': 0.7283427495291902}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (8, 8, 1, 3)
    variable_parametes: 192
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (8, 8, 3, 3)
    variable_parametes: 576
    ---
    shape: (3,)
    variable_parametes: 3
    ---
    shape: (3072, 369)
    variable_parametes: 1133568
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 1134711
model_checkpoint_path: checkpoints/hasy_i1-c8-c8-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c8-c8-f369-1.csv
^CTraceback (most recent call last):
  File "tf_hasy.py", line 146, in <module>
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

real    4152,10s
user    3168,54s
sys    628,42s
