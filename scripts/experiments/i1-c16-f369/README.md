Evaluate model
i1-c16-f369:
    train_time:    3249.9 (min=3249.92, max=3249.92)
    test_time:    2.6 (min=2.60, max=2.60)
    acc:        67.1 (min=67.1, max=67.1)
{'i1-c16-f369': [{'training_time': 3249.9200780391693, 'testing_time': 2.5992910861968994, 'accuracy': 0.6711982109227872}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (3, 3, 1, 16)
    variable_parametes: 144
    ---
    shape: (16,)
    variable_parametes: 16
    ---
    shape: (16384, 369)
    variable_parametes: 6045696
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 6046225
model_checkpoint_path: checkpoints/hasy_i1-c16-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c16-f369-1.csv
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

real    4326,88s
user    3316,37s
sys    659,08s
