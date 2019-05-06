# @Time : 2018/3/11 13:24 
# @Author : Jing Xu

import time
import threading
import random
import requests
import json

# thread_num = 10000
#
# def run():
# 	print("first, there are", threading.activeCount(), "threads running")
# 	time.sleep(thread_num/1000 * random.random())
# 	print("second, there are ", threading.activeCount(), "threads running")
#
# for i in range(thread_num):
# 	th = threading.Thread(target=run)
# 	th.start()

thread_num = 100

def run():
    print('first, there are', threading.activeCount(), 'threads running')
    r = requests.post("http://httpbin.org/post",
    data = 'second there are {} threading running'.format(threading.activeCount()))
    print(r.json()['data'])

for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()
