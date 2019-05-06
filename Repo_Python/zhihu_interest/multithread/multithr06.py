# @Time : 2018/3/7 16:15 
# @Author : Jing Xu

import threading
import requests
from bs4 import BeautifulSoup

def gettitle(page):
	url = "https://movie.douban.com/top250?start={}&filter=".format(page * 25)
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	lis = soup.find("ol", class_="grid_view").find_all("li")
	print(threading.current_thread())
	for li in lis:
		title = li.find("span", class_="title").text
		print(title)

class MyThread(threading.Thread):

	def __init__(self, target, **args):
		threading.Thread.__init__(self)
		self.target = target
		self.args = args

	def run(self):
		self.target(**self.args)

for i in range(10):
	th = MyThread(gettitle, page=i)
	th.start()