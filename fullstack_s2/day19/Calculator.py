#__author:  "Jing Xu"
#date:  2018/1/22

import re
import sys


def start_window():
	'''
	起始界面
	:param:	expression:待计算表达式
	:return: 返回有内容的输入
	'''
	start_info = "正则计算器"
	print( start_info.center( 50, "*" ), "\n" )
	while True:
		expression = input(  "请输入你要计算的表达式[q:退出]：\n" ).strip()
		if expression == "q" or expression == "Q":
			sys.exit("关闭计算器")
		elif len(expression) == 0:
			continue
		else:
			return expression


def format_string(string):
	'''
	格式整理，包括正负关系判断和去除空格
	:param string: 待整理格式的表达式
	:return: 返回去除多余正负号和空格的表达式
	'''
	string = string.replace('--', '+')
	string = string.replace('-+', '-')
	string = string.replace('+-', '-')
	string = string.replace('++', '+')
	string = string.replace('*+', '*')
	string = string.replace('/+', '/')
	string = string.replace(' ', '')
	return string


def cal_mul_div(string):
	'''
	乘除乘方运算
	:param string: 待计算表达式，不包含括号
	:return: 返回计算完全部乘除和乘方运算的表达式
	'''
	regular = '\d+\.*\d*[*/]+[\+\-]?\d+\.*\d*'

	while re.findall( regular, string ):
		expression = re.search( regular, string ).group()

		if expression.count("*") == 1:
			x, y = expression.split("*")
			mul_result = str( float(x) * float(y) )
			string = string.replace( expression, mul_result )
			string = format_string(string)

		if expression.count("/"):
			x, y = expression.split("/")
			if float(y) == 0:
				print("计算部分有0作分母，请重新检查输入！")
				start_window()
			div_result = str( float(x) / float(y) )
			string = string.replace( expression, div_result )
			string = format_string(string)

		if expression.count("*") == 2:
			x, y = expression.split("**")
			pow_result = 1
			for i in range(int(y)):
				pow_result *= int(x)
			string = string.replace( expression, str(pow_result) )
			string = format_string(string)
	return string


def cal_add_sub(string):
	'''
	加减运算
	:param string:待计算表达式，不包含括号和乘除运算
	:return: 返回计算完全部加减运算的表达式
	'''
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


def recalculate(source):
	'''
	正则计算器
	:param source:待计算表达式
	:return: 返回正则计算器计算结果，输出为字符型
	'''
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
	return source.replace( "+", "" )


if __name__ == "__main__":
	try:
		expression = start_window()
		reresult = recalculate( expression )
		result = eval( expression )
		reresult = float( reresult )
		result = float( result )
		if result == reresult:
			print( "eval计算结果：%s" % result )
			print( "正则计算器计算结果：%s" % reresult )
		else:  # 两种计算方式的结果不正确，提示异常，并返回两种方式的计算结果
			print( "计算结果异常，请重新检查输入！")
			print( "eval计算结果：%s" % result )
			print( "正则计算器计算结果：%s" % reresult )
	except(SyntaxError, ValueError, TypeError):  # 如果有不合法输出，则抛出错误
		print("输入表达式不合法，请重新检查输入！")
		start_window()