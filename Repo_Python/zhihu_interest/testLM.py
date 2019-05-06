# @Time : 2018/3/24 13:49
# @Author : Jing Xu

import numpy as np

para_num = 2    #参数个数
data_num = 9    #数据个数
max_iters = 50  #最大迭代次数

#观测的离散数据
x_1 = np.array([0.25,0.5,1.0,1.5,2.0,3.0,4.0,6.0,8.0])
y_1 = np.array([19.306,18.182,16.126,14.302,12.685,9.978,7.849,4.857,3.005])

#模型函数系数初始猜测值，初始迭代值
a0 = -4.0
b0 = 0.0

#模型函数系数真实值
RealA = 20.5
RealB = 0.24

#计算控制精度要求
eps = 1e-8

#数据因变量的估计值，d为与真实值之间的误差
y_est = np.zeros(shape=data_num)
d = np.zeros(shape=data_num)
# rd = np.zeros(shape=(data_num,1))

#雅可比矩阵和其转置，海森矩阵
Jacobi = np.zeros(shape=(data_num, para_num))
Jacobi_trans = np.zeros(shape=(para_num, data_num))
Hessian = np.zeros(shape=(para_num, para_num))

# H_Lm = np.zeros(shape=(para_num, para_num))
# Inv_H_Lm = np.zeros(shape=(para_num, para_num))

#单位矩阵
eye = np.eye(para_num)

#迭代步长矩阵
delta = np.zeros(shape=(para_num, 1))

# a_est = 0.0
# b_est = 0.0
e = 0.0

# y_est_Lm = np.zeros(shape=data_num)
# d_Lm = np.zeros(shape=data_num)
# e_Lm = 0.0

#LM算法阻尼系数初始值
lamba = 0.01
v = 10.0

order = 1
a_est = a0
b_est = b0

for it in range(max_iters):
	if order == 1:  #根据当前估计值，计算雅可比矩阵
		y_est = a_est * np.exp( -b_est * x_1 )  #根据当前a_est，b_est及x_1，得到函数值y_est
		d = y_1 - y_est     #计算y估计值与真实值之间误差
		for i in range(data_num):   #计算雅可比矩阵，dy/da = Exp(-b*x)，dy/db = -a*x*Exp(-b*x)
			Jacobi[i,0] = np.exp( -b_est * x_1[i] )
			Jacobi[i,1] = -a_est * x_1[i] * np.exp( -b_est * x_1[i] )
		Jacobi_trans = np.transpose(Jacobi)
		Hessian = np.matmul( Jacobi_trans, Jacobi )     #计算海森矩阵

	if it == 0:     #若是第一次迭代，计算误差epsilon
		e = np.dot(d,d)
	H_Lm = Hessian + lamba*eye
	Inv_H_Lm = np.linalg.inv(H_Lm)

	rd = np.reshape( d, newshape=(data_num,1))
	delta = np.matmul( Inv_H_Lm, np.matmul( Jacobi_trans, rd ) )
	a_Lm = a_est + delta[0,0]
	b_Lm = b_est + delta[1,0]

	if np.dot(delta[:,0], delta[:,0]) < eps:
		break

	y_est_Lm = a_Lm * np.exp( -b_Lm * x_1 )
	d_Lm = y_1 - y_est_Lm
	e_Lm = np.dot( d_Lm, d_Lm )

	#根据误差，决定如何更新参数和阻尼系数，迭代成功时将lamda减小，否则增大lamda
	if e_Lm < e:
		lamba = lamba/v
		a_est = a_Lm
		b_est = b_Lm
		e = e_Lm
		order = 1
	else:
		order = 0
		lamba = lamba*v

	print(a_est, b_est)

print("停止迭代，总共迭代%s次" % str(it).strip())

print("反演参数为：", a_est, b_est)
print("原始数据为：", y_1)
print("拟合数据为：", a_est*np.exp(-b_est*x_1))