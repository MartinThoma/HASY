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
total_parameters: 406289
model_checkpoint_path: checkpoints/hasy_i1-c32-c32-m-c32-c32-f369_model.ckpt
validation_curve_path: validation-curve-accuracy-i1-c32-c32-m-c32-c32-f369.csv
Evaluate model
i1-c32-c32-m-c32-c32-f369:
    train_time:    1058.8 (min=1058.85, max=1058.85)
    test_time:    1.5 (min=1.50, max=1.50)
    acc:        64.1 (min=64.1, max=64.1)
{'i1-c32-c32-m-c32-c32-f369': [{'training_time': 1058.8490281105042, 'testing_time': 1.495779037475586, 'accuracy': 0.641066384180791}]}
^CTraceback (most recent call last):
  File "tf_hasy.py", line 74, in <module>
    one_hot=True)
  File "/home/moose/GitHub/HASY/scripts/input_data.py", line 132, in read_data_sets
    symbol_id2index)
  File "/home/moose/GitHub/HASY/scripts/hasy_tools.py", line 136, in load_images
    mode='L')
  File "/home/moose/.local/lib/python2.7/site-packages/scipy/ndimage/io.py", line 24, in imread
    return _imread(fname, flatten, mode)
  File "/home/moose/.local/lib/python2.7/site-packages/scipy/misc/pilutil.py", line 154, in imread
    im = Image.open(name)
  File "/usr/local/lib/python2.7/dist-packages/PIL/Image.py", line 2339, in open
    im = _open_core(fp, filename, prefix)
  File "/usr/local/lib/python2.7/dist-packages/PIL/Image.py", line 2329, in _open_core
    im = factory(fp, filename)
  File "/usr/local/lib/python2.7/dist-packages/PIL/ImageFile.py", line 87, in __init__
    if isPath(fp):
  File "/usr/local/lib/python2.7/dist-packages/PIL/_util.py", line 8, in isPath
    return isinstance(f, basestring)
KeyboardInterrupt

real    1134,82s
user    1056,80s
sys    181,18s
