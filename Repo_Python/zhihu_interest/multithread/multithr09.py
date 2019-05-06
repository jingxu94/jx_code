# @Time : 2018/3/8 21:49 
# @Author : Jing Xu

import time
import threading
import random

class Producer(threading.Thread):

	def __init__(self, condition, integer_list):
		threading.Thread.__init__(self)
		self.condition = condition
		self.integer_list = integer_list

	def run(self):
		while True:
			random_integer = random.randint(0, 100)
			with self.condition:
				self.integer_list.append(random_integer)
				print("integer list add integer {}".format(random_integer))
				self.condition.notify()
			time.sleep(1.2*random.random())


class Consumer(threading.Thread):

	def __init__(self, condition, integer_list):
		threading.Thread.__init__(self)
		self.condition = condition
		self.integer_list = integer_list

	def run(self):
		while True:
			with self.condition:
				if self.integer_list:
					integer = self.integer_list.pop()
					print("integer list lose integer {}".format(integer))
					time.sleep(random.random())
				else:
					print("there is no integer in the list")
					self.condition.wait()


def main():
	integer_list = []
	condition = threading.Condition()
	th1 = Producer(condition, integer_list)
	th2 = Consumer(condition, integer_list)
	th1.start()
	th2.start()

if __name__ == "__main__":
	main()