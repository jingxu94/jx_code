# @Time : 2018/3/8 21:53 
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
			with self.condition:
				if len(self.integer_list) > 5:
					print("Producer start waiting")
					self.condition.wait()
				else:
					for _ in range(3):
						self.integer_list.append(random.randint(0, 100))
					print("now {} after add ".format(self.integer_list))
					self.condition.notify()
			time.sleep(random.random())


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
					print("all {} lose {}".format(self.integer_list, integer))
					time.sleep(random.random())
					if len(self.integer_list) < 4:
						self.condition.notify()
						print("Producer don't need to wait")
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