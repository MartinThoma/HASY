Evaluate model
i1-c32-c32-m-c32-f369:
    train_time:    994.8 (min=979.06, max=1015.85)
    test_time:    1.5 (min=1.34, max=1.65)
    acc:        64.1 (min=63.8, max=64.3)
{'i1-c32-c32-m-c32-f369': [{'training_time': 979.0589189529419, 'testing_time': 1.5738599300384521, 'accuracy': 0.6411252354048964}, {'training_time': 991.5358200073242, 'testing_time': 1.3389251232147217, 'accuracy': 0.6434346414871643}, {'training_time': 992.644280910492, 'testing_time': 1.650771141052246, 'accuracy': 0.6432921421391828}, {'training_time': 1015.8491230010986, 'testing_time': 1.6151771545410156, 'accuracy': 0.6377481481481482}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (3, 3, 1, 32)
    variable_parametes: 288
    ---
    shape: (32,)
    variable_parametes: 32
    ---
    shape: (3, 3, 32, 32)
    variable_parametes: 9216
    ---
    shape: (32,)
    variable_parametes: 32
    ---
    shape: (3, 3, 32, 32)
    variable_parametes: 9216
    ---
    shape: (32,)
    variable_parametes: 32
    ---
    shape: (1024, 369)
    variable_parametes: 377856
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 397041
model_checkpoint_path: checkpoints/hasy_i1-c32-c32-m-c32-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-c32-m-c32-f369-4.csv
^CTraceback (most recent call last):
  File "tf_hasy.py", line 155, in <module>
    hasy, correct_prediction, i)
  File "tf_hasy.py", line 46, in log_score
    "test")
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

real    4496,56s
user    4188,62s
sys    707,26s
