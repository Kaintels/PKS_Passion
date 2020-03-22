from silence_tensorflow import silence_tensorflow
silence_tensorflow()
import tensorflow as tf
import numpy as np
from warnings import filterwarnings
import os
filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]

w = tf.Variable(2.0)
b = tf.Variable(0.5)

lr = 0.01

print("     i       w      b        cost")
for i in range(100+1):
    with tf.GradientTape() as tape:
        h = w * x_data + b
        cost = tf.reduce_mean(tf.square(h - y_data))

    w_grad, b_grad = tape.gradient(cost, [w, b])
    w.assign_sub(lr * w_grad)
    b.assign_sub(lr * b_grad)
    if i % 10 == 0:
        print("{:5}|{:10.4f}|{:10.4f}|{:10.6f}".format(i, w.numpy(), b.numpy(), cost))