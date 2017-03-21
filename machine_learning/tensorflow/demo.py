#!/usr/bin/env python

import tensorflow as tf

sess = tf.Session()
a = tf.constant(10)
b = tf.constant(20)
print sess.run(a + b)
