Evaluate model
i1-c8-m-f1024-f1024-f369-batch-64:
    Runs:    2
    train_time:    3733.7 (min=3708.76, max=3758.73)
    test_time:    4.7 (min=4.67, max=4.74)
    acc:        76.7 (min=74.0, max=79.3)
{'i1-c8-m-f1024-f1024-f369-batch-64': [{'training_time': 3708.7623579502106, 'testing_time': 4.673012018203735, 'accuracy': 0.740171845574388}, {'training_time': 3758.7329881191254, 'testing_time': 4.73507285118103, 'accuracy': 0.7932133372676305}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (3, 3, 1, 8)
    variable_parametes: 72
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
total_parameters: 3526081
model_checkpoint_path: checkpoints/hasy_i1-c8-m-f1024-f1024-f369-batch-64_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c8-m-f1024-f1024-f369-batch-64-2.csv
^CTraceback (most recent call last):
  File "tf_hasy.py", line 161, in <module>
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

real    7698,42s
user    6365,21s
sys    1324,62s
