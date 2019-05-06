# @Time : 2018/3/15 13:10 
# @Author : Jing Xu

import numpy as np
import matplotlib.pyplot as plt
import sys


def uke1(x, y):
	a = np.zeros(shape=3)
	b = np.zeros(shape=3)
	ke = np.zeros(shape=(3,3))
	a[0] = y[1] - y[2]
	a[1] = y[2] - y[0]
	a[2] = y[0] - y[1]
	b[0] = x[2] - x[1]
	b[1] = x[0] - x[2]
	b[2] = x[1] - x[0]
	s = 2.0 * ( a[0] * b[1] - a[1] * b[0] )

	for i in range(3):
		for j in range(i+1):
			ke[i,j] = ( a[i] * a[j] + b[i] * b[j] ) /s
	return ke

def uk1(ND, NE, IW, I3, XY):
	x = np.zeros(shape=3)
	y = np.zeros(shape=3)
	SK = np.zeros(shape=(ND,IW))
	for i in range(NE):
		for j in range(3):
			ii = int(I3[j,i]-1)
			x[j] = XY[0,ii]
			y[j] = XY[1,ii]
		ke = uke1(x, y)
		for j in range(3):
			nj = int(I3[j,i]-1)
			for k in range(j+1):
				nk = int(I3[k,i]-1)
				if nj < nk:
					nj = int(nj - nk + IW -1 )
					SK[nk,nj] = SK[nk,nj] + ke[j,k]
					nj = int(nj + nk - IW + 1 )
				else:
					nk = int(nk - nj + IW - 1 )
					SK[nj,nk] = SK[nj,nk] + ke[j,k]
	return SK

def mbw(NE, I3):
	semi_bandwidth = 0
	for i in range(NE):
		M = max( abs(I3[0,i]-I3[1,i]), abs(I3[1,i]-I3[2,i]), abs(I3[2,i]-I3[0,i]) )
		if M+1 > semi_bandwidth:
			semi_bandwidth = M+1
	return semi_bandwidth

def UB1(ND1, NB1, U1, ND, IW, SK):
	U = np.zeros(shape=ND)
	for i in range(ND1):
		j = int(NB1[i]-1)
		SK[j,IW-1] *= 1e+10
		U[j] = SK[j,IW-1] * U1[i]
	return U

def LDLT(A, N, IW, P, IE=0):
	for i in range(N):
		if i <= IW-1:
			IT = 0
		else:
			IT = i - IW + 2
		k = i
		if i != 0:
			if abs(A[i,IW-1]) < 1e-10:
				IE = 1
				print("Error")
				sys.exit()
			else:
				IE = 0
		for l in range(IT,k):
			IL = int(l + IW - i - 1)
			B = A[i,IL]
			A[i,IL] = B/A[l,IW-1]
			P[i] = P[i] - A[i,IL] * P[l]
			MI = l + 1
			for j in range(MI,i+1):
				ij = int(j + IW - i - 1)
				jl = int(l + IW - j - 1)
				A[i,ij] =  A[i,ij] - A[j,jl] * B

	for j in range(N):
		if j <= IW-1:
			IT = N - 1
			i = N - j - 1
		else:
			IT = N - j + IW - 1
			i = N - j - 1
		P[i] = P[i] / A[i,IW-1]
		# print("1", i, P[i])
		if j != 0:
			IE = 0
			K = i+1
			for mj in range(K,IT+1):
				ij = i - mj + IW - 1
				if ij == -1:
					continue
				P[i] = P[i] - P[mj] * A[mj,ij]
				# print("2", i, P[i])

	return P


ND = 20201
NE = 40000
ND1 = 400
I3 = np.transpose(np.loadtxt("I3.txt"))
XY = np.transpose(np.loadtxt("XY.txt"))
NB1 = np.transpose(np.loadtxt("NB1.txt"))
U1 = np.transpose(np.loadtxt("U1.txt"))

IW = int(mbw(NE,I3))
SK = uk1(ND, NE, IW, I3, XY)
UU = UB1(ND1, NB1, U1, ND, IW, SK)
U = LDLT(SK, ND, IW, UU)

# X, Y = np.meshgrid(XY[0,:], XY[1,:])
#
# # 填充等高线的颜色, 8是等高线分为几部分
# plt.contourf(X, Y, U, 8, alpha = 0.75, cmap = plt.cm.colors)
# # 绘制等高线
# C = plt.contour(X, Y, U, 8, colors = 'black', linewidth = 0.5)
# # 绘制等高线数据
# plt.clabel(C, inline = True, fontsize = 10)
#
# # 去除坐标轴
# plt.xticks(())
# plt.yticks(())
# plt.show()

plt.scatter(XY[0,:], XY[1,:], c=U, alpha=0.5)
plt.show()
# for i in range(15):
# 	print(U[i])
