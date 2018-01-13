#__author:  "Jing Xu"
#date:  2018/1/13
# --------------------------------------------------------------------------------------------------
# names=["wuchao","jinxin","xiaohu","sanpang","ligang"]
# print(names[1:-1])
# print(names[1::2])
# print(names[3::-2])
# names.append("xuepeng")
# print(names)
# names.insert(1,"jingxu")
# print(names)
# names[1:3]=["James","Jane"]
# print(names)
# # names.remove("James")
# b=names.pop(1)
# print(names)
# print(b)
# --------------------------------------------------------------------------------------------------
# t = ["to","be","or","not","to","be","to"].count("to")
# print(t)
# --------------------------------------------------------------------------------------------------
# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)
# print(a.index(6))
# --------------------------------------------------------------------------------------------------
# x = [4,6,3,1,8,5,7,7]
# x.sort(reverse=True)
# print(len(x))
# --------------------------------------------------------------------------------------------------
names = ["to","be","or","not","to","be","to"]
name_search = "to"
remaining_names = names
position = 0
while ( name_search in remaining_names ):
	position = position + remaining_names.index( name_search ) + 1
	print( "Find object in:" , position - 1 )
	remaining_names = names[position:]
# --------------------------------------------------------------------------------------------------