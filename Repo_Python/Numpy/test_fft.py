# @Time : 2018/5/25 16:12 
# @Author : Jing Xu

import numpy as np
from matplotlib.pyplot import plot, show
x = np.linspace(0, 2 * np.pi, 30) #创建一个包含30个点的余弦波信号
wave = np.cos(x)
transformed = np.fft.fft(wave)  #使用fft函数对余弦波信号进行傅里叶变换。
print(np.all(np.abs(np.fft.ifft(transformed) - wave) < 10 ** -9))  #对变换后的结果应用ifft函数，应该可以近似地还原初始信号。
plot(transformed)  #使用Matplotlib绘制变换后的信号。
show()

x = np.linspace(0, 2 * np.pi, 30)
wave = np.cos(x)  #创建一个包含30个点的余弦波信号。
transformed = np.fft.fft(wave)  #使用fft函数对余弦波信号进行傅里叶变换。
shifted = np.fft.fftshift(transformed) #使用fftshift函数进行移频操作。
print(np.all((np.fft.ifftshift(shifted) - transformed) < 10 ** -9))  #用ifftshift函数进行逆操作，这将还原移频操作前的信号。
plot(transformed, lw=2)
plot(shifted, lw=3)
show()    #使用Matplotlib分别绘制变换和移频处理后的信号。
