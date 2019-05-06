#__author:  "Jing Xu"
#date:  2018/2/4

import numpy as np
import timeit

print(np.__version__)
# ----------------------------------------------------------------
# a = np.array([1, 2, 3, 4])
# b = np.array([5, 6, 7, 8])
# c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
# print(c)
# print(a.shape, c.shape)
# c.shape = 2, -1
# print(c)
# d = a.reshape(2,-1)
# print(a)
# print(d)
# print(c.dtype)
# ai = np.array([1, 2, 3, 4], dtype=np.int32)
# af = np.array([1, 2, 3, 4], dtype=float)
# ac = np.array([1, 2, 3, 4], dtype=complex)
# print(ai.dtype, af.dtype, ac.dtype)
# print(set(np.typeDict.values()))
# ----------------------------------------------------------------
# print(np.arange(0, 1, 0.1))
# print(np.linspace(0, 1, 11))
# print(np.linspace(0, 1, 10, endpoint=False))
# print(np.logspace(0, 2, 5))
# print(np.logspace(0, 1, 12, base=2, endpoint=False))
# ----------------------------------------------------------------
# s = "abcdefgh"
# print(np.fromstring(s, dtype=np.int8))
# ----------------------------------------------------------------
# x = np.arange(10, 1, -1)
# print(x)
# print(x[np.array([3, 3, 1, 8])])
# print(x[[3, 3, 1, 8, 3, 3, -3, 8]].reshape(2,4))
# ----------------------------------------------------------------
# x = np.arange(5, 0, -1)
# print(x)
# print(x[np.array([True, False, True, False, False])])
# 布尔列表会被当做布尔数组，因此两种写法运行结果一样
# print(x[[True, False, True, False, False]])
# ----------------------------------------------------------------



