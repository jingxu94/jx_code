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

current_layer = menu #实现动态循环
parent_layers = [] #保存所有上一级字典

while True:
	for key in current_layer:
		print( key )
	choice = input(">>>:").strip()
	if len(choice) == 0: continue
	if choice in current_layer:
		parent_layers.append( current_layer )
		current_layer = current_layer[ choice ]
	elif choice == "b":
		if parent_layers:
			current_layer = parent_layers.pop() #列表最后一个元素就是当前的上一级字典目录
	elif choice == "q":
		break
	else:
		print( "无此项" )