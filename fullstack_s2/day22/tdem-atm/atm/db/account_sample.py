#__author:  "Jing Xu"
#date:  2018/1/25

import json
acc_dic = {
    'id': 1001,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

acc_dic1 = {
    'id': 1002,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

acc_dic2 = {
    'id': 1003,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

acc_dic3 = {
    'id': 1004,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

acc_dic4 = {
    'id': 1005,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

with open("1001.json",'w') as f1:
    f1.write(json.dumps(acc_dic))

with open("1002.json",'w') as f2:
    f2.write(json.dumps(acc_dic1))

with open("1003.json",'w') as f3:
    f3.write(json.dumps(acc_dic2))

with open("1004.json",'w') as f4:
    f4.write(json.dumps(acc_dic3))

with open("1005.json",'w') as f5:
    f5.write(json.dumps(acc_dic4))

