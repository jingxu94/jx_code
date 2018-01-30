#__author:  "Jing Xu"
#date:  2018/1/30

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RedirectHandler):
	def get(self):
		self.write("Hello, world")

application = tornado.web.Application([
	(r"/index", MainHandler),
])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()