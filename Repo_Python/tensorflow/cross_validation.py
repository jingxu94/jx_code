import tensorflow as tf
import sys
orig_stdout = sys.stdout
f = open('sgd_y.txt', 'w')
sys.stdout = f
import numpy as np
tf.set_random_seed(777) 

#Loading training and validation set
tx = np.loadtxt('em_training.csv', delimiter=',', dtype=np.float32)
ty = np.loadtxt('rho_training.csv', delimiter=',', dtype=np.float32)
x_train = tx[:, [1]]
y_train = ty[:, [1]]

vx = np.loadtxt('em_validation.csv', delimiter=',', dtype=np.float32)
vy = np.loadtxt('rho_validation.csv', delimiter=',', dtype=np.float32)
x_validation = vx[:, [1]]
y_validation = vy[:, [1]]

#Parameter
step_length=0.0001
regularization_parameter = 0

#Declearing variables
X = tf.placeholder(tf.float32, [None, 1])
Y = tf.placeholder(tf.float32, [None, 1])


#Construction of neural network
W1 = tf.get_variable("W1", shape=[1, 2],
                     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([2]))
L1 = tf.matmul(X, W1) + b1

W2 = tf.get_variable("W2", shape=[2, 2],
                     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([2]))
L2 = tf.matmul(L1, W2) + b2

W3 = tf.get_variable("W3", shape=[2, 2],
                     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([2]))
L3 = tf.matmul(L2, W3) + b3

W4 = tf.get_variable("W4", shape=[2, 1],
                     initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([1]))

#Hypothesis for forward propagation
hypothesis = tf.matmul(L3, W4) + b4

#Regularization
reg_W1 = tf.reduce_sum(tf.square(W1))
reg_W2 = tf.reduce_sum(tf.square(W2))
reg_W3 = tf.reduce_sum(tf.square(W3))
reg_W4 = tf.reduce_sum(tf.square(W4))
regularizer = reg_W1 + reg_W2 + reg_W3 + reg_W4

#Objective funtion
cost = tf.reduce_mean(tf.square(hypothesis - Y)+regularization_parameter*regularizer)

#Stochastic gradient descent 
optimizer = tf.train.GradientDescentOptimizer(
        learning_rate=step_length).minimize(cost)

#training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(500001):
        sess.run(optimizer, feed_dict={X: x_train, Y: y_train})
        if step % 10 == 0:
            misfit_train = sess.run(cost, feed_dict={X: x_train
                                    , Y: y_train})
            misfit_validation = sess.run(cost, feed_dict={X: x_validation
                                         , Y: y_validation})
            print("Step: {:5}\tData misfit Train: {:.7f}\tValidation: {:.7f}"
                  .format(step, misfit_train, misfit_validation))

    print('\n Training finished')
    
    print('--------------------------------------------------')
    prediction=sess.run(hypothesis, feed_dict={X: x_validation})
    label=y_validation
    print('\n Prediction\n')
    for i in prediction:
        print(i)
    print('\n True label')
    for j in label:
        print(j)
        

sys.stdout = orig_stdout
f.close()

    