from socket import *
from threading import Thread
import pymysql,sys

class Dict(object):
    '电子词典服务端方法分装类'

    def __init__(self):
        self.addr = '0.0.0.0'
        self.port = 8888
        self.s = self.create_socket()
        self.cur = self.create_cursor()

    def create_socket(self):
        '创建套接字'
        s = socket()
        s.bind((self.addr,self.port))
        s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        return s 

    def create_cursor(self):
        '连接数据库并创建游标'
        db = pymysql.connect(host = 'localhost',
            user = 'root',passwd = '123456'
            ,charset = 'utf8')
        #创建游标对象
        cur = db.cursor()
        cur.execute('use dianzi_dict')
        return cur

    def handle(self,c):
        '具体处理请求总列表'
        print('连接到',c.getpeername())
        data = c.recv(1024).decode().split(' ')
        print(data)
        if int(data[0]) == 1:
            #注册用户
            self.zhuce(c,data[1:])

    def zhuce(self,c,m):
        '1代表收到注册请求'
        




def main():
    a = Dict()   #创建类对象
    a.s.listen(5)
    print('正在监听8888')
    while True:
        try:
            c,addr = a.s.accept()
        except KeyboardInterrupt:
            a.s.close()
            sys.exit('服务器退出')
        except Exception:
            continue
        #创建新的线程处理请求
        dict_client = Thread(target = a.handle,args =(c,))
        dict_client.daemon = True
        dict_client.start()





#测试
if __name__ == '__main__':
    main()
