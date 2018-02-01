#__author:  "Jing Xu"
#date:  2018/2/1

import pickle
import uuid

class School:

	def __init__(self, name):
		self.name = name
		self.schoolid = uuid.uuid1()

	def __str__(self):
		return self.name

	def save(self):
		pickle.dump((open(xxx), "wb"), self)

	@staticmethod
	def get_all():
		obj_list = []
		for item in xxx:
			obj = pickle.load(item)
			obj_list.append(obj)
		return obj_list


class Classes:

	def __init__(self, name):
		self.name = name
		self.classid = uuid.uuid1()

	def save(self):
		pass

	@staticmethod
	def get_all():
		pass


class Student:

	def __init__(self, name, classes_name):
		self.name = name
		self.classes_name = classes_name
