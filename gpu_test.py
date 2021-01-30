#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: yangcheng
# license: © 2011-2019 The Authors. All Rights Reserved.
# contact: yangcheng@zuzuche.com
# time: 2020/6/1 15:38
# desc:
# ======================================================

import tensorflow as tf

x = tf.random.uniform([3, 3])

print("Is there a GPU available: ")
print(tf.config.experimental.list_physical_devices("GPU"))

print("Is the Tensor on GPU #0:  ")
print(x.device.endswith('GPU:0'))