from pymysql import connect
import re

db = connect(host = 'localhost',
            user = 'root',passwd = '123456'
            ,charset = 'utf8')

cur = db.cursor()

cur.execute('use dianzi_dict;')
try:
    f = open('dict.txt','r')
except:
    print('文件打开失败')
for line in f:
    a = re.split(r'\s+',line)
    word = a[0]
    miaoshu = ' '.join(a[1:-1])
    cur.execute('insert into dict values(%s,%s)',[word,miaoshu])
    db.commit()
cur.close()
db.close()
    
    
        
