# @Time : 2018/4/28 21:20 
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
	time.strptime(dt, '%Y-%m-%d %H:%M:%S')
	## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
	#将"2012-03-28 06:53:40"转化为时间戳
	s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
	return int(s)

t1 = datetime_timestamp("2018-03-25 00:00:00") - 3600
t2 = t1 + 3600

# print(max(np.random.random(10)))

df=pd.read_csv('part-00000-0d0c6b9b-7325-4e92-a18f-efe95f305852.csv',names=["时间",'车牌','经度','纬度','行驶速度','卫星速度'])

dict_data = df.to_dict(orient="records")
# print(type(dict_data))
# print(dict_data[0]["时间"])
# print(dict_data[1])
# print(len(dict_data))

for j in range(24):
	t1 = t1 + 3600
	t2 = t2 + 3600

	x_list = []
	y_list = []
	v_list = []

	xlow_list = []
	ylow_list = []
	vlow_list = []

	for i in range(len(dict_data)-1):
		if dict_data[i]["时间"] > t1 and dict_data[i]["时间"] < t2:
			x_list.append(dict_data[i]["经度"])
			y_list.append(dict_data[i]["纬度"])
			v_list.append(dict_data[i]["行驶速度"])
			if dict_data[i]["行驶速度"] < 10:
				xlow_list.append(dict_data[i]["经度"])
				ylow_list.append(dict_data[i]["纬度"])
				vlow_list.append(dict_data[i]["行驶速度"])

	plt.figure(j+1)

	plt.scatter(x_list, y_list, c=v_list, alpha=0.8)
	# plt.xlim(114.003,114.061803)
	# plt.ylim(22.550567,22.57408)
	if x_list == []:
		continue
	plt.xlim(min(x_list),max(x_list))
	plt.ylim(min(y_list),max(y_list))

	# plt.scatter(xlow_list, ylow_list, c=vlow_list, alpha=0.8)
	# # plt.xlim(114.003,114.061803)
	# # plt.ylim(22.550567,22.57408)
	# plt.xlim(min(x_list),max(x_list))
	# plt.ylim(min(y_list),max(y_list))
	plt.savefig("".join([str(j),".png"]))

# plt.show()