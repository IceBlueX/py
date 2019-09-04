# -*- coding:utf-8 -*-
__author__ = "LBK"

import paramiko

host = "10.211.55.3"
port = 1728

transport = paramiko.Transport((host, port))
print(1)
transport.connect(username='root', password='hhh')
print(2)
sftp = paramiko.SFTPClient.from_transport(transport)  # 如果连接需要密钥，则要加上一个参数，hostkey="密钥"
print(3)
sftp.put('Windows.txt', '/root/Windows.txt')  # 将本地的Windows.txt文件上传至服务器/root/Windows.txt

transport.close()  # 关闭连接
