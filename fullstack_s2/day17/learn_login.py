#__author:  "Jing Xu"
#date:  2018/1/18

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
			username = input("username:")
			passward = input("passwd:")

			if auth_type == 1:
				with open( "User_Jingdong","r" ) as f1:
					for user_passwd in f1:
						if " ".join([username,passward]) == user_passwd.strip():
							print("Welcome ...")

							login_status = True
			else:
				with open( "User_Weixin","r" ) as f2:
					for user_passwd in f2:
						if " ".join([username,passward]) == user_passwd.strip():
							print("Welcome ...")

							login_status = True
		func(*args,**kwargs)
	return inner

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