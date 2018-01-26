#__author:  "Jing Xu"
#date:  2018/1/25

import os,time
import json
from core import db_handler
from conf import settings

def add_account():
	db_path = db_handler.db_handler(settings.DATABASE)
	id = input("\033[32;1maccount_id:\033[0m").strip()
	if not os.path.isfile( "%s/%s.json" %( db_path, id ) ):
		password = input("\033[32;1mpassword:\033[0m").strip()
		credit = input("\033[32;1mcredit:\033[0m").strip()
		balance = input("\033[32;1mbalance:\033[0m").strip()
		expire_date = input("\033[32;1mexpire_date:\033[0m")
		acc_dic = {
			'id': int(id),
			'password': password,
			'credit': int(credit),
			'balance': int(balance),
			'enroll_date': time.strptime("%Y-%m-%d",time.localtime()),
			'expire_date': expire_date,
			'pay_day': 22,
			'status': 0  # 0 = normal, 1 = locked, 2 = disabled
		}
		account_file = "%s/%s.json" %( db_path, id )
		with open(account_file,"w") as f:
			f.write(json.dumps(acc_dic))
	else:
		print("\033[31;1m账户id已存在\033[0m")