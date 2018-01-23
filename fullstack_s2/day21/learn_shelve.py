#__author:  "Jing Xu"
#date:  2018/1/23

import shelve

f = shelve.open("SHELVE_text")
# f["info"]={"name":"alex","age":"18"}
# f.close()
print( f.get("info") )