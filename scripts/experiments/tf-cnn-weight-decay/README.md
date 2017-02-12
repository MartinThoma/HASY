model_checkpoint_path: checkpoints/hasy_tf-cnn-relu-weight-decay_model.ckpt
validation_curve_path: validation-curves/validation-curve-accuracy-tf-cnn-relu-weight-decay-2.csv
Evaluate model
(16945, 1024)
tf-cnn-relu-weight-decay:
    train_time: 1741.7 (min=1741.48, max=1741.94)
    test_time:  2.9 (min=2.91, max=2.92)
    acc:        78.8 (min=78.7, max=78.8)
{'tf-cnn-relu-weight-decay': [{'training_time': 1741.9421598911285, 'testing_time': 2.924149990081787, 'accuracy': 0.7874293785310734}, {'training_time': 1741.4842150211334, 'testing_time': 2.906607151031494, 'accuracy': 0.7880790793744468}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX TITAN Black, pci bus id: 0000:01:00.0)
    shape: (3, 3, 1, 32)
    variable_parametes: 288
    ---
    shape: (32,)
    variable_parametes: 32
    ---
    shape: (3, 3, 32, 64)
    variable_parametes: 18432
    ---
    shape: (64,)
    variable_parametes: 64
    ---
    shape: (4096, 1024)
    variable_parametes: 4194304
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
total_parameters: 4592369
model_checkpoint_path: checkpoints/hasy_tf-cnn-relu-weight-decay_model.ckpt
validation_curve_path: validation-curves/validation-curve-accuracy-tf-cnn-relu-weight-decay-3.csv
^CTraceback (most recent call last):
  File "./tf_hasy.py", line 178, in <module>
    hasy, correct_prediction, i)
  File "./tf_hasy.py", line 59, in log_score
    "train")
  File "./tf_hasy.py", line 49, in eval_network
    test_correct = correct_prediction.eval(feed_dict=feed_dict)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/ops.py", line 575, in eval
    return _eval_using_default_session(self, feed_dict, self.graph, session)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/framework/ops.py", line 3633, in _eval_using_default_session
    return session.run(tensors, feed_dict)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.py", line 766, in run
    run_metadata_ptr)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.py", line 964, in _run
    feed_dict_string, options, run_metadata)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.py", line 1014, in _do_run
    target_list, options, run_metadata)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.py", line 1021, in _do_call
    return fn(*args)
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/client/session.py", line 1003, in _run_fn
    status, run_metadata)
KeyboardInterrupt

real    4838,97s
user    4774,69s
sys 464,93s
