#__author:  "Jing Xu"
#date:  2018/1/16
# ------------------------------------------------------------------
# def f():
# 	print('ok')
# f()
# f()
#
# def add(a,b):
# 	print(a+b)
# add(3,9)
# ------------------------------------------------------------------
# import time
#
# def logger(n):
# 	time_format = '%Y-%m-%d %X'
# 	time_current = time.strftime( time_format )
# 	with open('test_log.txt','a') as f:
# 		f.write('%s end action%s\n'%(time_current,n))
#
# logger(1)
# time.sleep(2)
# logger(2)
# ------------------------------------------------------------------
# def print_info(sex='male',*args,**kwargs):
# 	print(sex)
# 	for i in kwargs:
# 		print('%s:%s'%(i,kwargs[i]))
#
# print_info()
# print_info(2,3,4)
# print_info('lichun',18,job='IT',height=188)
# ------------------------------------------------------------------
# def add(*args):
# 	sum = 0
# 	for i in args:
# 		sum += i
# 	return sum
# a = add(1,4,24,5,2,1,5)
# print(a)
# ------------------------------------------------------------------
# def f():
# 	print('ok')
#
# 	return 10
#
#
# a = f()
# print(a)
# ------------------------------------------------------------------
# x = int(2.9)
# g_count = 0
# def outer():
# 	o_count = 1
#
# 	def inner():
# 		i_count = 2
# 		print(o_count)
#
# 	# print(i_count)	#can't find
# 	inner()
# outer()
# ------------------------------------------------------------------
count = 10
def outer():
	print(count)	#全局变量在局部域中不可以修改，变量查找顺序LEGB
outer()