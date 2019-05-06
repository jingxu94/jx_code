import time
import threading

class MyThread(threading.Thread):

	def run(self):
		time.sleep(1)
		a = 1 + 1
		print(a)

t1 = time.time()

ths = []

for _ in range(5):
	th = MyThread()
	ths.append(th)
	th.start()

for th in ths:
	th.join()

t2 = time.time()
print(t2-t1)