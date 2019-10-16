#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
@Author: by LBK
@Date:  2019/8/21
@Function: 定时获取每日dove 客户端 for windows
"""

import datetime
import socket
import os

# path = 'C:\code\src\CVBU\data\temp'
Today = datetime.datetime.now()
Yesterday = Today + datetime.timedelta(days=-1)
FromThatDay = Yesterday.date()


def run_server():
    # 在这里我将os.path的默认路径进行了更改，改到了桌面
    os.chdir(r'C:\code\src\CVBU\data\temp')

    host = '10.211.55.3'
    port = 9092
    # path = r'C:\code\src\CVBU\data\temp'
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定端口号,ip地址不绑定
    tcp_server_socket.bind((host, port))

    # 程序结束，释放端口号，端口号复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 设置监听，把主动套接字变成被动套接字，服务端套接字只负责接收客户端的连接请求
    tcp_server_socket.listen(128)

    print('等待连接中...')

    while True:
        # 创建信的套接字，等待接收客户端的连接请求
        service_client_socket, ip_port = tcp_server_socket.accept()
        print("客户端连接成功了:", ip_port)
        welcome_msg = '已成功连接至服务器，请输入秘钥指令：'
        service_client_socket.sendall(bytes(welcome_msg, encoding="utf-8"))

        # 接收客户端的请求信息
        received_approve_data = service_client_socket.recv(1024)

        # 对二进制数据进行解码
        secret_key = received_approve_data.decode("utf-8")
        # file_name = file_name_data.decode("utf-8")

        # 判断文件是否存在
        if secret_key == 'get dove':

            file_list = os.listdir()
            if len(file_list) > 0:

                for file_name in file_list:
                    # if os.path.exists(file_name):
                    # 文件存在
                    with open(file_name, "rb") as file:
                        # 读取文件数据
                        # 当文件不报错
                        while True:
                            # 循环读取文件数据
                            file_data = file.read(1024)
                            # 表示读到数据
                            if file_data:
                                # 然后把数据发送给客户端
                                service_client_socket.send(file_data)
                            else:
                                print("请求的文件数据发送完成")
                                break
                    file.close()

        else:
            print("密钥错误")
        # 终止和这个客户端服务
        service_client_socket.close()
    # 终止客户端连接请求服务, 服务端的套接字可以不用关闭
    tcp_server_socket.close()


if __name__ == '__main__':
    run_server()


