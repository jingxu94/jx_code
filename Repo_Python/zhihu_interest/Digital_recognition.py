# @Time : 2018/4/3 9:57 
# @Author : Jing Xu

import sys,re,types


class NotIntegerError(Exception):
	pass


class OutOfRangeError(Exception):
	pass


_MAPPING = (u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九',)
_P0 = (u'', u'十', u'百', u'千',)
_S4, _S8, _S16 = 10 ** 4, 10 ** 8, 10 ** 16
_MIN, _MAX = 0, 9999999999999999


def _to_chinese4(num):
	'''转换[0, 10000)之间的阿拉伯数字
	'''
	assert (0 <= num and num < _S4)
	if num < 10:
		return _MAPPING[num]
	else:
		lst = []
		while num >= 10:
			lst.append(num % 10)
			num = num / 10
		lst.append(num)
		c = len(lst)  # 位数
		result = u''

		for idx, val in enumerate(lst):
			if val != 0:
				result += _P0[idx] + _MAPPING[val]
				if idx < c - 1 and lst[idx + 1] == 0:
					result += u'零'

		return result[::-1].replace(u'一十', u'十')


def _to_chinese8(num):
	assert (num < _S8)
	to4 = _to_chinese4
	if num < _S4:
		return to4(num)
	else:
		mod = _S4
		high, low = num / mod, num % mod
		if low == 0:
			return to4(high) + u'万'
		else:
			if low < _S4 / 10:
				return to4(high) + u'万零' + to4(low)
			else:
				return to4(high) + u'万' + to4(low)


def _to_chinese16(num):
	assert (num < _S16)
	to8 = _to_chinese8
	mod = _S8
	high, low = num / mod, num % mod
	if low == 0:
		return to8(high) + u'亿'
	else:
		if low < _S8 / 10:
			return to8(high) + u'亿零' + to8(low)
		else:
			return to8(high) + u'亿' + to8(low)


def to_chinese(num):
	if type(num) != int:
		raise NotIntegerError(u'%s is not a integer.' % num)
	if num < _MIN or num > _MAX:
		raise OutOfRangeError(u'%d out of range[%d, %d)' % (num, _MIN, _MAX))

	if num < _S4:
		return _to_chinese4(num)
	elif num < _S8:
		return _to_chinese8(num)
	else:
		return _to_chinese16(num)

def start_window():
	'''
	起始界面
	:param:	number:待计算表达式
	:return: 返回有内容的输入
	'''
	start_info = "数字转换"
	print( start_info.center( 50, "*" ), "\n" )
	while True:
		# number = input(  "请输入你要转换的数字[q:退出]：\n" ).strip()
		number = "123456.78"
		if number == "q" or number == "Q":
			sys.exit("关闭程序")
		elif len(number) == 0:
			continue
		else:
			return number


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
	string = string.replace(' ', '')
	return string


def trans(number):
	point = "."
	num = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
	trans_decimal = ""
	if re.findall( point, number ):
		number, decimal = number.split( point )
		decimal_list = []
		for index in decimal:
			decimal_list.append(num[int(index)])
		trans_decimal = "".join(decimal_list)
	return number, trans_decimal


if __name__ == "__main__":
	number = start_window()
	number = format_string(number)
	number, trans_decimal = trans(number)
	number = to_chinese(int(number))
	if trans_decimal:
		number = "".join([number, "点", trans_decimal])
	print(number)
