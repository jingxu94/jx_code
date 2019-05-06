#__author:  "Jing Xu"
#date:  2018/2/8

import tensorflow as tf

# tf.constant是一个计算，这个计算的结果为一个张量，保存在变量a中
a = tf.constant([1.0, 2.0], name="a")
# a = tf.constant([1, 2], name="a") 会出现类型不匹配错误
b = tf.constant([2.0, 3.0], name="b")
result = tf.add(a, b, name="add")
# 张量保存了三个重要属性：名字(name)、维度(shape)、类型(type)
print(result)
print(tf.Session().run(result))