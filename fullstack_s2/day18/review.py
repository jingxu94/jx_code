#__author:  "Jing Xu"
#date:  2018/1/19

import random

print("Start")

login_status = False

def login(func):
	def inner(*args,**kwargs):
		global login_status
		if not login_status:
			msg1='''请选择登录方式：
			1.京东账号密码登陆
			2.微信账号登录
			>>>:'''
			auth_type = int(input(msg1))
			if not (auth_type == 1 or auth_type == 2 ):
				print("输入参数有误！")
				inner()
			login_flag = True
			while login_flag:
				username = input("username:")
				passward = input("passwd:")
				vcode_flag = True
				while vcode_flag:
					verification_code = v_code()
					print(verification_code)
					icode = input("verification_code(Enter [R] to refresh):")
					if icode != 'R' and icode != 'r':
						vcode_flag = False
				if icode == verification_code:
					if auth_type == 1:
						with open("User_Jingdong", "r") as f1:
							for user_passwd in f1:
								if " ".join([username, passward]) == user_passwd.strip():
									print("Welcome ...")
									login_flag = False
									login_status = True

					else:
						with open("User_Weixin", "r") as f2:
							for user_passwd in f2:
								if " ".join([username, passward]) == user_passwd.strip():
									print("Welcome ...")
									login_flag = False
									login_status = True

					if login_flag == True:
						print("账号密码有误")

				else:
					print("验证码错误")
		func(*args,**kwargs)
	return inner

def v_code():
	code = ''
	for i in range(5):
		add_str = random.choice([str(random.randrange(10)),chr(random.randrange(65,91)),chr(random.randrange(97,123))])
		code += add_str
	return code

@login
def home():
	print("Welcome to home page")
@login
def finance():
	print("Welcome to finance page")
@login
def book():
	print("Welcome to book page")

finance()
home()
book()