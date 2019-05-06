import threading
import requests
from bs4 import BeautifulSoup

class Mythread(threading.Thread):

	def __init__(self, i):
		threading.Thread.__init__(self)
		self.i = i

	def run(self):
		url = "https://movie.douban.com/top250?start={}&filter=".format(self.i*25)
		r = requests.get(url)
		soup = BeautifulSoup(r.content, "html.parser")
		lis = soup.find("ol", class_="grid_view").find_all("li")
		print(threading.current_thread())
		for li in lis:
			title = li.find("span", class_="title").text
			print(title)

for i in range(10):
	th = Mythread(i)
	th.start()