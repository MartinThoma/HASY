Evaluate model
i1-c16-f369:
    train_time:    3085.4 (min=3085.41, max=3085.41)
    test_time:    4.5 (min=4.53, max=4.53)
    acc:        68.2 (min=68.2, max=68.2)
{'i1-c16-f369': [{'training_time': 3085.4126200675964, 'testing_time': 4.529749870300293, 'accuracy': 0.682144538606403}]}
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce 940MX, pci bus id: 0000:02:00.0)
    shape: (16, 16, 1, 3)
    variable_parametes: 768
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
total_parameters: 1134708
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

real    3762,37s
user    2848,64s
sys    507,01s
