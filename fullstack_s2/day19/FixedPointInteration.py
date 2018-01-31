#__author:  "Jing Xu"
#date:  2018/1/31

from sympy import diff,symbols
import re


def format_string(expression):
	'''
	格式整理，包括正负关系判断和去除空格
	:param expression: 待整理格式的表达式
	:return: 返回去除多余正负号和空格的表达式
	'''
	expression = expression.replace("--", "+")
	expression = expression.replace("-+", "-")
	expression = expression.replace("+-", "-")
	expression = expression.replace("++", "+")
	expression = expression.replace("*+", "*")
	expression = expression.replace("/+", "/")
	expression = expression.replace(" ", "")
	return expression


def cal_pow(string):
	'''
	乘方运算
	:param string: 待计算表达式，不包含括号
	:return: 返回计算完乘方运算的表达式
	'''
	regular = '\d+\.*\d*[*][*]+[\+\-]?\d+\.*\d*'

	while re.findall( regular, string ):
		expression = re.search( regular, string ).group()


		if expression.count("**"):
			x, y = expression.split("**")
			pow_result = 1
			for i in range(int(y)):
				pow_result *= float(x)
			string = string.replace( expression, str(pow_result) )
			string = format_string(string)
	return string


def cal_mul_div(string):
	'''
	乘除运算
	:param string: 待计算表达式，不包含括号
	:return: 返回计算完全部乘除运算的表达式
	'''
	regular = '\d+\.*\d*[*/**]+[\+\-]?\d+\.*\d*'

	while re.findall( regular, string ):
		expression = re.search( regular, string ).group()

		if expression.count("*"):
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


def recalculate( source, x_value ):
	'''
	正则计算器
	:param source:待计算表达式
	:return: 返回正则计算器计算结果，输出为字符型
	'''
	x_value_str = str(x_value)
	source = source.replace("x", x_value_str)
	source = format_string(source)
	# print(source)
	# return eval(source)
	while source.count('(') > 0:
		strs = re.search( '\([^()]+\)', source ).group()
		replace_str = cal_pow(strs)
		replace_str = cal_mul_div(replace_str)
		replace_str = cal_add_sub(replace_str)
		source = format_string( source.replace( strs, replace_str[1:-1] ) )
	else:
		replace_str = cal_pow(source)
		replace_str = cal_mul_div(replace_str)
		replace_str = cal_add_sub(replace_str)
		source = source.replace( source, replace_str )
	return source.replace( "+", "" )


def func( x_value, expression ):
	cal_expression = expression
	# print(cal_string)
	value = float('%.4f' %float(recalculate(cal_expression, x_value)))
	# print("value:",value)
	return value

expression = input("请输入方程左端项：").strip()
x_value = float( input("请输入初始迭代值：").strip() )
eps = 1e-2
x = symbols("x")
diff_expression = str(diff( expression, x ))
expression = "(" + diff_expression + ")" + "*" + "x" + "-" + "(" + expression + ")"
cal_string = "(" + expression + ")" + "/" + "(" + diff_expression + ")"

while True:
	xtemp = func( x_value, cal_string )
	if ( abs( xtemp - x_value ) < eps ):
		break
	x_value = xtemp
print( "The solution is:", xtemp )
