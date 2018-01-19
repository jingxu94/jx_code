#__author:  "Jing Xu"
#date:  2018/1/19
# ----------------------------------------------------------------
# import time
# print(help(time))
# print(time.time())
# time.sleep(3)
# print(time.clock())
# print(time.gmtime())
# print(time.localtime())
# struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time))
# print(time.strptime("2018-01-19 15:40:23","%Y-%m-%d %H:%M:%S"))
# a = time.strptime("2018-01-19 15:40:23","%Y-%m-%d %H:%M:%S")
# print(a.tm_year)
# print(a.tm_mon)
# print(a.tm_wday)
# print(time.ctime(time.time()))
# print(help(time.mktime))
# print(time.mktime(time.localtime()))
# ----------------------------------------------------------------
# import datetime
# print(type(datetime.datetime.now()))
# print(datetime.datetime.now())
# ----------------------------------------------------------------
# import random
# print(random.random())
# print(random.randint(1,8))
# print(random.choice('hello'))
# print(random.choice(['123','4',[1,2]]))
# print(random.sample(['123','4',[1,2]],2))
# print(random.randrange(1,4))
# ----------------------------------------------------------------
import random

def v_code1():
	code = ''
	for i in range(5):
		if i == random.randint(i,i+2):
			add_str = random.randrange(10)
		elif i == random.randint(i,i+1):
			add_str = chr(random.randrange(65,91))
		else:
			add_str = chr(random.randrange(97,123))
		code += str(add_str)
	return code

def v_code2():
	code = ''
	for i in range(5):
		add_str = random.choice([str(random.randrange(10)),chr(random.randrange(65,91)),chr(random.randrange(97,123))])
		code += add_str
	return code

a = v_code1()
print(a)
b = v_code2()
print(b)