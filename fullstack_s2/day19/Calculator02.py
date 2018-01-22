#__author:  "Jing Xu"
#date:  2018/1/22

# !/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import re


def welcome_func():
	"""
	输入判断
	:param expression: 表达式
	:return: 返回有效表达式
	"""
	welcome_str = "超级计算器"
	print(welcome_str.center(50, '*'), '\n')  # 输出欢迎界面
	while True:
		iput = input("请输入你要计算的表达式[q:退出]：").strip()
		if iput == 'q':  # 退出计算
			sys.exit("bye-bye")
		elif len(iput) == 0:
			continue
		else:
			iput = re.sub('\s*', '', iput)  # 去除空格
			return iput


def chengchu(expression):
	"""
	乘除运算
	:param expression: 表达式
	:return: 返回没有乘除的表达式/最终计算结果
	"""
	val = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', expression)  # 匹配乘除号
	if not val:  # 乘除号不存在，返回输入的表达式
		return expression
	data = re.search('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', expression).group()  # 匹配乘除号
	if len(data.split('*')) > 1:  # 当可以用乘号分割，证明有乘法运算
		part1, part2 = data.split('*')  # 以乘号作为分割符
		value = float(part1) * float(part2)  # 计算乘法
	else:
		part1, part2 = data.split('/')  # 用除号分割
		if float(part2) == 0:  # 如果分母为0，则退出计算
			sys.exit("计算过程中有被除数为0的存在，计算表达式失败！")
		value = float(part1) / float(part2)  # 计算除法

	# print("计算:%s=%s：" % (data,value) )
	# 获取第一个匹配到的乘除计算结果value，将value放回原表达式
	s1, s2 = re.split('\d+\.*\d*[\*\/]+[\+\-]?\d+\.*\d*', expression, 1)  # 分割表达式
	# print("上一个表达式：",expression)
	next_expression = "%s%s%s" % (s1, value, s2)  # 将计算结果替换会表达式
	# print("下一个表达式%s" % next_expression)
	return chengchu(next_expression)  # 递归表达式


def jiajian(expression):
	"""
	加减运算
	:param expression: 表达式
	:return: 返回没有加减的表达式/最终计算结果
	"""
	expression = expression.replace('+-', '-')  # 替换表达式里的所有'+-'
	expression = expression.replace('--', '+')  # 替换表达式里的所有'--'
	expression = expression.replace('-+', '-')  # 替换表达式里的所有'-+'
	expression = expression.replace('++', '+')  # 替换表达式里的所有'++'
	# print("处理特殊加减后的表达式：",expression)
	data = re.search('\d+\.*\d*[\+\-]{1}\d+\.*\d*', expression)  # 匹配加减号
	if not data:  # 如果不存在加减号，则证明表达式已计算完成，返回最终结果
		return expression
	val = re.search('[\-]?\d+\.*\d*[\+\-]{1}\d+\.*\d*', expression).group()
	if len(val.split('+')) > 1:  # 以加号分割成功，有加法计算
		part1, part2 = val.split('+')
		value = float(part1) + float(part2)  # 计算加法
	elif val.startswith('-'):  # 如果是已'-'开头则需要单独计算
		part1, part2, part3 = val.split('-')
		value = -float(part2) - float(part3)  # 计算以负数开头的减法
	else:
		part1, part2 = val.split('-')
		value = float(part1) - float(part2)  # 计算减法

	s1, s2 = re.split('[\-]?\d+\.*\d*[\+\-]{1}\d+\.*\d*', expression, 1)  # 分割表达式
	# print("计算%s=%s" % (val,value))
	next_expression = "%s%s%s" % (s1, value, s2)  # 将计算后的结果替换回表达式，生成下一个表达式
	# print("下一个表达式: ",next_expression)
	return jiajian(next_expression)  # 递归运算表达式


def del_bracket(expression):
	"""
	小括号去除运算
	:param expression: 表达式
	:return:
	"""
	if not re.search(r'\(([^()]+)\)', expression):  # 判断小括号，如果不存在小括号，直接调用乘除，加减计算
		ret1 = chengchu(expression)
		ret2 = jiajian(ret1)
		return ret2  # 返回最终计算结果
	data = re.search(r'\(([^()]+)\)', expression).group()  # 如果有小括号，匹配出优先级最高的小括号
	# print("获取表达式",data)
	data = data.strip('[\(\)]')  # 剔除小括号
	ret1 = chengchu(data)  # 计算乘除
	# print("全部乘除计算完后的表达式：",ret1)
	ret2 = jiajian(ret1)  # 计算加减
	# print("全部加减计算结果：",ret2)
	part1, replace_str, part2 = re.split(r'\(([^()]+)\)', expression, 1)  # 将小括号计算结果替换回表达式
	expression = '%s%s%s' % (part1, ret2, part2)  # 生成新的表达式
	return del_bracket(expression)  # 递归去小括号


if __name__ == "__main__":
	try:
		expression = welcome_func()  # 获取到的表达式
		# expression = "-1+ 3 *(-3*2-2/-2+1)/2"
		# expression = '1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
		reslut = eval(expression)  # 用eval计算验证
		ret = del_bracket(expression)  # 用函数计算后得出的结果
		reslut = float(reslut)
		ret = float(ret)
		if reslut == ret:  # 将两种方式计算的结果进行比较，如果相等，则计算正确，输出结果
			print("eval计算结果：%s" % reslut)
			print("表达式计算结果：%s" % ret)
		else:  # 两种计算方式的结果不正确，提示异常，并返回两种方式的计算结果
			print("计算结果异常，请重新检查！")
			print("eval计算结果：%s" % reslut)
			print("表达式计算结果：%s" % ret)
	except(SyntaxError, ValueError, TypeError):  # 如果有不合法输出，则抛出错误
		print("输入表达式不合法，请重新检查！")