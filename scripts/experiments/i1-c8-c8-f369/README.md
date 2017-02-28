Evaluate model
i1-c8-c8-f369:
    train_time:    3387.1 (min=3387.13, max=3387.13)
    test_time:    2.9 (min=2.94, max=2.94)
    acc:        69.4 (min=69.4, max=69.4)
{'i1-c8-c8-f369': [{'training_time': 3387.1334969997406, 'testing_time': 2.9411799907684326, 'accuracy': 0.6940913370998116}]}
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
    shape: (8192, 369)
    variable_parametes: 3022848
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 3023881
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
s
real    3666,70s
user    2787,22s
sys    553,19s