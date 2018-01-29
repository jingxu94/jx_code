#__author:  "Jing Xu"
#date:  2018/1/29

'''
Python中一切事物都是对象
obj是对象，Foo是类
Foo类也是一个对象，type的对象
声明了一个类
def func(self):
	print("123")
Foo = type("Foo",(object,), {"func": function})
'''

class MyType(type):

	def __init__(self, *args, **kwargs):
		print("123")

	def __call__(self, *args, **kwargs):
		print("456")

class Foo(object, metaclass=MyType):

	def __init__(self):
		pass

	def __new__(cls, *args, **kwargs):
		return "object"

	def func(self):
		print("hello world")


obj = Foo()