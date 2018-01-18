#__author:  "Jing Xu"
#date:  2018/1/18
# ----------------------------------------------------------------
# def outer():
# 	x = 10
# 	def inner():	#条件一：inner是一个内部函数
# 		print(x)    #条件二：引用外部环境的一个变量
# 	return inner    #结论：  内部函数inner是一个闭包
# outer()()
# ----------------------------------------------------------------
# import time
#
# def show_time(func):
# 	def inner():
# 		start = time.time()
# 		func()
# 		end = time.time()
# 		print('Spend %s' % (end - start))
# 	return inner
#
# @show_time
# def foo():
# 	print('foo......')
# 	time.sleep(2)
# # foo = show_time(foo)
#
# @show_time
# def bar():
# 	print('bar......')
# 	time.sleep(3)
# # bar = show_time(bar)
#
# foo()
# bar()
# ----------------------------------------------------------------
import time

def logger(flag=''):
	def show_time(func):
		def inner(*args,**kwargs):
			start = time.time()
			func(*args,**kwargs)
			end = time.time()
			print('Spend %s' % (end - start))
			if flag == 'True':
				print('日志记录')
		return inner
	return show_time

@logger('True')
def add(*args):
	sums = 0
	for i in args:
		sums += i
	print(sums)
	time.sleep(2)

@logger()
def bar():
	print('bar......')
	time.sleep(3)

add(2,3,6,8,4,3.5)
bar()