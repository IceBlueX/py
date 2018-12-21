import socket
import os
#通信阶段
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.pc6.com',80))

s.send(b'GET / HTTP/1.1\r\nHost: www.pc6.com\r\nConnection: close\r\n\r\n')

buffer =[]

while True:
    #每次最多接收1024字节
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)

s.close()
#数据处理
header, html = data.split(b'\r\n\r\n',1)    #头和网页分离
print(header.decode('utf-8'))   #头转换为utf-8格式输出

with open('sina.html','wb') as f:
    f.write(html)

os.system("open sina.html")

