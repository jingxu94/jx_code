#__author:  "Jing Xu"
#date:  2018/1/31

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# -------------------------------------------------------------
# mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# mat2 = np.arange(1,10).reshape(3,3)
# mat3 = np.zeros((3,3))
# mat4 = np.ones((3,3))
# mat5 = np.eye(3)
# print(mat1)
# print(mat2)
# print(mat3)
# print(mat4)
# print(mat5)
# -------------------------------------------------------------
# a = np.array([[1.25, -16],[32,264.75]], np.float32)
# b = np.array(a, np.int32)
# c = b.astype("uint8")
# print(a)
# print(b)
# print(c)
# -------------------------------------------------------------
# mat = np.arange(1,10).reshape(3,3)
# print(mat)
# print(mat[2][2])
# print(mat[2,2])
# print(mat[:2,:2])
#
# mask = mat > 5
# print(mask)
#
# mat[mask] = 5
# print(mat)
# -------------------------------------------------------------
# x = np.arange(4)
# print(x)
# xt = x.reshape(-1,1)
# print(xt)
# z = np.ones((3,4))
# print(z)
# print(x+xt)
# print(x+z)
# -------------------------------------------------------------

## (1) 绘制随机噪点
## 初始化随机种子，并生成随机坐标
np.random.seed(0)
data = np.random.randn(2, 100)
## 创建画布
fig, axs = plt.subplots(2, 2, figsize=(5, 5))
## 绘制子图
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])
## 显示
plt.show()

## (2) 绘制图像
img = mpimg.imread("/home/auss/Pictures/test.png")
imgx = img[:,:,0] # 取第一个通道

## 创建画布
fig = plt.figure()

## 绘制原始图像，并加上颜色条
axs = fig.add_subplot(1,3,1)
ipt = plt.imshow(img)
axs.set_title("origin")
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

## 绘制伪彩色图像，并加上颜色条
axs = fig.add_subplot(1,3,2)
ipt = plt.imshow(imgx,cmap="winter")
axs.set_title("winter")
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

## 绘制直方图
axs = fig.add_subplot(1,3,3)
ipt = plt.hist(imgx.ravel(), bins=256, range=(0, 1.0), fc='k', ec='k')
axs.set_title("histogram")

plt.show()
