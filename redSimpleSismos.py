import lector
datas = lector.Cargador()

import tensorflow as tf
x = tf.placeholder("float", [None, 9])
W = tf.Variable(tf.zeros([9,95]))
b = tf.Variable(tf.zeros([95]))
matm=tf.matmul(x,W)
y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder("float", [None,95])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
sess = tf.Session()
sess.run(tf.initialize_all_variables())
for i in range(1000):
 batch_xs, batch_ys = datas.randomTest(100)
 sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
 correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
 accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
 print sess.run(accuracy, feed_dict={x: datas.trainDatas(), y_: datas.trainLabels()})