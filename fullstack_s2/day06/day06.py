#__author:  "Jing Xu"
#date:  2018/1/13
# ---------------------------------------------------------------------------------------------------
# dic1={'age':23,'sex':'male'}
# dic2=dict((('name','jingxu'),))
# print(dic1)
# print(dic2)
# ret = dic1.setdefault('age',34)
# print(ret)
# dic1['hobby']='coding'
# print(dic1)
# print(list(dic1.keys()))
# print(type(dic1.keys()))
# print(list(dic1.values()))
# print(list(dic1.items()))
# dic1.update(dic2)
# print(dic1)
# print(dic2)
# # del dic1['name']
# # dic1.clear()
# print(dic1.pop('age'))
# print(dic1)
# dic3=dict.fromkeys(['host1','host2','host3'],['test1','test2','test3'])
# dic3['host2'][1]='test3'
# print(dic3)
# for i in dic1:
# 	print(i,dic1[i])
# ---------------------------------------------------------------------------------------------------
# a = '123'
# b = 'abc'
# c = a + b
# print(c)
# d = '***'.join([a,b])
# print(d)
# ---------------------------------------------------------------------------------------------------
st='hello world {name} is {age}'
print(st.count('l'))
print(st.capitalize())
print(st.center(50,'-'))
print(st.endswith('d'))
print(st.startswith('h'))
print(st.expandtabs(tabsize=10))
print(st.find('l'))
print(st.format(name='jingxu',age=23))
print(st.format_map({'name':'jingxu','age':23}))
print(st.index('e'))
print('abc456'.isalnum())
print('3434f'.isdecimal())
print('3424'.isdigit())
print('13.34'.isnumeric())
print('f43f'.isidentifier())
print('sCdfd'.islower())
print('FDTD'.isupper())
print('  '.isspace())
print('My Name Is Kyrie'.istitle())
print('MFDf'.lower())
print('Mydf'.upper())
print('dfjkDFD'.swapcase())
print('         My title'.strip())
print('My title title title'.replace('title','lesson',2))
print('My title title'.rfind('t'))
print('My title title'.split('t',1))
print('My title title'.rsplit('t',1))
# ---------------------------------------------------------------------------------------------------