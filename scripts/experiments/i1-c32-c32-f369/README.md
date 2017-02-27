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
    shape: (32768, 369)
    variable_parametes: 12091392
    ---
    shape: (369,)
    variable_parametes: 369
    ---
total_parameters: 12101329
model_checkpoint_path: checkpoints/hasy_i1-c32-c32-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-c32-f369.csv
W tensorflow/core/common_runtime/bfc_allocator.cc:217] Ran out of memory trying to allocate 1.10GiB. The caller indicates that this is not a failure, but may mean that there could be performance gains if more memory is available.
W tensorflow/core/common_runtime/bfc_allocator.cc:217] Ran out of memory trying to allocate 1.04GiB. The caller indicates that this is not a failure, but may mean that there could be performance gains if more memory is available.
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

real    1089,02s
user    792,58s
sys    153,00s
