Evaluate model
i1-c32-f369:
    train_time:    2062.6 (min=2062.57, max=2062.57)
    test_time:    3.8 (min=3.81, max=3.81)
    acc:        68.9 (min=68.9, max=68.9)
{'i1-c32-f369': [{'training_time': 2062.572835922241, 'testing_time': 3.8098950386047363, 'accuracy': 0.6893832391713748}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (32, 32, 1, 3)
    variable_parametes: 3072
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
total_parameters: 1137012
model_checkpoint_path: checkpoints/hasy_i1-c32-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-f369-1.csv
^CTraceback (most recent call last):
  File "tf_hasy.py", line 138, in <module>
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

real    2484,32s
user    1910,14s
sys    383,82s
