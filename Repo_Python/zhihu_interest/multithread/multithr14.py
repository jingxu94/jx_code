# @Time : 2018/3/11 12:56 
# @Author : Jing Xu

import threading
import requests
from bs4 import BeautifulSoup
from queue import Queue


class MyThread(threading.Thread):

	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		while not self.queue.empty():
			url = self.queue.get()
			print(self.name, url)
			url_queue.task_done()
			r = requests.get(url)
			soup = BeautifulSoup(r.content, "html.parser")
			lis = soup.find("ol", class_="grid_view").find_all("li")
			for li in lis:
				title = li.find("span", class_="title").text
				print(title)


url_queue = Queue()
for i in range(10):
	url = "https://movie.douban.com/top250?start={}&filter=".format(i*25)
	url_queue.put(url)

th1 = MyThread(url_queue)
th2 = MyThread(url_queue)
th1.start()
th2.start()
th1.join()
th2.join()
url_queue.join()
print("finish")
