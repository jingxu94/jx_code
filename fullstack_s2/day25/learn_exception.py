#__author:  "Jing Xu"
#date:  2018/1/29

'''
try:
	代码块，逻辑
	pass
except Exception(IndexError/ValueError/IOError...) as e:
	上述代码块如果出错，自动执行当前块的内容

assert条件，条件成立通过，不成立报错，并且可以捕获
'''
try:
	int("78r")
except IndexError as e:
	print("IndexError", e)
except ValueError as e:
	print("ValueError", e)
except Exception as e:
	print("Exception", e)
else:
	print("Else")
finally:
	print("...")
# --------------------------------------------------------------------
class TdemError(Exception):

	def __init__(self, msg):
		self.message = msg

	def __str__(self):
		return self.message


obj = TdemError("xxx")
print(obj)
try:
	raise TdemError("Error")
except TdemError as e:
	print(e)    #e对象的__str__()方法，获取返回
# --------------------------------------------------------------------

