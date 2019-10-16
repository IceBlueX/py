import os
import sys
import time
import flask
from flask import request, send_from_directory

interface_path = os.path.dirname(__file__)
sys.path.insert(0, interface_path)  # 将当前文件的父目录加入临时系统变量

# 新建flask服务
server = flask.Flask(__name__)

# get方法：指定目录下载文件
# 客户端从服务端下载文件
@server.route('/download', methods=['get'])
def download():
    fpath = request.values.get('path', '')  # 获取文件路径
    fname = request.values.get('filename', '')  # 获取文件名
    if fname.strip() and fpath.strip():
        print(fname, fpath)
        if os.path.isfile(os.path.join(fpath, fname)) and os.path.isdir(fpath):
            return send_from_directory(fpath, fname, as_attachment=True)  # 返回要下载的文件内容给客户端
        else:
            return '{"msg":"参数不正确"}'
    else:
        return '{"msg":"请输入参数"}'


# get方法：查询当前路径下的所有文件
# 服务端发送当前文件夹列表给客户端
@server.route('/getfiles', methods=['get'])
def getfiles():
    fpath = request.values.get('fpath', '')  # 获取用户输入的目录
    print(fpath)
    if os.path.isdir(fpath):
        filelist = os.listdir(fpath)
        files = [file for file in filelist if os.path.isfile(os.path.join(fpath, file))]
    return '{"files":"%s"}' % files


# post方法：上传文件的
# 接收来自客户端的文件
@server.route('/upload', methods=['post'])
def upload():
    fname = request.files.get('file', stream=True)  # 获取上传的文件

    if fname:
        new_fname = r'../upload/' + fname.filename

        with open(new_fname, "wb") as f:
            # 读取文件数据
            # 当文件不报错
            for chunk in fname.iter_content(chunk_size=float(1024*1024)):
                if chunk:
                    f.write(chunk)
                else:
                    print('接收完成！')
        f.close()
        return '{"code": "ok"}'
    else:
        return '{"msg": "请上传文件！"}'


if __name__ == '__main__':

    # 绑定8000 端口 一直运行
    server.run(port=8000, debug=True)


