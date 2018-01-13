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
# _user="JingXu"
# _passwd="123456"
# for i in range(3):
# 	username = input("Username:")
# 	password = input("Password:")
# 	if username == _user and password == _passwd :
# 		print("Welcome %s login......" % _user)
# 		break
# 	else:
# 		print("Invalid username or password!")
# else:
# 	print("Login failed!")
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
# 	counter += 1
# 	if counter == 3:
# 		keep_going_choice = input("Try again?[Y/N]")
# 		if keep_going_choice == "Y" or keep_going_choice == "y":
# 			counter = 2
# else:
# 	print("Login failed!")
# --------------------------------------------------------------------------------------------------
exit_flag = False
for i in range(10):
	if i < 5:
		continue
	print(i)
	for j in range(10):
		print("layer2",j)
		if j == 6:
			exit_flag = True
			break
	if exit_flag:
		break
# --------------------------------------------------------------------------------------------------