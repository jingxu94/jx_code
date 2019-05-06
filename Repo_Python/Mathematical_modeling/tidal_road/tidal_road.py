# @Time : 2018/4/30 11:44 
# @Author : Jing Xu

import time
import numpy as np
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
	time.strptime(dt, '%Y/%m/%d %H:%M:%S')
	## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
	#将"2012-03-28 06:53:40"转化为时间戳
	s = time.mktime(time.strptime(dt, '%Y/%m/%d %H:%M:%S'))
	return int(s)

def excel_unix(value):
	'''
	将Excel时间转换为Unix时间戳
	:param value: Excel时间，1900时间表示法
	:return: Unix时间戳
	'''
	return int((value-25569)*86400-28800)

df1=pd.read_csv('xmh-2018-3-30-south.csv',names=["车牌号码","车牌颜色","时间","监测点名称","车道ID"])
df2=pd.read_csv('xmh-2018-3-30-north.csv',names=["车牌号码","车牌颜色","时间","监测点名称","车道ID"])
dict_data1 = df1.to_dict(orient="records")
dict_data2 = df2.to_dict(orient="records")

# print(dict_data1[0]["车牌号码"])
# print(timestamp_datetime(excel_unix(dict_data1[1]["时间"])))

south_list = []
north_list = []

t1 = datetime_timestamp("2018/03/30 00:00:00") - 3600
t2 = t1 + 3600

for j in range(24):
	t1 = t1 + 3600
	t2 = t2 + 3600

	south_sum = 0
	north_sum = 0

	for i in range(len(dict_data1)-1):
		if t1 < excel_unix(dict_data1[i]["时间"]) < t2:
			south_sum += 1
		if t1 < datetime_timestamp(dict_data2[i]["时间"]) < t2:
			north_sum += 1
	south_list.append(south_sum)
	north_list.append(north_sum)


total_width, n = 1.6, 2
width = total_width / n
x = list(range(len(south_list)))
for i in range(len(south_list)):
	x[i] = 2*x[i]
labels = []
for i in range(24):
	labels.append(str(i))

plt.bar(x, south_list, width=width, label='south',fc = 'b')
for i in range(len(x)):
	x[i] = x[i] + width
plt.bar(x, north_list, width=width, label='north',fc = 'r')

plt.xticks(x, labels, rotation=0)
plt.legend()
plt.show()