#__author:  "Jing Xu"
#date:  2018/1/17
#
# def f(n):
# 	return n*n
#
# def foo(a,b,f):
# 	return f(a)+f(b)
#
# def g(n):
# 	return n*n*n
#
# print( foo(1,2,f) )
# print( foo(1,2,g) )
#
# ----------------------------------------------------------------
# def foo():
#
# 	def inner():
# 		return 8
#
# 	return inner()
#
# print( foo() )
# ----------------------------------------------------------------
# def f(n):
# 	flag = 1
# 	for i in range(n):
# 		flag *= (i+1)
# 	return flag
#
# print(f(5))
# print(f(7))
#
# def g(n):
# 	if n==1:
# 		return 1
# 	return  n*g(n-1)
#
# print(g(5))
# print(g(7))
# ----------------------------------------------------------------
# def fibo(n):
# 	if n <= 2:
# 		return n-1
# 	return fibo(n-1)+fibo(n-2)
# print(fibo(8))
# ----------------------------------------------------------------
# from functools import reduce
#
# def add1(x,y):
# 	return x + y
# print(reduce(add1,range(1,101)))
# ----------------------------------------------------------------
# from functools import reduce
# print(reduce(lambda x,y: x*y,range(1,6)))
# ----------------------------------------------------------------
# squares = map(lambda x:x*x,range(9))
# print(squares)
# print(list(squares))
# ----------------------------------------------------------------
from functools import reduce
print(list(map(lambda x:x*x,[0,1,2,3,4,5,6])))
print(reduce(lambda x,y:x+y,[0,1,2,3,4,5,6]))
print(list(filter(lambda x:x&1,[0,1,2,3,4,5,6])))