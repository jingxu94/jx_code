#__author:  "Jing Xu"
#date:  2018/2/28

try:
	f = open("hp","r")
except IOError:
	print("could not open file")

def safe_float(obj):
	try:
		retval = float(obj)
	except ValueError:
		retval = "could not convert non-number to float"
	except TypeError:
		retval = "object type can not be converted to float"
	return retval

print(safe_float("hp"))
print(safe_float({"hp":"pavilion"}))
print(safe_float("200"))
print(safe_float(200))

def safe_float2(obj):
	try:
		retval = float(obj)
	except (ValueError, TypeError):
		retval = "argument must be a numberic string"
	return retval

print(safe_float2({}))
print(safe_float2("123"))