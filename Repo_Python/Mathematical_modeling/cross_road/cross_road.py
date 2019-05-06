# @Time : 2018/4/30 20:24 
# @Author : Jing Xu

import time
import pandas as pd

# def timestamp_datetime(value):
# 	format = '%Y-%m-%d %H:%M:%S'
# 	# value为传入的值为时间戳(整形)，如：1332888820
# 	value = time.localtime(value)
# 	## 经过localtime转换后变成
# 	## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
# 	# 最后再经过strftime函数转换为正常日期格式。
# 	dt = time.strftime(format, value)
# 	return dt
#
# def datetime_timestamp(dt):
# 	#dt为字符串
# 	#中间过程，一般都需要将字符串转化为时间数组
# 	time.strptime(dt, '%Y-%m-%d %H:%M:%S')
# 	## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
# 	#将"2012-03-28 06:53:40"转化为时间戳
# 	s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
# 	return int(s)
#
def road_silt(T, tga, tgb, tgc, tgd, ua, ub, uc, ud):
	silta = ua * (tgb+tgc+tgd)
	siltb = ub * (tga+tgc+tgd)
	siltc = uc * (tga+tgb+tgd)
	siltd = ud * (tga+tgb+tgc)
	return {"siltsum":(silta+siltb+siltc+siltd)/T, "silta":silta, "siltb":siltb, "siltc":siltc, "siltd":siltd}
#
# def braking_distance(v):
# 	return v*v/(2.0*9.8*0.8)
#
# t1 = datetime_timestamp("2018-03-25 00:00:00") - 3600
# t2 = t1 + 3600
#
# df=pd.read_csv('part-00000-0d0c6b9b-7325-4e92-a18f-efe95f305852.csv',names=["时间",'车牌','经度','纬度','行驶速度','卫星速度'])
# dict_data = df.to_dict(orient="records")

widtha = 1
widthb = 1
widthc = 1
widthd = 1
loop_time = 200
tga, tgb = 55, 70
tgc, tgd = 65, 50
road, roada, roadb, roadc, roadd = 0, 0, 0, 0, 0
road_list, roada_list, roadb_list, roadc_list, roadd_list = [], [], [], [], []
ratio, ratioa, ratiob, ratioc, ratiod = [], [], [], [], []
ua, ub, uc, ud = 1.8, 3.6, 2.2, 1.5

for j in range(12):
	# t1 = t1 + 3600
	# t2 = t2 + 3600
	# suma, vela = 0, 0
	# sumb, velb = 0, 0
	# sumc, velc = 0, 0
	# sumd, veld = 0, 0
	# for i in range(len(dict_data)-1):
	#
	# 	if t1 < dict_data[i]["时间"] < t2:
	# 		if 114.026033 < dict_data[i]["经度"] < 114.027542 and 22.55897 < dict_data[i]["纬度"] < 22.562241:
	# 			suma += 1
	# 			vela += dict_data[i]["行驶速度"]
	# 		elif 114.026931 < dict_data[i]["经度"] < 114.030704 and 22.553863 < dict_data[i]["纬度"] < 22.558269:
	# 			sumb += 1
	# 			velb += dict_data[i]["行驶速度"]
	# 		elif 114.022116 < dict_data[i]["经度"] < 114.026033 and 22.557968 < dict_data[i]["纬度"] < 22.559303:
	# 			sumc += 1
	# 			velc += dict_data[i]["行驶速度"]
	# 		elif 114.027542 < dict_data[i]["经度"] < 114.03286 and 22.558603 < dict_data[i]["纬度"] < 22.55897:
	# 			sumd += 1
	# 			veld += dict_data[i]["行驶速度"]
	# vela /= suma
	# velb /= sumb
	# velc /= sumc
	# veld /= sumd
	#
	# ua = (braking_distance(vela) + 3) * suma / widtha / 300
	# ub = (braking_distance(velb) + 3) * sumb / widthb / 300
	# uc = (braking_distance(velc) + 3) * sumc / widthc / 300
	# ud = (braking_distance(veld) + 3) * sumd / widthd / 300
	ua *= 1.1
	ub *= 1.1
	uc *= 1.1
	ud *= 1.1

	road = road_silt(loop_time, tga, tgb, tgc, tgd, ua, ub, uc, ud)["siltsum"]
	roada = road_silt(loop_time, tga, tgb, tgc, tgd, ua, ub, uc, ud)["silta"]
	roadb = road_silt(loop_time, tga, tgb, tgc, tgd, ua, ub, uc, ud)["siltb"]
	roadc = road_silt(loop_time, tga, tgb, tgc, tgd, ua, ub, uc, ud)["siltc"]
	roadd = road_silt(loop_time, tga, tgb, tgc, tgd, ua, ub, uc, ud)["siltd"]

	road_list.append(road)
	roada_list.append(roada)
	roadb_list.append(roadb)
	roadc_list.append(roadc)
	roadd_list.append(roadd)

for i in range(len(road_list)-2):
	ratio.append(road_list[i + 1]/road_list[i])
	ratioa.append(roada_list[i + 1] / roada_list[i])
	ratiob.append(roadb_list[i + 1] / roadb_list[i])
	ratioc.append(roadc_list[i + 1] / roadc_list[i])
	ratiod.append(roadd_list[i + 1] / roadd_list[i])

print(road_list)
print(roada_list)
print(roadb_list)
print(roadc_list)
print(roadd_list)

print(ratio)
print(ratioa)
print(ratiob)
print(ratioc)
print(ratiod)