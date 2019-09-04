# coding=utf-8
import os
import sys
import socket
import time
import hashlib
import base64
import struct
from multiprocessing import Process

# 无秘信息头
HTTP_RESPONSE = "HTTP/1.1 {code} {msg}\r\n" \
                "Server:LyricTool\r\n" \
                "Date:{date}\r\n" \
                "Content-Length:{length}\r\n" \
                "\r\n" \
                "{content}\r\n"
STATUS_CODE = {200: 'OK', 501: 'Not Implemented'}

# 有密信息头
UPGRADE_WS = "HTTP/1.1 101 Switching Protocols\r\n" \
             "Connection: Upgrade\r\n" \
             "Upgrade: websocket\r\n" \
             "Sec-WebSocket-Accept: {}\r\n" \
             "WebSocket-Protocol: chat\r\n\r\n"


def sec_key_gen(msg):
    key = msg + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    ser_key = hashlib.sha1(key.encode('utf-8')).digest()
    return base64.b64encode(ser_key).decode()


class WebsocketServer(object):

    def __init__(self, conn):
        # 接受一个socket对象
        # 初始化连接
        self.conn = conn
        # 初始化连接状态为0 即READY
        self.state = 0

    def open(self):

        # 握手建立连接
        self._hand_shake()

        # 若是连接状态未更新，则报错 握手失败
        if self.state == 1:
            return self
        else:
            raise Exception('Hand shake failed.')

    # todo 这是啥？
    def __enter__(self):
        return self.open()

    def getstate(self):
        # 获取连接状态 连接状态对应关系
        state_map = {0: 'READY', 1: 'CONNECTION ESTABLISHED', 2: 'HANDSHAKED', 3: 'FAILED', -1: 'CLOSED'}
        return self.state, state_map[self.state]

    def _hand_shake(self):
        """
        握手建立连接过程
        :return:
        """

        # 原生数据初始化
        raw_data = b''

        # 循环接收客户端的请求
        while True:

            # fragment 破碎，片段
            # 每次接收1k的片段 500汉字左右
            fragment = self.conn.recv(1024)

            # 整合到该次请求总数据
            raw_data += fragment

            # 如果接收的的数据不足1k,则认为数据已经接收完
            # 接收完退出接收循环
            if len(fragment) < 1024:
                break
        # utf-8 解码 采用相同的编码方式就好
        data = raw_data.decode('utf-8')
        print('data>>>', data)
        print('<<<data over')

        # 1代表分成两部分 只分割一次
        # '\r\n\r\n'将data 分成头和内容两部分
        header, content = data.split('\r\n\r\n', 1)

        # print('header>>>', header)
        # print('<<<header over')

        print('content>>>', content)
        print('<<<content over')

        # 开始解析信息头

        # 按行拆分
        header = header.split('\r\n')
        # for value in header:
        #     print(value)

        # 将第一行之后的同行数据 按照': ' 进行拆分 同行放入一个 list 多个list存储在list中的
        # map函数的第一个参数为函数或者方法，后一个参数为可迭代对象
        # 循环迭代后一个对象 作为前面方法的输入量，并将结果存在map中
        options = map(lambda i: i.split(': '), header[1:])

        # 将map后的数据拆分为字典存储起来
        options_dict = {item[0]: item[1] for item in options}
        # print(options_dict)

        # todo 一个无聊的日期格式？
        date = time.strftime("%m,%d%Y", time.localtime())
        print(date)

        if 'Sec-WebSocket-Key' not in options_dict:

            # 无密钥传输 todo 发送信息后 关闭连接 并更新状态
            # todo ???这发送了个啥 无密钥信息头
            self.conn.send(
                bytes(HTTP_RESPONSE.format(code=501, msg=STATUS_CODE[501], date=date, length=len(date), content=date),
                      encoding='utf-8'))
            self.conn.close()

            # 更新状态为握手失败？
            self.state = 3
            return True

        else:

            # 有密钥传输 设定状态为连接已建立 准备握手
            self.state = 2

            # 通过密钥进行握手
            self._build(options_dict['Sec-WebSocket-Key'])
            return True

    def _build(self, sec_key):
        # 建立WebSocket连接
        response = UPGRADE_WS.format(sec_key_gen(sec_key))
        self.conn.send(bytes(response, encoding='utf-8'))
        self.state = 1
        return True

    def _get_data(self, info, setcode):
        payload_len = info[1] & 127
        fin = 1 if info[0] & 128 == 128 else 0
        opcode = info[0] & 15  # 提取opcode

        # 提取载荷数据
        if payload_len == 126:
            # extend_payload_len = info[2:4]
            mask = info[4:8]
            decoded = info[8:]
        elif payload_len == 127:
            # extend_payload_len = info[2:10]
            mask = info[10:14]
            decoded = info[14:]
        else:
            # extend_payload_len = None
            mask = info[2:6]
            decoded = info[6:]

        bytes_list = bytearray()
        for i in range(len(decoded)):
            chunk = decoded[i] ^ mask[i % 4]
            bytes_list.append(chunk)
        if opcode == 0x00:
            opcode = setcode
        if opcode == 0x01:  # 文本帧
            body = str(bytes_list, encoding='utf-8')
            return fin, opcode, body
        elif opcode == 0x08:
            self.close()
            raise IOError('Connection closed by Client.')
        else:  # 二进制帧或其他，原样返回
            body = decoded
            return fin, opcode, body

    def recv(self):
        msg = ''
        # 处理切片
        opcode = 0x00
        while True:
            raw_data = b''
            while True:
                section = self.conn.recv(1024)
                raw_data += section
                if len(section) < 1024:
                    break
            fin, _opcode, fragment = self._get_data(raw_data, opcode)
            opcode = _opcode if _opcode != 0x00 else opcode
            msg += fragment
            if fin == 1:  # 是否是最后一个分片
                break
        return msg

    def send(self, msg, fin=True):
        # 发送数据
        data = struct.pack('B', 129) if fin else struct.pack('B', 0)
        msg_len = len(msg)
        if msg_len <= 125:
            data += struct.pack('B', msg_len)
        elif msg_len <= (2 ** 16 - 1):
            data += struct.pack('!BH', 126, msg_len)
        elif msg_len <= (2 ** 64 - 1):
            data += struct.pack('!BQ', 127, msg_len)
        else:
            # 分片传输超大内容（应该用不到）
            while True:
                fragment = msg[:(2 ** 64 - 1)]
                msg -= fragment
                if msg > (2 ** 64 - 1):
                    self.send(fragment, False)
                else:
                    self.send(fragment)
        data += bytes(msg, encoding='utf-8')
        self.conn.send(data)

    def ping(self):
        ping_msg = 0b10001001
        data = struct.pack('B', ping_msg)
        data += struct.pack('B', 0)
        while True:
            self.conn.send(data)
            data = self.conn.recv(1024)
            pong = data[0] & 127
            if pong != 9:
                self.close()
                raise IOError('Connection closed by Client.')

    def close(self):
        self.conn.close()
        self.state = -1

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is IOError:
            print(exc_val)
        self.close()


def ws_handler(conn):
    with WebsocketServer(conn) as ws:
        while True:
            msg = ws.recv()
            if ws.state == -1:
                break
            print(msg)
            ws.send(str(msg.split(',')))


def get_ip():
    """
    根据 netifaces 中调用系统包获得当前网卡的主要信息
    主要是IPv4 下的网卡IP
    :return:
    """
    try:
        import netifaces
    except ImportError:
        try:
            command_to_execute = "pip install netifaces || easy_install netifaces"
            os.system(command_to_execute)
        except OSError:
            print("Can NOT install netifaces, Aborted!")
            sys.exit(1)
        import netifaces

    routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
    routingNicName = netifaces.gateways()['default'][netifaces.AF_INET][1]

    for interface in netifaces.interfaces():
        if interface == routingNicName:
            # print netifaces.ifaddresses(interface)
            routingNicMacAddr = netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']
            try:
                routingIPAddr = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
                # TODO(Guodong Ding) Note: On Windows, netmask maybe give a wrong result in 'netifaces' module.
                routingIPNetmask = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']
            except KeyError:
                pass

    display_format = '%-30s %-20s'
    print(display_format % ("Routing Gateway:", routingGateway))
    print(display_format % ("Routing NIC Name:", routingNicName))
    print(display_format % ("Routing NIC MAC Address:", routingNicMacAddr))
    print(display_format % ("Routing IP Address:", routingIPAddr))
    print(display_format % ("Routing IP Netmask:", routingIPNetmask))
    
    return routingIPAddr
    

def run_server():
    computer_name = socket.gethostname()
    # # 获取本机ip
    # computer_host = socket.gethostbyname(computer_name)

    print('本机计算机名：', computer_name)

    # 获得地址和端口
    host = get_ip()
    # host = '127.0.0.1'
    # 设置为0 系统自动分配可用的端口
    port = 8080

    # 创建tcp服务端套接字
    websocket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 程序结束，释放端口号，端口号复用
    websocket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定地址以及端口号
    websocket_server.bind((host, port))

    # 获得绑定的地址，以及分配的端口号
    sock_binded = websocket_server.getsockname()
    print('绑定地址：', sock_binded)

    # 等待一个连接
    websocket_server.listen(1)

    print('Server Started.')
    while True:
        con, addr = websocket_server.accept()
        print("Accepted. {0}, {1}".format(con, str(addr)))
        p = Process(target=ws_handler, args=(con,))
        p.start()


if __name__ == '__main__':
    run_server()



