#__author:  "Jing Xu"
#date:  2018/1/12
# --------------------------------------------------------------------------------------------------
# name = input("Name:")
# age = int(input("Age:"))
# job = input("Job:")
# salary = input("Salary:")
# if salary.isdigit():
# 	salary = int(salary)
# else:
# 	exit("must input digit")
# msg = '''
# ---- info of %s ----
# Name: %s
# Age : %s
# Job : %s
# Salary: %s
# You will be retired in %s years
# --------- end --------
# ''' % (name,name,age,job,salary,65-age)
# print(msg)
# --------------------------------------------------------------------------------------------------
_user="JingXu"
_passwd="123456"
for i in range(3):
	username = input("Username:")
	password = input("Password:")
	if username == _user and password == _passwd :
		print("Welcome %s login......" % _user)
		break
	else:
		print("Invalid username or password!")
else:
	print("Login failed!")
# --------------------------------------------------------------------------------------------------
# _user="JingXu"
# _passwd="123456"
# counter = 0
# while counter < 3:
# 	username = input("Username:")
# 	password = input("Password:")
# 	if username == _user and password == _passwd :
# 		print("Welcome %s login......" % _user)
# 		break
# 	else:
# 		print("Invalid username or password!")
# else:
# 	print("Login failed!")









































