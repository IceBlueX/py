import psycopg2 #导入psycopg2包
import socket
import threading
import os
import time 


# 连接到给定的数据库
conn = psycopg2.connect(database="magicbox", user="libaokun",password="magicbox",
                        host="127.0.0.1",port="5432")
# 建立游标，用来执行数据库操作
cursor = conn.cursor()

#创建socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定监听端口
s.bind(('127.0.0.1',9999))
#监听端口
s.listen(5)
print('waiting for connection...')


"""
#执行SQL命令
cursor.execute("DROP TABLE test_conn")
cursor.execute("CREATE TABLE test_conn(id int, name text)")
cursor.execute("INSERT INTO test_conn values(1,'haha')")

#提交SQL命令
conn.commit()
"""

#执行sql select命令
cursor.execute("select * from magicbox")

#获取SELECT返回的元组
rows = cursor.fetchall()
#for row in rows:
 #   for item in row:
#        print(item)
 #   print('\n')



def tcplink(sock,addr):
    print('Accept new connection from %s:%s...'% addr)

    for row in rows:
        for item in row:
            print(str.encode(item))
            sock.send(str.encode(item))
        print('\n')
    #sock.send(b'Welcome!')

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s'% data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
    
while True:
    #接受一个新链接
    sock,addr = s.accept()
    #创建新线程来处理TCP连接
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

#关闭游标
cursor.close()

#关闭数据库
conn.close()