# @Time : 2018/4/29 17:05 
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

t1 = datetime_timestamp("2018-03-25 00:00:00") - 3600
t2 = t1 + 3600

df=pd.read_csv('part-00000-0d0c6b9b-7325-4e92-a18f-efe95f305852.csv',names=["时间",'车牌','经度','纬度','行驶速度','卫星速度'])

dict_data = df.to_dict(orient="records")

v = []
flag_list = []

for j in range(23):
	t1 = t1 + 3600
	t2 = t2 + 3600

	v_list = []
	flag = 0

	for i in range(len(dict_data)-1):

		if t1 < dict_data[i]["时间"] < t2 and 114.04249 < dict_data[i]["经度"] < 114.047053 and 22.557668 < dict_data[i]["纬度"] < 22.561974:
			flag += 1
			v_list.append(dict_data[i]["行驶速度"])
	v.append(sum(v_list)//len(v_list))
	flag_list.append(flag)

ratio = []

for i in range(len(v)):
	ratio.append(flag_list[i]/v[i])
	v[i] = v[i]*100

total_width, n = 0.9, 3
width = total_width / n
x = list(range(len(v)))

plt.bar(x, v, width=width, label='velocity',fc = 'y')
for i in range(len(x)):
	x[i] = x[i] + width
plt.bar(x, flag_list, width=width, label='number',fc = 'r')
for i in range(len(x)):
	x[i] = x[i] + width
plt.bar(x, ratio, width=width, label='ratio',fc = 'b')
plt.legend()
plt.savefig("jamroad_2018-03-25.png")
plt.show()

