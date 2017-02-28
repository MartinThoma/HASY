Evaluate model
i1-c8-f369:
    train_time:    1800.3 (min=1800.29, max=1800.29)
    test_time:    1.8 (min=1.84, max=1.84)
    acc:        66.8 (min=66.8, max=66.8)
{'i1-c8-f369': [{'training_time': 1800.287572145462, 'testing_time': 1.8400452136993408, 'accuracy': 0.6682556497175142}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (8, 8, 1, 3)
    variable_parametes: 192
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
total_parameters: 1134132
model_checkpoint_path: checkpoints/hasy_i1-c8-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c8-f369-1.csv
^CTraceback (most recent call last):
  File "tf_hasy.py", line 140, in <module>
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

real    1997,00s
user    1640,68s
sys    298,14s
