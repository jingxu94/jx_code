#__author:  "Jing Xu"
#date:  2018/1/20
#Python解释器进行交互

import sys,os
# --------------------------------------------------------------
# print(sys.argv)
#
# def post():
# 	print('ok')
#
# def download():
# 	pass
#
# if sys.argv[1] == 'post':
# 	post()
# elif sys.argv[1] == 'download':
# 	download()
# --------------------------------------------------------------
# print(sys.path)
# print(sys.platform)
# --------------------------------------------------------------
if sys.platform == 'win32':
	os.system('dir')
else:
	os.system('ls')