## Prerequisite

1. TensorFlow 1.2

2. Opencv3 (Not a must, used to [read images](https://github.com/watsonyanghx/CNN_LSTM_CTC_Tensorflow/blob/master/utils.py#L66)).

3. Numpy


## How to run

python3.6 main.py --train_lst=train.txt --image_height=60 --image_width=180 -image_channel=1 --max_stepsize=64 --num_hidden=128 --log_dir=./log/train --num_gpus=1 --mode=train --val_dir=val.txt

python ./main.py --infer_dir=./imgs/infer/ \
                 --checkpoint_dir=./checkpoint/ \
                 --num_gpus=0 \
                 --mode=infer

``` shell
# make sure the data path is correct, have a look at helper.py.

python helper.py
```

