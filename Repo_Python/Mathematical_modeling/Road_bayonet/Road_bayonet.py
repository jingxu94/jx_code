# @Time : 2018/4/30 10:37 
# @Author : Jing Xu

import time
import matplotlib.pyplot as plt
import pandas as pd

def timestamp_datetime(value):
	format = '%Y-%m-%d %H:%M:%S'
	# value为传入的值为时间戳(整形)，如：1332888820
	value = time.localtime(value)
	## 经过localtime转换后变成
	## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
	# 最后再经过strftime函数转换为正常日期格式。
	dt = time.strftime(format, value)
	return dt

def datetime_timestamp(dt):
	#dt为字符串
	#中间过程，一般都需要将字符串转化为时间数组
	time.strptime(dt, '%Y-%m-%d %H:%M:%S')
	## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
	#将"2012-03-28 06:53:40"转化为时间戳
	s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
	return int(s)

def excel_unix(value):
	'''
	将Excel时间转换为Unix时间戳
	:param value: Excel时间，1900时间表示法
	:return: Unix时间戳
	'''
	return int((value-25569)*86400-28800)

df1=pd.read_csv('2018-3-30.csv',names=["车牌号码","车牌颜色","时间","监测点名称","车道ID"])

dict_data = df1.to_dict(orient="records")

license_list = []

t1 = datetime_timestamp("2018-03-30 00:00:00") - 3600
t2 = t1 + 3600

for j in range(24):
	t1 = t1 + 3600
	t2 = t2 + 3600
	license_plate = {"blue": 0, "yellow": 0, "black": 0, "white": 0, "others": 0}

	for i in range(len(dict_data)-1):
		if excel_unix(dict_data[i]["时间"]) > t1 and excel_unix(dict_data[i]["时间"]) < t2:
			if dict_data[i]["车牌颜色"] == "蓝牌":
				license_plate["blue"] += 1
			elif dict_data[i]["车牌颜色"] == "黄牌":
				license_plate["yellow"] += 1
			elif dict_data[i]["车牌颜色"] == "黑牌":
				license_plate["black"] += 1
			elif dict_data[i]["车牌颜色"] == "白牌":
				license_plate["white"] += 1
			else:
				license_plate["others"] += 1
	license_list.append(license_plate)
	# print(license_plate)

blue_list = []
yellow_list = []
black_list = []
white_list = []
others_list = []
for i in range(24):
	blue_list.append(license_list[i]["blue"])
	yellow_list.append(license_list[i]["yellow"])
	black_list.append(license_list[i]["black"])
	white_list.append(license_list[i]["white"])
	others_list.append(license_list[i]["others"])

total_width, n = 1.5, 5
width = total_width / n
x = list(range(len(license_list)))
for i in range(len(license_list)):
	x[i] = 2*x[i]
labels = []
for i in range(24):
	labels.append(str(i))

plt.bar(x, blue_list, width=width, label='blue',fc = 'b')
for i in range(len(x)):
	x[i] = x[i] + width
plt.bar(x, yellow_list, width=width, label='yellow',fc = 'y')
for i in range(len(x)):
	x[i] = x[i] + width
plt.bar(x, black_list, width=width, label='black',fc = 'm')
for i in range(len(x)):
	x[i] = x[i] + width
plt.bar(x, white_list, width=width, label='white',fc = 'w')
for i in range(len(x)):
	x[i] = x[i] + width
plt.bar(x, others_list, width=width, label='others',fc = 'c')
plt.xticks(x, labels, rotation=0)
plt.legend()
plt.savefig("license_plate_2018-03-30.png")
plt.show()