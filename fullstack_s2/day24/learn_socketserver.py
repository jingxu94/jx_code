#__author:  "Jing Xu"
#date:  2018/1/26

import socketserver

obj = socketserver.ThreadingTCPServer(1,2)
obj.serve_forever()