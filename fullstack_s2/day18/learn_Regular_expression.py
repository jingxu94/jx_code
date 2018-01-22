#__author:  "Jing Xu"
#date:  2018/1/21
# -----------------------------------------------------------------
# s = "hello world"
# print(s.find("ll"))
# ret = s.replace("ll","xx")
# print(ret)
# print(s.split("w"))
# -----------------------------------------------------------------
import re
ret1 = re.findall("w...d","hello world")
print(ret1)
ret2 = re.findall("alex","alexalexalex")
print(ret2)
ret3 = re.findall('ba*','urtseoutksafaabaaaadf')
print(ret3)
ret4 = re.findall('a+b','aaaabbbfabdh')
print(ret4)
ret5 = re.findall('a?b','aaaaabhghabfkbbd')
print(ret5)
ret6 = re.findall('a{1,5}b','aaaaaabbb')
print(ret6)
ret7 = re.findall('a[c,d]x','acx')
print(ret7)
ret8 = re.findall('[1-9,a-z,A-Z]','12tyAS')
print(ret8)
ret9 = re.findall('[^t12]','iu12tyAiiuS')
print(ret9)