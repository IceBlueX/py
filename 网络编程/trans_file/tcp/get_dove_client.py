#!/usr/bin/python
# -*- coding=utf-8 -*-
"""
@Author: by LBK
@Date:  2019/8/21
@Function: 定时获取每日dove 客户端 for iMac
"""
import datetime
from hashlib import md5
import socket
import sys
import os


def reprint(*args):
    """
    实时刷新输出
    :return:
    """
    sys.stdout.write("\r" + str(args))
    sys.stdout.flush()


# "\\Mac\Home\Desktop\start_server.bat"
def get_filesize(filepath):
    """
    获取对应路径的文件大小 单位为MB 保留两位小数
    :param filepath:
    :return:
    """
    filepath = filepath.encode("utf-8")
    fsize = os.path.getsize(filepath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)


def file_approve():
    # os.chdir(r'/Users/libaokun/Desktop/')

    # 创建套接字,AF_INET:ipv4，SOCK_STREAM：TCP协议
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置服务端的ip地址 端口
    host = '10.211.55.3'
    port = 1909
    # 和服务端连接
    tcp_client_socket.connect((host, port))
    msg = tcp_client_socket.recv(1024)
    receive = msg.decode("utf-8")
    # print(receive)

    # 输入密钥
    secret_key = input(receive)
    # while True:

    # 个人在服务端和客户端都采用utf-8编码
    secret_key_data = secret_key.encode("utf-8")

    # 发送请求密钥数据
    tcp_client_socket.send(secret_key_data)

    # 接收文件列表
    file_list_str = tcp_client_socket.recv(1024)
    file_list = file_list_str.decode("utf-8").split('\n')
    print(file_list)

    # 输入确认下载
    secret_key = input('文件列表如上，请确认下载：')
    # while True:
    # 个人在服务端和客户端都采用utf-8编码
    secret_key_data = secret_key.encode("utf-8")
    # 发送请求密钥数据
    tcp_client_socket.send(secret_key_data)

    for files in file_list:
        # 把数据写入到文件里
        file_name = files.split(' ++ ')[0]
        file_size = float(files.split(' ++ ')[1])
        path = "/Users/libaokun/Desktop/" + file_name
        with open(path, "wb") as file:
            i = 0
            while True:
                # 循环接收文件数据
                i += 1
                file_data = tcp_client_socket.recv(1024*1024)
                # 只要接收到数据，就写入
                if file_data:
                    print_str = ''
                    file.write(file_data)
                    downloaded_size = get_filesize(path)
                    downloaded_percent = downloaded_size/file_size
                    size_str = str(downloaded_size) + '/' + str(file_size)
                    # print(size_str)
                    percent_str = format(downloaded_percent, '.1%')
                    print_str = '正在下载：' + percent_str + ' ' + size_str
                    reprint("{}".format(print_str))

                    # final_str = '正在下载：' + print_str
                    # print('\r' + final_str, end='', flush=True)

                    # print("数据已接收 %s M" % str(get_filesize(path)))
                if downloaded_size == file_size:
                    print("%s 接收完成" % path)
                    break
    # 关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    file_approve()


