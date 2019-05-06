# @Time : 2018/3/11 20:44 
# @Author : Jing Xu

def myfun(total):
	for i in range(total):
		yield i

# m = myfun(4)
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))

# for i in myfun(4):
# 	print(i)

m = myfun(4)
while True:
	try:
		print(next(m))
	except StopIteration:
		break

from itertools import count
c = count(start=5, step=2)
for _ in range(5):
	print(next(c))

def myfun1(total):
	for i in range(total):
		yield i
	yield from ["a", "b", "c"]

m1 = myfun1(4)
while True:
	try:
		print(next(m1))
	except StopIteration:
		break

def consumer():
	r = ""
	while True:
		n = yield r
		if not n:
			return
		print("[CONSUMER] Consuming %s..." % n)
		r = "200 OK"

def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print("[PRODUCER] Producing %s..." % n)
		r = c.send(n)
		print("[PRODUCER] Consumer return: %s" % r)
	c.close()

c = consumer()
produce(c)