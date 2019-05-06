# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 09:11:38 2018
@author: luk
"""

#------------------------------------------------------------------#
# 2.1.1 创建
import numpy as np
# 创建一维数组
a = np.array( [1,2,3,4] ) # 元素之间不能用空格隔开
b = np.array( (5,6,7,8) )
a = 2*a
print ( " 2*a: ", a )

# 创建二维数组
c = np.array( [ [1,2,3,4],[4,5,6,7],[6,7,8,9] ] )
print ( " array a: ", a )
print ( " array b: ", b )
print ( " array c: ", c )
m = len(c)  # 获取二维数组的行与列
n = len(c[0])
print ( " row c: ", m )
print ( " col c: ", n )

# 输出二维数组
for i in range( m ):
      for j in range( n ):
            print ( c[i][j], end = ' ' )
            if j == n-1:
                  print ( '\n' )  # 换行

# tyep( a.shape ) 为元组
print ( " a shape: ", a.shape, type(a.shape) )
print ( " b shape: ", b.shape )
print ( " c shape: ", c.shape )

# 改变二维数组c的形状
c.shape = 4, 3
m = len(c)  # 获取二维数组的行与列
n = len(c[0])
print ( " row c: ", m )
print ( " col c: ", n )
for i in range( m ):
      for j in range( n ):
            print ( c[i][j], end = ' ' )
            if j == n-1:
                  print ( '\n' )

# 当某个维度的元素个数是-1时，将自动计算此维度的长度
# 由于数组c有12个元素，因此下面的程序将数组c的shape改成了(2,6)
c.shape = 2, -1
m = len(c)  # 获取二维数组的行与列
n = len(c[0])
print ( " row c: ", m )
print ( " col c: ", n )
for i in range( m ):
      for j in range( n ):
            print ( c[i][j], end = ' ' )
            if j == n-1:
                  print ( '\n' )
a.shape = -1 # 对于一维数组还是其原来的size
print ( a )

# 使用数组的reshape()方法，可以创建指定形状的数组，而原数组的形状保持不变
# 但是这种情况，a和d是共享数据存储空间，一个改变，另一个也改变
d = a.reshape((2,2)) # 由于数组形状的type为tuple，所以是(2,2),不是[2,2]
print ( " d :", d )
# d的size是2*2，shape是(2,2)
print ( " d.shape: ", d.shape )
print ( " d.size: ", d.size )

# 由于共享内存，所以d的shape改变，a的shape也改变
e = a
e.shape = 2, 2
print ( " shape a: ", a.shape )
print ( " e :", e )
a[1] = 100
print( e )

# sizd的用法
import numpy as np
from numpy import random
matrix1 = random.random(size=(2,4))
# 每维的大小
print( matrix1.shape )

# 对应矩阵元素相乘
# 对于aray对象：
a = np.array( [[1,2],[3,4]] )
b = np.array( [[4,3],[2,1]] )
print ( " a*b: ", a*b )

# 按矩阵运算法则相乘: np.dot和np.matmul运算结果一样
print ( " np.dot(a,b): ", np.dot(a,b) )
print ( " np.matmul(a,b): ", np.matmul(a,b) )

# 对于matrix对象：
a = np.mat( [[1,2],[3,4]] )
b = np.mat( [[4,3],[2,1]] )
# 对于matrix对象，'*'表示原生的矩阵乘法规则
print ( " a*b: ", a*b )
# multiply表示数量积
print ( " np.multiply(a,b): ", np.multiply(a,b) )

# 矩阵的转置
print ( " before transpose b: ", b )
b = np.transpose(b)
print ( " after transpose b: ", b )

#------------------------------------------------------------------#
# 2.1.2 元素类型
# 通过dtype参数在创建数组时指定元素类型
# float是64位的双精度浮点类型
# complex是128位的双精度复数类型
ai32 = np.array( [1,2,3,4], dtype = np.int32 )  # int32前面要加np.
af = np.array( [1,2,3,4], dtype = float )
ac = np.array( [1,2,3,4], dtype = complex )
print ( ' ai32 type: ', ai32.dtype )  # 获取数组的元素类型
print ( ' af type: ', af.dtype )
print ( ' ac type: ', ac.dtype )

# 使用astype()方法可以对数组的元素类型进行转化
t1 = np.array( [1,2,3,4], dtype = np.float )
t2 = np.array( [1,2,3,4], dtype = np.complex )
t3 = t1.astype( np.int32 )
t4 = t2.astype( np.complex64 )

#------------------------------------------------------------------#
# 2.1.3 自动生成数组
# 一维数组
# 1. arange()类似于内置函数range(), 指定开始值，终值和步长
a = np.arange( 0, 1, 0.1, dtype = float )
# 2. linspace()通过指定开始值，终值和元素个数创建等差数列一维数组
# 可以通过endpoint指定是否包含终值，默认值位True, 即包含终值
b = np.linspace( 0, 1, 10, dtype = np.float64 )
# 3. logspace()创建的数组是等比数列。默认的基数是10
a = np.logspace( 0, 2, 5 )
b = np.logspace( 0, 1, 12, base = 2.0, endpoint = False )
# 上面的三个函数创建的都是一维数组

# 二维数组
# 1. zeros()将数组初始化为0
a = np.zeros( (2,2), np.int32 )
# 2. ones()将数组初始化为1
b = np.ones( (2,3), dtype = float )
# 3. empty()只分配数组使用的内存，不对数组进行初始化操作
c = np.empty( 4, np.int32 )
# 4. full()将数组初始化为指定值
c = np.full( (2,3), np.pi )
# 此外， zeros_like(), ones_like(), full_like(), empty_like等函数创建与参数数组的
# 形状和类型相同的数组，因此zeros_like(a)与zeros( a.shape, a.dtype )的效果相同
# 5. 通过fromfunction()创建数组
def func1(i):
      return i % 4 + 1
a = np.fromfunction( func1, (10,) )  # 数组大小为10，但是i的范围为0-9

def func2( i, j ):
      return ( i + 1 ) * ( j + 1 )
b = np.fromfunction( func2, (9,9) ) # 数组大小为(9,9)，但是i和j的范围是0-8

#------------------------------------------------------------------#
a = np.arange(10)
print ( a[5] )  # 获取第六个元素
print ( a[3:5] ) # 获取第四个到第五个元素
print ( a[:5] )   # 获取前六个（包括第六个）元素
print ( a[:-2] ) # 去掉后面两个数
print ( a[5:1:-2] )  # 取[5,4,3,2]中的[5,3]，这个重点记忆
print ( a[1:-1:2] ) # [1,...,8]隔两个取一个
print ( a[::-1] ) # 颠倒数组a输出
# 不同于列表，数组可以修改片段
a[2:4] = 100, 101
print ( a )
b = a[3:7] # 不能b = a[3,4,5,6,7], 可以b = a[[3,4,5,6,7]]
print ( b )
b[2] = -10
print ( a )
print ( id(a), id(b) )  # a, b有相同的id

b = [1,2,3,4]
print ( a )
print ( id(a), id(b) )  # 此时a, b有不同的id。因为b赋值的不是某一个数组的片段
# **使用列表作为下标得到的数组不和原始数组共享内存
x = np.arange( 10, 1, -1 )  # x = [10,.., 2]. 不包括1
a = x[ [3,3,1,8] ]
b = x[ [3,3,-3,8] ] # 下标可以是负数，倒数第三个
b[2] = 100 # 修改其值
print ( b )  # b = [ 7, 7, 100, 2 ]
print ( x )  # x = [10 9 8 7 6 5 4 3 2] # 数组x不变

# 整数序列下标也可以用来修改元素的值
x[[3,5,1]] = -1, -2, -3
print ( x ) # x = [ 10,-3,8,-1,6,-2,4,3,2 ]
# 当下标是一维数组时，结果和用列表作为下标的结果相同
x = np.arange( 10, 1, -1 ) # x = [10,9,8,7,6,5,4,3,2]
a = x[np.array([3,3,1,8])]
print ( a ) # a = [7,7,9,2]
# 当数组是多维数组时，得到的也是多维数组
a = x[np.array( [[3,3,1,8],[3,3,-3,8]] )]
print ( a )

# 布尔数组
x = np.arange(5,0,-1)
print ( x ) # x = [5,4,3,2,1]
a = x[np.array( [True,False,True,False,False] )]
# 数组a的值为True对应的值，False对应的值舍去
print ( a ) # a = [5,3]
# 布尔列表
a = x[ [True,False,True,False,False] ]
# 布尔列表与布尔数组功能相同
print ( a ) # a = [5,3]

# 布尔数组下标修改元素
# 将True对应处的值进行修改
x[np.array([True,False,True,True,False])] = -1, -2, -3
print ( x )

# 布尔数组下标的应用
x = np.random.randint(0,10,6) # 产生长度为6的随机数组，0-9之间
print ( x )
a = x[ x > 5 ]  # x > 5会产生一个长度为6的布尔数组
print ( a )