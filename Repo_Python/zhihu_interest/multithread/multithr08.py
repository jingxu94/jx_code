# @Time : 2018/3/8 21:01 
# @Author : Jing Xu

import time
import threading
import random

class Producer(threading.Thread):

	def __init__(self, lock, integer_list):
		threading.Thread.__init__(self)
		self.lock = lock
		self.integer_list = integer_list

	def run(self):
		while True:
			random_integer = random.randint(0, 100)
			with self.lock:
				self.integer_list.append(random_integer)
				print("integer list add integer {}".format(random_integer))
			time.sleep(1.2*random.random())


class Consumer(threading.Thread):

	def __init__(self, lock, integer_list):
		threading.Thread.__init__(self)
		self.lock = lock
		self.integer_list = integer_list

	def run(self):
		while True:
			with self.lock:
				if self.integer_list:
					integer = self.integer_list.pop()
					print("integer list lose integer {}".format(integer))
					time.sleep(random.random())
				else:
					print("there is no integer in the list")


def main():
	integer_list = []
	lock = threading.Lock()
	th1 = Producer(lock, integer_list)
	th2 = Consumer(lock, integer_list)
	th1.start()
	th2.start()

if __name__ == "__main__":
	main()