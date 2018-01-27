#__author:  "Jing Xu"
#date:  2018/1/26

# import socketserver
#
# obj = socketserver.ThreadingTCPServer(1,2)
# obj.serve_forever()
# ----------------------------------------------------------
# class Person:
#
# 	def __init__(self, name, age, gender, fight):
# 		self.name = name
# 		self.age = age
# 		self.gender = gender
# 		self.fight = fight
#
# y_n = input("是否创建角色？")
# if y_n == "Y" or y_n == "y":
# 	name = input("输入角色名：")
# 	age = input("输入年龄：")
# 	gender = input("性别：")
# 	fight = input("战斗力")
# p1 = Person(name, age, gender, fight)
# print(p1)
# ----------------------------------------------------------
# '''
# 类成员：
# 	字段
# 		- 普通字段，保存在对象中，执行只能通过对象访问
# 		- 静态字段，保存在类中，执行可以通过对象访问，也可以通过类访问
# 	方法
# 		- 普通方法，保存在类中，由对象来调用，self==>>对象
# 		- 静态方法，保存在类中，由类直接调用
# 		- 类方法，保存在类中，由类直接调用，cls==>>当前类
# 	应用场景：
# 		如果对象中需要保存一些值，执行某功能时，需要使用对象中的值 ==>> 普通方法
# 		不需要任何对象中的值 ==>> 静态方法
# '''
# class Foo:
#
# 	country = "China"   #静态字段
#
# 	def __init__(self, name):
# 		self.name = name    #普通字段
#
# 	def show(self):
# 		print(self.name)
#
# 	@staticmethod
# 	def sta():
# 		print("123")
#
# 	@staticmethod
# 	def stat(a1,a2):
# 		print(a1,a2)
#
# 	@classmethod
# 	def classmd(cls):   # cls是类名
# 		print(cls)
# 		print("classmd")
#
#
# Foo.classmd()
# Foo.sta()
# Foo.stat(3,4)
# print(Foo.country)
# obj = Foo("alex")
# print(obj.name)
# obj.show()
# ----------------------------------------------------------
# class Foo:
#
# 	def __init__(self):
# 		self.name = "a"
#
# 	def bar(self):
# 		print("bar")
#
# 	@property   #属性，方法是内在，调用像字段
# 	def per(self):
# 		print("123")
# 		return 1
#
# 	@per.setter
# 	def per(self, val):
# 		print(val)
#
# 	@per.deleter
# 	def per(self):
# 		print("666")
#
# obj = Foo()
# r = obj.per
# print(r)
# obj.per = 1221
# del obj.per
# ----------------------------------------------------------
class Foo:

	def f1(self):
		print("666")
		return 123

	def f2(self,v):
		print(v)

	def f3(self):
		print("del")

	per = property(fget=f1,fset=f2,fdel=f3)

obj = Foo()
ret = obj.per
print(ret)
obj.per = 1212
del obj.per