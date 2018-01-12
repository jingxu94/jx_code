# -*- coding:utf-8 -*-
#------------------------------------------------------------
# print('hello world')
# print('The quick brown fox','jumps over','the lazy dog')
# print('I\'m \"ok\"')
# print('I\'m learning\nPython.')
# print(r'\\\t\\')
#------------------------------------------------------------
# print absolute value of an integer 
# a=100 
# if a>=0:
#     print(a)
# else:
#     print(-a)
#------------------------------------------------------------
# s='Python-中文'
# print(s)
# b=s.encode('utf-8')
# print(b)
# print(b.decode('utf-8'))
#------------------------------------------------------------
# age = 3
# if age >= 18:
#     print('Your age is', age)
#     print('adult')
# else:
#     print('Your age is', age)
#     print('teenager')
#------------------------------------------------------------
# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)
#------------------------------------------------------------
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n 
#     n = n - 2
# print(sum)
#------------------------------------------------------------
import math
def quadratic(a, b, c):
    delta = math.sqrt( b*b - 4*a*c )
    x1=( -b + delta )/( 2*a )
    x2=( -b - delta )/( 2*a )
    return x1,x2

r=quadratic(2,3,1)
print(r) 







































































































































































