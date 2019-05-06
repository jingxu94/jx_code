# @Time : 2018/3/9 21:12 
# @Author : Jing Xu

import threading
import time


class MyThread(threading.Thread):

	def __init__(self, event):
		threading.Thread.__init__(self)
		self.event = event

	def run(self):
		print("first")
		self.event.wait()
		print("after wait")


event = threading.Event()
MyThread(event).start()
print("before set")
time.sleep(1)
event.set()