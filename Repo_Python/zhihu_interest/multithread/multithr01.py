import time
from threading import Thread

def myfun():
	time.sleep(1)
	a = 1 + 1
	print(a)

t1 = time.time()
for i in range(5):
	myfun()

t2 = time.time()
print(t2-t1)

ths = []
for _ in range(5):
	th = Thread(target=myfun)
	th.start()
	ths.append(th)

for th in ths:
	th.join()

t3 = time.time()
print(t3-t2)