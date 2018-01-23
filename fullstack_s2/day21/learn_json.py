#__author:  "Jing Xu"
#date:  2018/1/23

import json

dict1 = {'name':'alex','age':'18'}
data = json.dumps( dict1 )

with open('JSON_text','w') as f:
	f.write(data)

with open('JSON_text','r') as f1:
	data1 = json.loads( f1.read() )

print(data1['name'])

def foo():
	print("ok")

# data2 = json.dumps( foo )	# Object of type 'function' is not JSON serializable