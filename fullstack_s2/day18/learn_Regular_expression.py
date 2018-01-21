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
ret = re.findall("w...d","hello world")
print(ret)
# ret = re.findall("alex","alexalexalex")
# print(ret)