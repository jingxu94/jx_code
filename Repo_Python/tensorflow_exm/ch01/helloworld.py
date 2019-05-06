# @Time : 2018/3/16 22:25 
# @Author : Jing Xu


import tensorflow as tf

hello = tf.constant("Hello, TensorFlow Example!")

sess = tf.Session()

print(sess.run(hello))