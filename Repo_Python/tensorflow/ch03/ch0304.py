#__author:  "Jing Xu"
#date:  2018/2/9

import tensorflow as tf

# 声明w1、w2两个变量，还通过seed参数设定了随机种子
# 这样可以保证每次运行得到的结果是一样的
w1 = tf.Variable(tf.random_normal([2,3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3,1], stddev=1, seed=1))

# 暂时将输入的特征向量定义为一个常量，这里x是一个1*2的矩阵
# x = tf.constant([[0.7, 0.9]])

x = tf.placeholder(tf.float32, shape=(3, 2), name="input")

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

sess = tf.Session()
# sess.run(w1.initializer)
# sess.run(w2.initializer)
init_op = tf.global_variables_initializer()  # 初始化所有变量，这个函数可以自动处理变量之间的依赖关系
sess.run(init_op)
print(sess.run(y, feed_dict={x: [[0.7, 0.9], [0.1, 0.4], [0.5, 0.8]]}))
sess.close()
