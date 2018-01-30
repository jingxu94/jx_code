#__author:  "Jing Xu"
#date:  2018/1/30

class Teacher:

	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

class Course:

	def __init__(self, name, cost, teacher):
		self.name = name
		self.cost = cost
		self.teacher = teacher

	def class_up(self):
		self.teacher.salary += self.cost


t1 = Teacher("alex", 31, 1000)
t2 = Teacher("eric", 25, 1000)
c1 = Course("Python", 4000, t1)
print(c1.teacher.name)
print(c1.teacher.age)
print(c1.teacher.salary)
c1.class_up()
print(c1.teacher.salary)