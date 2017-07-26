from __future__ import print_function
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


#create random data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

#tf structure building
Weights = tf.Variable(tf.random_normal([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

sess = tf.Session()
#initiate all
init = tf.global_variables_initializer()
sess.run(init)    #the most important part

#run
for step in range(1000):
	sess.run(train_step)
	if step % 50 == 0:
		print (step, sess.run(Weights), sess.run(biases))
		
