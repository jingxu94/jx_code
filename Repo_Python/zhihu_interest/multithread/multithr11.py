# @Time : 2018/3/8 22:07 
# @Author : Jing Xu

import time
import threading
import random
from queue import Queue


class ListQueue(Queue):

    def _init(self, maxsize):
        self.maxsize = maxsize
        self.queue = []

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop()


class Producer(threading.Thread):

	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			for _ in range(3):
				self.queue.put(random.randint(0, 100))
			print("now {} after add".format(self.queue.queue))
			time.sleep(random.random())


class Consumer(threading.Thread):

	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			get_integer = self.queue.get()
			print("lose {}".format(get_integer), "now total", self.queue.queue)
			time.sleep(random.random())


def main():
	queue = ListQueue(5)
	th1 = Producer(queue)
	th2 = Consumer(queue)
	th1.start()
	th2.start()

if __name__ == "__main__":
	main()