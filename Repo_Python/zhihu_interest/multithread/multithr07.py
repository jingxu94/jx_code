# @Time : 2018/3/8 20:16 
# @Author : Jing Xu

import requests
from bs4 import BeautifulSoup
import time
from threading import Thread
import numpy as np

def cal(a=None):
	s = 0
	for i in range(5000000):
		s = s + i

def file(a=None):
	with open("try.txt","w") as f:
		for i in range(5000000):
			f.write("abcd\n")

def gettitle(a):
	url = "https://movie.douban.com/top250?start={}&filter=".format(a*25)
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html.parser")
	lis = soup.find("ol", class_="grid_view").find_all("li")
	for li in lis:
		title = li.find("span", class_="title").text

def no_thread(func):
	t = time.time()
	for i in range(10):
		func(i)
	duration = time.time() - t
	return duration

def thread(func):
	t = time.time()
	ths = []
	for i in range(10):
		th = Thread(target=func, args=(i,))
		th.start()
		ths.append(th)
	for th in ths:
		th.join()
	duration = time.time() - t
	return duration

def get_duration(func_th, func):
	l = []
	for _ in range(5):
		l.append(func_th(func))
	mean_duration = "%.2f" % np.mean(l)
	all_duration = ["%.2f" % i for i in l]
	return mean_duration, all_duration

print(get_duration(no_thread, cal))
print(get_duration(thread, cal))

# print(get_duration(no_thread, file))
# print(get_duration(thread, file))

print(get_duration(no_thread, gettitle))
print(get_duration(thread, gettitle))