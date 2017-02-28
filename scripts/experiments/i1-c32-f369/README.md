Evaluate model
i1-c32-f369:
    train_time:    6434.4 (min=6434.43, max=6434.43)
    test_time:    3.9 (min=3.86, max=3.86)
    acc:        68.5 (min=68.5, max=68.5)
{'i1-c32-f369': [{'training_time': 6434.434569120407, 'testing_time': 3.863692045211792, 'accuracy': 0.6848516949152542}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (3, 3, 1, 32)
    variable_parametes: 288
    ---
    shape: (32,)
    variable_parametes: 32
    ---
    shape: (32768, 369)
    variable_parametes: 12091392
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 12092081
model_checkpoint_path: checkpoints/hasy_i1-c32-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-f369-1.csv
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

real    8713,57s
user    6403,82s
sys    1346,92s
