#__author:  "Jing Xu"
#date:  2018/2/9

import tensorflow as tf

v1 = tf.constant([1.0, 2.0, 3.0, 4.0])
v2 = tf.constant([4.0, 3.0, 2.0, 1.0])

sess = tf.InteractiveSession()
# tf.greater的输入是两个张量，此函数会比较这两个输入张量中每一个元素的大小，并返回比较结果
# tf.where替换旧版本tf.select，该函数有三个参数，第一个为选择条件依据，当选择条件为True时，选择第二个参数中的值，否则使用第三个参数中的值
print(tf.greater(v1, v2).eval())
print(tf.where(tf.greater(v1, v2), v1, v2).eval())
sess.close()
