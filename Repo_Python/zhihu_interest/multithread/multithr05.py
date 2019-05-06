import time
import threading

class MyThread(threading.Thread):

	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name

	def run(self):
		a = 1 + 1
		print(threading.current_thread().name)
		time.sleep(1)
		print(self.name)
		time.sleep(1)
		print(self.is_alive())

t = time.time()

ths = [MyThread("thread {}".format(i)) for i in range(3)]

for th in ths:
	th.start()

print(threading.activeCount())
for th in ths:
	th.join()

print(time.time()-t)