#__author:  "Jing Xu"
#date:  2018/1/20

import hashlib
# --------------------------------------------------------------
# m = hashlib.md5()
# print(m)
# m.update('hello world'.encode('utf8'))
# print(m.hexdigest())
# m.update('alex'.encode('utf8'))
# print(m.hexdigest())
# m2 = hashlib.md5()
# m2.update('hello worldalex'.encode('utf8'))
# print(m2.hexdigest())
# print(type(m2))
# print(type(m2.hexdigest()))
# --------------------------------------------------------------
s = hashlib.sha256()
s.update('hello world'.encode('utf8'))
print(s.hexdigest())
# --------------------------------------------------------------