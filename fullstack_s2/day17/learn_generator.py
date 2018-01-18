#__author:  "Jing Xu"
#date:  2018/1/18
# -------------------------------------------------------------------------
# def f(n):
# 	return n*n*n
#
# a = [ x*2 for x in range(10) ]
#
# s = ( x*2 for x in range(10) )	#generator is an iterable
# print(s)		#<generator object <genexpr> at 0x000001C20702C308>
# print(next(s))  #等价于s.__next__() in Py2
# print(next(s))
# -------------------------------------------------------------------------
# s = ( x*2 for x in range(10) )
# for i in s:	#for具有调用next的作用
# 	print(i)
# -------------------------------------------------------------------------
# def foo():
# 	print('ok')
# 	yield 1
# 	print('ok2')
# 	yield 2
#
# g=foo()
# print(g)
# next(g)
# g=foo()
# next(g)
# print(g)
# next(g)
# -------------------------------------------------------------------------
def fibo(max):
	n, before, after = 0, 0, 1
	while n < max:
		yield before
		before, after = after, before+after
		n += 1

for i in fibo(10):
	print(i)