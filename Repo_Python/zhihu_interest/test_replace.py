# @Time : 2018/6/6 21:53 
# @Author : Jing Xu

import os

file_dir = "./40/"

for dirs in os.walk(file_dir):
	# print(root) #当前目录路径
	# print(dirs) #当前路径下所有子目录
	# print(files) #当前路径下所有非目录子文件
	for directory in dirs:
		# print(directory)
		for dir1 in directory:
			for names in os.walk(dir1):
				if names == "input.dat":
					print(names)
					f = open(names, 'r+', encoding='gbk')
					all_the_lines = f.readlines()
					# print(all_the_lines)
					for line in all_the_lines:
						str1 = '40    !// 脉宽'
						print(666)
						str2 = '50    !// 脉宽'
						f.write(line.replace(str1, str2))
					f.close()



