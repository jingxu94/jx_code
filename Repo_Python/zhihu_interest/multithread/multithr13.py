# @Time : 2018/3/10 22:55 
# @Author : Jing Xu

import threading
import time


# ----------------------------------------------------------------------------
# '''
# 线程锁（线程同步、互斥锁）
# '''
# zero = 0
# lock = threading.Lock()
#
# def change_zero():
# 	global zero
# 	for i in range(1000000):
# 		lock.acquire()  # Lock具有上下文管理模式，此段代码可以改为 with lock:
# 		zero = zero +1
# 		zero = zero -1
# 		lock.release()
#
# th1 = threading.Thread(target=change_zero)
# th2 = threading.Thread(target=change_zero)
# th1.start()
# th2.start()
# th1.join()
# th2.join()
# print(zero)
# ----------------------------------------------------------------------------

lock1 = threading.Lock()
lock2 = threading.Lock()
class MyThread(threading.Thread):
    def print1(self):
        lock1.acquire() # 获得第一个锁
        print('print1 first ' + threading.current_thread().name)
        time.sleep(1)
        lock2.acquire() # 未释放第一个锁就请求第二个锁
        print('print1 second ' + threading.current_thread().name)
        lock2.release()
        lock1.release()
    def print2(self):
        lock2.acquire() # 获得第二个锁
        print('print2 first ' + threading.current_thread().name)
        time.sleep(1)
        lock1.acquire() # 未释放第二个锁就请求第一个锁
        print('print2 second ' + threading.current_thread().name)
        lock1.release()
        lock2.release()
    def run(self):
        self.print1()
        self.print2()
th1 = MyThread()
th2 = MyThread()
th1.start()
th1.join()
th2.start()
th2.join()
print('finish')