import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#純量
x1 = tf.placeholder(tf.float32, shape=None)
y1 = tf.placeholder(tf.float32, shape=None)

r1 = x1 + y1

#矩陣                                 兩個 每個裡面一個
x2 = tf.placeholder(tf.float32, shape=[2, 1])
y2 = tf.placeholder(tf.float32, shape=[1, 2])

r2 = tf.matmul(x2, y2)


with tf.Session() as sess:
    #只跑一個operation
    r1_value = sess.run(r1, feed_dict={x1: 4, y1: 8})
    #跑多個
    r1_value, r2_value = sess.run(
        [r1, r2],
        feed_dict={
            x1: 5, y1: 6,
            x2: [[2], [2]], y2: [[3, 3]]
        })
    print (r1_value)
    print (r2_value)

    
   
