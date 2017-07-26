import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

def add_layer(inputs, in_size, out_size, activation_function=None):
    W = tf.Variable(tf.random_normal([in_size, out_size]))
    b = tf.Variable(tf.zeros([1, out_size]) + 0.1)  #推薦不要為零
    y = tf.matmul(inputs, W) + b  #還沒被激活的值

    if activation_function is None:
            outputs = y
    else:
        outputs = activation_function(y)
    return outputs

#create data        之間  個位置        增加維度
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)  #mean=0, std=0.05, 形狀同x_data
y_data = np.square(x_data)-0.5 + noise

#第一層 一個輸入 十個隱藏神經元 一個輸出
xs = tf.placeholder(tf.float32, [None ,1])  #因為x_data的屬性只有1 
ys = tf.placeholder(tf.float32, [None, 1])
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
prediction = add_layer(l1, 10, 1, activation_function=None)
#                                                       
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                                    reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#important part
init = tf.global_variables_initializer()

sess = tf.Session() 
sess.run(init)


#plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion() #連續畫
#plt.show() #只畫一次

for i in range(10000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0 :
        #print(sess.run(loss, feed_dict={xs:x_data, ys:y_data})) #只要有經過placeholde就要feed dict
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs:x_data})
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5) #要連續就要把前一條刪掉
        
        plt.pause(0.1)
        
