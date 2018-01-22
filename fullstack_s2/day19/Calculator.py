#__author:  "Jing Xu"
#date:  2018/1/22

import re

source = " 1- 2 *(( 60-30+(-40/5)* ( 9-2*5/3+7/3*99/4*2998 + 10*568 /14))-( -4*3) / ( 16-3*2)) "

def check(string):
	flag = True
	if re.findall('[a-zA-Z]',string):
		print('Invalid')
		flag = False
	return flag

def format_string(string):
	string = string.replace('--', '+')
	string = string.replace('-+', '-')
	string = string.replace('+-', '-')
	string = string.replace('++', '+')
	string = string.replace('*+', '*')
	string = string.replace('/+', '/')
	string = string.replace(' ', '')
	return string

def cal_mul_div(string):
	regular = '[\-]\d+\.?\d*[*/][\-]\d+\.?\d*'

	while re.findall( regular, string ):
		expression = re.search( regular, string ).group()

		if expression.count("*") == 1:
			x, y = expression.split("*")
			mul_result = str( float(x) * float(y) )
			string = string.replace( expression, mul_result )
			string = format_string(string)

		if expression.count("/"):
			x, y = expression.split("/")
			div_result = str( float(x) / float(y) )
			string = string.replace( expression, div_result )
			string = format_string(string)

		if expression.count("**") == 2:
			x, y = expression.split("**")
			pow_result = 1
			for i in range(int(y)):
				pow_result *= int(x)
			string = string.replace( expression, str(pow_result) )
			string = format_string(string)
	return string



def cal_add_sub(string):
	add_regular = "[\-]?\d+\.?\d*\+[\-]?\d+\.?\d*"
	sub_regular = "[\-]?\d+\.?\d*\-[\-]?\d+\.?\d*"

	while re.findall( add_regular, string ):
		add_list = re.findall( add_regular, string )
		for add_str in add_list:
			x, y = add_str.split("+")
			add_result = "+" + str( float(x) + float(y) )
			string = string.replace( add_str, add_result)
		string = format_string(string)

	while re.findall( sub_regular, string ):
		sub_list = re.findall( sub_regular, string )

		for sub_str in sub_list:
			numbers = sub_str.split("-")
			if len(numbers) == 3:
				sub_result = 0
				for v in numbers:
					if v:
						sub_result -= float(v)
			else:
				x, y = numbers
				sub_result =  float(x) - float(y)
			string = string.replace( sub_str, str(sub_result) )
		string = format_string(string)
	return string



if check(source):
	source = format_string(source)
	while source.count('(') > 0:
		strs = re.search( '\([^()]+\)', source ).group()
		replace_str = cal_mul_div(strs)
		replace_str = cal_add_sub(replace_str)
		source = format_string( source.replace( strs, replace_str[1:-1] ) )
	else:
		replace_str = cal_mul_div(source)
		replace_str = cal_add_sub(replace_str)
		source = source.replace( source, replace_str )
	print( "my result:", source.replace( "+", "" ) )
