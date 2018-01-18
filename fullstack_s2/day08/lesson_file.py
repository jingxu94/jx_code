#__author:  "Jing Xu"
#date:  2018/1/13

# -------------------------------------------------------------------------
# f = open("小重山",'r',encoding='utf8')
# data = f.read(5)
# print( data )
# f.close()
# -------------------------------------------------------------------------
# f = open("helloworld",'w',encoding='utf8')
# f.write('Hello world!\n')
# f.write('Jing Xu')
# f.close()
# -------------------------------------------------------------------------
# f = open("小重山",'a',encoding='utf8')
# f.write("\nhello world")
# f.close()
# -------------------------------------------------------------------------
# f = open( "小重山","r",encoding="utf8" )
# data = f.readlines()
# f.close()
# for i in data:
# 	if i.startswith("欲将"):
# 		i="".join( [ i.strip(),"I like it." ] )
# 	print( i.strip() )
# -------------------------------------------------------------------------
# f = open( "小重山","r",encoding="utf8" )
# for i in f:
# 	print( i.strip() )
# -------------------------------------------------------------------------
# f = open( "小重山","r",encoding="utf8" )
# for i,v in enumerate( f.readlines(),1 ):
# 	print( i,v.strip() )
# 	print( f.tell() )
# f.close()
# -------------------------------------------------------------------------
# import sys,time
# for i in range(30):
# 	sys.stdout.write( "*" )
# 	sys.stdout.flush()
# 	time.sleep( 0.1 )
# -------------------------------------------------------------------------
# import sys,time
# for i in range(30):
# 	print( "*",end="",flush=True )
# 	time.sleep( 0.1 )
# -------------------------------------------------------------------------
# f = open( "小重山","r+",encoding="utf8" )
# print( f.readline() )
# f.write( "岳飞" )
# print( f.tell() )
# print( f.readline() )
# f.seek(0)
# print( f.readline() )
# f.close()
# -------------------------------------------------------------------------
# f_old = open( "小重山","r+",encoding="utf8" )
# f_new = open( "小重山副本","w",encoding="utf8" )
# with open( "小重山","r+",encoding="utf8" ) as f_old , open( "小重山副本","w",encoding="utf8" ) as f_new:
# number = 0
# for line in f_old:
# 	number += 1
# 	if number == 5:
# 		f_new.write( "I like it!\n" )
# 	else:
# 		f_new.write( line )
# f_new.close()
# f_old.close()
# -------------------------------------------------------------------------
# a = str( {"Beijing":{"1":111}} )
# print( type(a) )
# print(a)
# a = eval(a)
# print( type(a) )
# print( a["Beijing"] )
# -------------------------------------------------------------------------
# with open("helloworld","r") as f:
# 	print( f.readline() )
# print("hello")
# -------------------------------------------------------------------------