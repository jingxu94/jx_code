#__author:  "Jing Xu"
#date:  2018/2/8

import tensorflow as tf

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")
result = tf.add(a, b, name="add")
# TensorFlow运行模型--会话：第一种模式需要明确调用会话生成函数和关闭会话函数
sess = tf.Session()
c = sess.run(result)
sess.close()
print(c)

with tf.Session() as sess1:
	d = sess1.run(result)
print(d)

sess2 = tf.Session()
with sess2.as_default():
	print(result.eval())

sess3 = tf.InteractiveSession()
print(result.eval())
sess3.close()

# config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)
# sess4 = tf.InteractiveSession(config=config)
# sess5 = tf.Session(config=config)
