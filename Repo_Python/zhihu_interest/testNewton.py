# @Time : 2018/3/13 16:23 
# @Author : Jing Xu

import numpy as np

para_num = 2
data_num = 7
max_iters = 50

x_1 = np.array([0.038, 0.194, 0.425, 0.626, 1.253, 2.500, 3.740])
y_1 = np.array([0.050, 0.127, 0.094, 0.2122, 0.2729, 0.2665, 0.3317])

a0 = 0.1
b0 = 0.1
RealA = 20.5
RealB = 0.24
eps = 1e-8

y_est = np.zeros(shape=data_num)
d = np.zeros(shape=data_num)
Jacobi = np.zeros(shape=(data_num, para_num))
Jacobi_trans = np.zeros(shape=(para_num, data_num))
Hessian = np.zeros(shape=(para_num, para_num))
delta = np.zeros(shape=(para_num, 1))

a_est = a0
b_est = b0

for it in range(max_iters):
	y_est = a_est * x_1 / ( b_est + x_1 )
	d = y_1 - y_est
	for i in range(data_num):
		Jacobi[i,0] = x_1[i] / ( b_est + x_1[i] )
		Jacobi[i,1] = -a_est * x_1[i] / ( b_est + x_1[i] )**2
	Jacobi_trans = np.transpose(Jacobi)
	Hessian = np.matmul( Jacobi_trans, Jacobi )

	Inv_H_Lm = np.linalg.inv(Hessian)

	rd = np.reshape( d, newshape=(data_num,1))
	delta = np.matmul( np.matmul( Inv_H_Lm, Jacobi_trans ), rd )
	a_Lm = a_est + delta[0,0]
	b_Lm = b_est + delta[1,0]

	if np.dot(delta[:,0], delta[:,0]) < eps:
		break

	a_est = a_Lm
	b_est = b_Lm

	print(a_est, b_est)

print("停止迭代，总共迭代%s次" % str(it).strip())

print("反演参数为：", a_est, b_est)
print("原始数据为：", y_1)
print("拟合数据为：", a_est*x_1/(b_est+x_1))