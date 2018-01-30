#__author:  "Jing Xu"
#date:  2018/1/30

# class Foo:
#
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def show(self):
# 		return "%s-%s" %(self.name, self.age)
#
# obj = Foo("alex", 18)
# print(obj.name)
# b = "name"
# print(obj.__dict__[b])
# print(getattr(obj, b))
# func = getattr(obj, "show")
# print(func)
# r = func()
# print(r)
# setattr(obj, "k1", "v1")
# print(obj.k1)
# ---------------------------------------------------------------
# class Page:
#
# 	def f1(self):
# 		return "首页"
#
# 	def f2(self):
# 		return "新闻"
#
# 	def f3(self):
# 		return "精华"
#
# inp = input("请输入要查看的URL：")
# obj = Page()    # obj对象，obj也称为Page类的实例，（实例化）
# if hasattr(obj, inp):
# 	func = getattr(obj, inp)
# 	result = func()
# 	print(result)
# else:
# 	print("输入有误")
# ----------------------------------------------------------------
'''
Python实现单例模式
	- 内存中对象只创建一次，节省内存
'''
class Foo:

	__v = None

	@classmethod
	def get_instance(cls):
		if cls.__v:
			return cls.__v
		else:
			cls.__v = Foo()
			return cls.__v


obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)
