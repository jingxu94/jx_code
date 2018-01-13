#__author:  "Jing Xu"
#date:  2018/1/13

menu = {
	'北京':{
		'朝阳':{
			'国贸':{
				'CICC':{},
				'HP':{},
				'CCTV':{},
			},
			'望京':{
				'陌陌':{},
				'奔驰':{},
				'360':{},
			},
			'三里屯':{
				'优衣库':{},
				'apple':{},
			},
		},
		'昌平':{
			'沙河':{
				'老男孩':{},
				'阿泰包子':{},
			},
			'天通苑':{
				'链家':{},
				'我爱我家':{},
			},
			'回龙观':{},
		},
		'海淀':{
			'五道口':{
				'谷歌':{},
				'网易':{},
				'搜狐':{},
				'快手':{},
				'sogo':{},
			},
			'中关村':{
				'youku':{},
				'Iqiyi':{},
				'QQ':{},
			},
		},
	},
	'上海':{
		'浦东':{
			'陆家嘴':{
				'CICC':{},
				'高盛':{},
				'摩根':{},
			},
			'外滩':{},
		},
		'闵行':{},
		'静安':{},
	},
	'山东':{
		'济南':{},
		'德州':{
			'乐陵':{
				'丁务镇':{},
				'城区':{},
			},
			'平原县':{},
		},
		'青岛':{},
	},
}

back_flag = False
exit_flag = False
while not back_flag and not exit_flag:
	for key in menu:
		print(key)
	choice1 = input(">>:").strip()
	if choice1 == "q":
		exit_flag = True
	if choice1 in menu:
		while not back_flag and not exit_flag:
			for key2 in menu[choice1]:
				print(key2)
			choice2 = input(">>:").strip()
			if choice2 == "b":
				back_flag = True
			if choice2 == "q":
				exit_flag = True
			if choice2 in menu[choice1]:
				while not back_flag and not exit_flag:
					for key3 in menu[choice1][choice2]:
						print(key3)
					choice3 = input(">>:").strip()
					if choice3 == "b":
						back_flag = True
					if choice3 == "q":
						exit_flag = True
					if choice3 in menu[choice1][choice2]:
						while not back_flag and not exit_flag:
							for key4 in menu[choice1][choice2][choice3]:
								print(key4)
							print("last level")
							choice4 = input(">>:").strip()
							# print("last level")
							if choice4 == "b":
								back_flag = True
							if choice4 == "q":
								exit_flag =True
						else:
							back_flag = False
				else:
					back_flag = False
		else:
			back_flag = False
else:
	back_flag = False