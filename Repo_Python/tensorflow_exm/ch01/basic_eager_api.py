# @Time : 2018/3/19 21:08 
# @Author : Jing Xu

import numpy as np
import tensorflow as tf
import tensorflow.contrib.eager as tfe

print("Setting Eager mode...")
tfe.enable_eager_execution()

print("Define constant tensors")
a = tf.constant(2)
print("a = %i" % a)
b = tf.constant(3)
print("b = %i" % b)

print("Running operations, without tf.Session")
c = a + b
print("a + b = %i" % c)
d = a * b
print("a * b = %i" % d)

a = tf.constant([[2., 1.],
                 [1., 0.]], dtype=tf.float32)
print("Tensor:\n a = %s" % a)
b = np.array([[3., 3.],
              [5., 1.]], dtype=np.float32)
print("NumpyArray:\n b = %s" % b)
print("Running operations, without tf.Session")
c = a + b
print("a + b = %s" % c)
d = a * b
print("a * b = %s" % d)

print("Iterate through Tensor 'a':")
for i in range(a.shape[0]):
	for j in range(a.shape[1]):
		print(a[i][j])