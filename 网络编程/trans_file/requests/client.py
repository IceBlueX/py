import requests
import os

url = 'https://short-deer-46.localtunnel.me'


def upload_file():
    os.chdir(r'C:\code\src\CVBU\data\temp')

    file_list = os.listdir()
    print('指定文件夹中文件有 %s 个' % len(file_list))
    print('对应的文件名为：', file_list)
    for file_name in file_list:
        print(' %s 正在传输。。。' % file_name)
        # if os.path.exists(file_name):
        # 文件存在
        with open(file_name, "rb") as file:
            # 读取文件数据
            # 当文件不报错
            file_dict = {'file': file}
            r = requests.post('%s/upload' % url, files=file_dict)
            print(r.text)
        file.close()
        print(' %s 传输完成！' % file_name)

    # # 上传文件到服务器
    # file = {'file': open('hello.txt', 'rb')}
    # r = requests.post('http://127.0.0.1:8000/upload', files=file)
    # print(r.text)


def query_file():
    # 查询fpath下的所有文件
    r1 = requests.get('%s/getfiles' % url, data={'fpath': r'download/'})
    print(r1.text)


def download_file():
    # 下载服务器download目录下的指定文件
    r2 = requests.get('%s/download' % url, data={'filename': 'hello_upload.txt', 'path': r'upload/'})
    file = r2.text  # 获取文件内容
    basepath = os.path.join(os.path.dirname(__file__), r'download/')
    with open(os.path.join(basepath, 'hello_download.txt'), 'w', encoding='utf-8') as f:  # 保存文件
        f.write(file)


if __name__ == '__main__':

    upload_file()
    # query_file()
    # download_file()




