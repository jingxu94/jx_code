#__author:  "Jing Xu"
#date:  2018/1/26
# -----------------------------------------------------------
# class Bar:
#     '''构造方法'''
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def foo(self,arg):
#         print(self.name, self.age, self.sex, arg)
#
# z = Bar("alex", 18, "male")
# z.foo("oldboy")
# -----------------------------------------------------------
# class database_helper:
#
#     def __init__(self, ip, port, username, pwd):
#         self.ip = ip
#         self.port = port
#         self.username = username
#         self.pwd = pwd
#
#     def add(self,content):
#         '''利用self封装的用户名、密码、IP、端口等信息'''
#         print(content)
#
#     def delete(self,content):
#         pass
#
#     def update(self,content):
#         pass
#
#     def get(self,content):
#         pass
#
# s1 = database_helper("1.1.1.1", 3306, "alex", "abc")
# s1.add("ok")
# -----------------------------------------------------------
# class F:
#
#     def f1(self):
#         print("F.f1")
#
#     def f2(self):
#         print("F.f2")
#
# class S(F):
#
#     def s1(self):
#         print("S.s1")
#
#     def f2(self):
#         super(S,self).f2()
#         F.f2(self)
#         print("S.f2")
#
# s1 = S()
# s1.f1()
# s1.f2()
# -----------------------------------------------------------
class BaseReuqest:

    def __init__(self):
        print('BaseReuqest.init')


class RequestHandler(BaseReuqest):
    def __init__(self):
        print('RequestHandler.init')
        BaseReuqest.__init__(self)

    def serve_forever(self):
        # self,是obj
        print('RequestHandler.serve_forever')
        self.process_request()

    def process_request(self):
        print('RequestHandler.process_request')

class Minx:

    def process_request(self):
        print('minx.process_request')


class Son(Minx, RequestHandler):
    pass


obj = Son() # init
obj.serve_forever()
