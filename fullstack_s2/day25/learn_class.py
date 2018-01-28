#__author:  "Jing Xu"
#date:  2018/1/28
# --------------------------------------------------------------------
# class Foo:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.__age = age    #私有字段，外部无法直接访问
#
# 	def show(self):
# 		return self.__age
#
# obj = Foo("alex",19)
# print(obj.name)
# print(obj.show())
# --------------------------------------------------------------------
# class Foo:
# 	__v = "123"
#
# 	def __init__(self):
# 		pass
#
# 	def show(self):
# 		return Foo.__v
#
# 	@staticmethod
# 	def stat():
# 		return Foo.__v
#
#
# ret = Foo()
# print(ret.show())
# ret = Foo.stat()
# print(ret)
# --------------------------------------------------------------------
# '''
# 成员修饰符
# 	共有成员
# 	私有成员，__字段名
# 		- 无法直接访问，只能间接访问
# '''
# class Foo:
#
# 	def __f1(self):
# 		return 123
#
# 	def f2(self):
# 		r = self.__f1()
# 		return r
#
# obj = Foo()
# ret = obj.f2()
# print(ret)
# --------------------------------------------------------------------
# class F:
# 	def __init__(self):
# 		self.ge = 1212
# 		self.__game = 123
#
# class S(F):
#
# 	def __init__(self, name):
# 		self.name = name
# 		self.__age = 18
# 		super(S, self).__init__()
#
# 	def show(self):
# 		print(self.name)
# 		print(self.__age)
# 		print(self.ge)
# 		print(self.__game)    #无法访问父类的私有字段
#
# s = S("alex")
# s.show()
# --------------------------------------------------------------------
# '''
# 类的特殊用法，对象后面跟括号，执行类中的特殊方法：__call__(self, *args, **kwargs)
# '''
# class Foo:
#
# 	def __init__(self):
# 		print("init")
#
# 	def __call__(self, *args, **kwargs):
# 		print("call")
#
#
# obj = Foo()
# obj()
# --------------------------------------------------------------------
# class Foo:
#
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def __int__(self):
# 		return 111
#
# 	def __str__(self):
# 		return "%s-%s" %(self.name, self.age)
#
#
# obj = Foo("alex", 18)
# print(obj, type(obj))
# print(int(obj))
# print(str(obj))
# --------------------------------------------------------------------
# class Foo:
# 	'''
# 	当前类的作用是：
# 	'''
#
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def __add__(self, other):
# 		return Foo( "%s-%s" %(self.name, other.name), self.age + other.age )
#
# 	def __del__(self):
# 		print("析构方法")   #对象被销毁时，自动执行
#
#
#
# obj1 = Foo("alex", 18)
# obj2 = Foo("eric", 66)
#
# r = obj1 + obj2
# print( r.name )
# print( r.age )
# print( type(r) )
# print( Foo.__dict__)
# --------------------------------------------------------------------
# li = list([11, 22, 33, 44])
# r1 = li[3]
# print(r1)
# li[3] = 666
# del li[2]
# print(li)
# --------------------------------------------------------------------
'''
特殊成员：
    __init__ 类()自动执行
    __call__ 对象() 类()()自动执行
    __int__  str(对象)，得到返回值
    __str__  int(对象)，得到返回值
    __add__  +，其他运算同理
    __del__  析构方法，当对象被销毁时自动执行
    __dict__ 将对象中封装的所有内容通过字典的形式返回
    __getitem__
    __setitem__
    __delitem__
    __iter__
'''
class Foo:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __getitem__(self, item):
		if type(item) == slice:
			print("采用切片处理")
		else:
			print("采用索引处理")

	def __setitem__(self, key, value):
		print(key, value)

	def __delitem__(self, key):
		print(key)

	def __iter__(self):
		print("666")
		return iter([11,22,33])

li = Foo("alex",18)
# r = li[8]   # 自动执行li类对象的类中的__getitem__方法，8当做参数传递给item
# p = li[1:4:2]
# print(r)
# li[100] = "abcd"
# del li[999]
# --------------------------------------------------------------------
# 如果类中有__iter__方法，对象是可迭代对象
# 对象.__iter__()的返回值：迭代器
# for循环，迭代器，next
# for循环，可迭代对象，对象.__iter__()，迭代器，next
# 1、执行li对象的类Foo中的__iter__方法，并获取返回值
# 2、循环上一步中返回的对象
for i in li:
	print(i)
