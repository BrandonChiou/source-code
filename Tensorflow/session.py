import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

m1 = tf.constant([[3,3]])
m2 = tf.constant([[2],[2]])

product = tf.matmul(m1, m2)

with tf.Session() as sess:
	result_ = sess.run(product)
	print (result_)