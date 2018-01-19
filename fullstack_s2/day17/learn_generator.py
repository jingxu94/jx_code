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
# def fibo(max):
# 	n, before, after = 0, 0, 1
# 	while n < max:
# 		yield before
# 		before, after = after, before+after
# 		n += 1
#
# for i in fibo(10):
# 	print(i)
# -------------------------------------------------------------------------
# #可迭代对象（对象拥有iter方法的称为可迭代对象）
# l = [1,2,3]
# l.__iter__()
# t = (1,2,3)
# t.__iter__()
# d={'name':'123'}
# d.__iter__()
# -------------------------------------------------------------------------
# def bar():
# 	print('ok1')
# 	count = yield 1
# 	print(count)
# 	print('ok2')
# 	count1 = yield 2
# 	print(count1)
# 	print('ok3')
# 	yield 3
#
# b=bar()
# next(b)
# b.send('eee')
# b.send('fff')
# -------------------------------------------------------------------------
# import time
#
# def consumer(name):
# 	print("%s 准备吃包子" %name)
# 	while True:
# 		baozi = yield
# 		print("包子[%s]来了，被[%s]吃了" %(baozi,name))
#
# def producer(name):
# 	c = consumer('A')
# 	c2 = consumer('B')
# 	c.__next__()
# 	c2.__next__()
# 	print("%s准备做包子" %name)
# 	for i in range(1,19,2):
# 		time.sleep(1)
# 		print("做了2个包子")
# 		c.send(i)
# 		c2.send(i+1)
#
# producer("alex")
# -------------------------------------------------------------------------
# # 生成器都是迭代器，迭代器不一定是生成器
# # list，tuple，dict，string：Iterable（可迭代对象）
# l = [1,2,3,4,5]
# d = iter(l)
# print(d)
# # 迭代器满足两个条件(迭代器协议)：1.有iter方法 2.有next方法
# # for循环内部三件事：1.调用可迭代对象的iter方法，返回一个迭代器对象 2.不断调用迭代器对象的next方法 3.处理StopIteration
# -------------------------------------------------------------------------
# from collections import Iterator,Iterable
#
# l = [1,2,3,4,5]
# d = iter(l)
# print(isinstance(l,list))
# print(isinstance(l,Iterator))
# print(isinstance(l,Iterable))
# print(isinstance(d,Iterator))
# -------------------------------------------------------------------------
print(max(len(x.strip()) for x in open("Help_on_builtin_module_time","r",encoding="utf8")))