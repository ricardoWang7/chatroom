from socket import *

class Dictway(object):
    '客户端功能方法'

    def __init__(self):
        self.addr = '127.0.0.1'
        self.port = 8888
        self.connect()

    def connect(self):
        '连接服务端'
        self.s = socket()
        self.s.connect((self.addr,self.port))
        

    def one_face(self):
        '界面一'
        print('1 =======注册========')
        print('2 =======登录========')
        print('3 =======退出========')

    def zhuce(self):
        '注册新用户'
        while True:
            while True:
                username = input('请输入用户名6-15位：')
                if  len(username) > 15 and len(username) < 6:
                    print('请重新输入')
                    continue
                else:
                    break
            while True:
                password = input('请输入密码6-15位：')
                if  len(password) > 15 and len(password) < 6:
                    print('请重新输入')
                    continue
                else:
                    break                
        #向服务端发送注册信息
            msg = '1 '+ username + ' ' + password
            self.s.send(msg.encode())
            data = self.s.recv(1024).decode()
            print(data)











def main():
    a = Dictway()
    while True:
        a.one_face()
        data = int(input('请输入操作编号：'))
        if data not in(1,2,3):
            print('请输入正确编号')
            continue
        if data == 1:  #注册
            a.zhuce()






#测试
if __name__ == '__main__':
    main()
