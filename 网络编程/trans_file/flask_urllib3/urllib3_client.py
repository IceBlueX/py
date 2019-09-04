import urllib3
import os


url = 'https://short-deer-46.localtunnel.me'

# 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()
# # 通过request()方法创建一个请求：
# r = http.request('GET', 'http://cuiqingcai.com/')
# print(r.status)  # 200
# # 获得html源码,utf-8解码
# print(r.data.decode())


def upload():
    os.chdir(r'C:\code\src\CVBU\data\temp')
    file_list = os.listdir()

    print('指定文件夹中文件有 %s 个' % len(file_list))
    print('对应的文件名为：', file_list)
    for file_name in file_list:
        print(' %s 正在传输。。。' % file_name)
        # if os.path.exists(file_name):
        # 文件存在
        with open(file_name, "rb", encoding='UTF-8') as file:
            file_read = file.read()
            # 读取文件数据
            # 当文件不报错
            r = http.request('POST',
                             '%s/upload' % url,
                             fields={'filefield': (file_name, file_read, 'text/plain')
                                     })
            print(r.data.decode('unicode_escape'))

        file.close()
        print(' %s 传输完成！' % file_name)


if __name__ == '__main__':
    upload()


