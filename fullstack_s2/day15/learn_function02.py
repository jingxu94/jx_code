#__author:  "Jing Xu"
#date:  2018/1/17
#
# def f(n):
# 	return n*n
#
# def foo(a,b,f):
# 	return f(a)+f(b)
#
# def g(n):
# 	return n*n*n
#
# print( foo(1,2,f) )
# print( foo(1,2,g) )
#
# ----------------------------------------------------------------
# def foo():
#
# 	def inner():
# 		return 8
#
# 	return inner()
#
# print( foo() )
# ----------------------------------------------------------------
def f(n):
	flag = 1
	for i in range(n):
		flag *= (i+1)
	return flag

print(f(5))
print(f(7))

def g(n):
	if n==1:
		return 1
	return  n*g(n-1)

print(g(5))
print(g(7))




