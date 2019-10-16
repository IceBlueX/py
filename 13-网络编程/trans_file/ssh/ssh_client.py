

# -*- coding:utf-8 -*-
__author__ = "MuT6 Sch01aR"

import paramiko

host = "10.211.55.3"
port = 1728

transport = paramiko.Transport((host, port))
print(1)
transport.connect(username='root', password='hhh')
print(2)
sftp = paramiko.SFTPClient.from_transport(transport)
print(3)
sftp.get(
    r'C:\code\src\CVBU\data\temp\SGChina_DOVE_Plus31_20190821.txt',
    'SGChina_DOVE_Plus31_20190821.txt'
)  # 将Linux上的/root/Linux.txt下载到本地

transport.close()
