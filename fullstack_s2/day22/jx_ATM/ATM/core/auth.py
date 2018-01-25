#__author:  "Jing Xu"
#date:  2018/1/24

import os, time
import json



user_data = {
	"account_id" : None,
	"is_authenticated" : False,
	"account_data" : None
}


def acc_auth():
	db_path = db_handler.db_handler(settings.DATABASE)
	account_file = "%s/%s.json" % ( db_path, account )
	print( account_file )
	if os.path.isfile( account_file ):
		with open( account_file, "r" ) as f:
			account_data = json.load(f)
			if account_data["password"] == password:
				exp_time_stamp = time.mktime( time.strptime( account_data["expired"] ) )
				if time.time() > exp_time_stamp:
					print("\033[31;1mAccount [%s] has expired,please contact the manager.")
				else:
					return account_data
			else:
				print("\033[31;1mAccount ID or password is incorrect!\033[0m")
	else:
		print("\033[31;1mAccount [%s] does not exist!\033[0m" % account)







def acc_login( user_data, log_obj ):
	retry_count = 0
	while user_data["is_authenticated"] is not True and retry_count < 3:
		account = input("\033[32;1maccount:\033[0m").strip()
		password = input("\033[32;1mpassword:\033[0m").strip()
		auth = acc_auth( account, password )
		if auth:
			user_data["is_authenticated"] = True
			user_data["account_id"] = account
			return auth
		retry_count += 1
	else:
		log_obj.error("account [%s] too many login attemps" % account)
		exit()
