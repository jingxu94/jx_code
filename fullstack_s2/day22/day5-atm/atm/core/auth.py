#__author:  "Jing Xu"
#date:  2018/1/25

import os,sys
from core import db_handler
from conf import settings
from core import logger
import json
import time
import random

def v_code():
	code = ''
	for i in range(5):
		add_str = random.choice([str(random.randrange(10)),chr(random.randrange(65,91)),chr(random.randrange(97,123))])
		code += add_str
	return code

def acc_auth(account,password):
    '''
    account auth func
    :param account: credit account number
    :param password: credit card password
    :return: if passed the authentication , retun the account object, otherwise ,return None
    '''
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = "%s/%s.json" %(db_path,account)
    print(account_file)
    if os.path.isfile(account_file):
        with open(account_file,'r') as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                exp_time_stamp = time.mktime(time.strptime(account_data['expire_date'], "%Y-%m-%d"))
                if time.time() > exp_time_stamp:
                    print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
                else: #passed the authentication
                    return  account_data
            else:
                print("\033[31;1mAccount ID or password is incorrect!\033[0m")
    else:
        print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)

def acc_login(user_data,log_obj):
    '''
    account login func
    :user_data: user info data , only saves in memory
    :return:
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3 :
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        vcode_flag = True
        while vcode_flag:
            verification_code = v_code()
            print("\033[32;1m [%s] \033[0m" % verification_code)
            vcode = input("\033[31;1mverification_code(Enter [R] to refresh):\033[0m")
            if vcode != 'R' and icode != 'r':
                vcode_flag = False
        if vcode == verification_code:
            auth = acc_auth(account, password)
            if auth: #not None means passed the authentication
                user_data['is_authenticated'] = True
                user_data['account_id'] = account
                print("welcome")
                return auth
            retry_count +=1
    else:
        log_obj.error("account [%s] too many login attempts" % account)
        exit()

def acc_logout(user_data, acc_data):
    while user_data['is_authenticated'] is True:
        key = input("\033[32;1mPress [y] to logout,[b] to back:\033[0m")
        if key == "b" or key == "B":
            return acc_data
        elif key == "y" or key == "Y":
            user_data['is_authenticated'] = False
            user_data['account_id'] = None
            acc_data = None
            sys.exit()

