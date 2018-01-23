#__author:  "Jing Xu"
#date:  2018/1/23

import pickle

def foo():
	print("ok1")

data = pickle.dumps( foo )
with open("PICKLE_text","wb") as f1:
	f1.write(data)

def foo():
	print("ok2")

with open("PICKLE_text","rb") as f2:
	data1 = f2.read()

data1 = pickle.loads( data1 )

data1()