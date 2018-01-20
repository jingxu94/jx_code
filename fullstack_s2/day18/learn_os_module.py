#__author:  "Jing Xu"
#date:  2018/1/19

import os
# ----------------------------------------------------------------------
# print(os.getcwd())
# print(os.curdir)
# print(os.pardir)
# os.chdir(r'D:\\')
# # os.makedirs('abc\\alex')
# os.removedirs('abc\\alex')	#只能删除空文件夹
# ----------------------------------------------------------------------
# os.mkdir('dir1')
# os.mkdir('dir1\\dir2')
# ----------------------------------------------------------------------
# os.rmdir('dir1\\dir2')
# os.rmdir('dir1')
# ----------------------------------------------------------------------
# print(type(os.listdir()))
# print(os.listdir(r'..'))
info = os.stat('.\\review.py')
print(info.st_size)
print(info)
# print(os.path.dirname('.\\review.py'))
# os.path.join([a,b])