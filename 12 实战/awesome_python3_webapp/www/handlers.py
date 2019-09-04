#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LBK'

"""
处理URL，对不同的路由做出不同的反应
这里的路由及各种参数要和前端一一对应
"""

import re, time, json, logging, hashlib, base64, asyncio
import markdown2
from aiohttp import web

from coroweb import get, post
from apis import *

from models import User, Comment, Blog, next_id
from config import configs


COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret


def check_admin(request):
    if request.__user__ is None or not request.__user__.admin:
        raise APIPermissionError()


def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p


def user2cookie(user, max_age):
    """
    通过用户生成cookie字符串
    :param user:
    :param max_age:
    :return:
    """
    # cookie 字符串的格式为 用户ID+过期时间+哈希值
    # id + expires + sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)


def text2html(text):
    lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'),
                filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)


async def cookie2user(cookie_str):

    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = await User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user

    except Exception as e:
        logging.exception(e)
        return None

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

# 前端框架
#
#
# ## 管理页面包括：
#
# #### 评论列表页：GET/manage/comments
# #### 日志列表页：GET/manage/blogs
@get('/manage/blogs')
def manage_blogs(*, page='1'):
    return {
        '__template__': 'manage_blogs.html',
        'page_index': get_page_index(page)
    }

# #### 创建日志页：GET/manage/blogs/create
@get('/manage/blogs/create')
def manage_creat_blog():
    return {
        '__template__': 'manage_blog_edit.html',
        'id': '',
        'action': '/api/blogs'
    }

# #### 修改日志页：GET/manage/blogs/
# #### 用户列表页：GET/manage/users
#
#
# ## 用户浏览页面包括：
#
# #### 注册页：GET/register
@get('/register')
async def register():
    return {
        '__template__': 'register.html'
    }

# #### 登录页：GET/signin
@get('/signin')
async def signin():
    return {
        '__template__': 'signin.html'
    }

# #### 注销页：GET/signout
@get('/signout')
async def signout(request):
    referer = request.headers.get('Referer')
    r = web.HTTPFound(referer or '/')
    r.set_cookie(COOKIE_NAME, '-deleted-', max_age=0, httponly=True)
    logging.info('user signed out.')
    return r

# #### 首页：GET/
@get('/')
async def index(request):
    # users = await User.findAll()
    # print('在 handlers.py->index中 根据路径获得后端返回的数据', users)
    # for u in users:
    #     print(u.name, u.email)
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200),
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs,
        # '__user__': request.__user__
    }

# #### 日志详情页：GET/blog/:blog_id
@get('/blog/{id}')
async def get_blog(id):
    blog = await Blog.find(id)
    comments = await Comment.findAll('blog_id=?', [id], orderBy='created_at desc')
    for c in comments:
        c.html_content = text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)
    return {
        '__template__': 'blog.html',
        'blog': blog,
        'comments': comments
    }

#
#
# ## 后端API包括：
#
# #### 获取日志：GET/api/blogs
@get('/api/blogs')
async def api_blogs(*, page='1'):
    page_index = get_page_index(page)
    num = await Blog.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    print('在 handlers.py->api_blogs() 读取的条数及位置', (p.offset, p.limit))
    blogs = await Blog.findAll(orderBy='created_at desc', limit=(p.limit, p.offset))
    return dict(page=p, blogs=blogs)

# #### 创建日志：POST/api/blogs
@post('/api/blogs')
async def api_creat_blog(request, *, name, summary, content):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')

    blog = Blog(
        user_id=request.__user__.id,
        user_name=request.__user__.name,
        user_image=request.__user__.image,
        name=name.strip(),
        summary=summary.strip(),
        content=content.strip()
    )
    await blog.save()
    return blog

# #### 修改日志：POST/api/blogs/:blog_id
@get('/api/blogs/{id}')
async def api_get_blog(*, id):
    blog = await Blog.find(id)
    return blog

# #### 删除日志：POST/api/blogs/:blog_id/delete
# #### 获取评论：GET/api/comments
# #### 创建评论：POST/api/blogs//:blog_id/comments
# #### 删除评论：POST/api/comments/:comment_id/delete
# #### 创建新用户：POST/api/users
@post('/api/users')
async def api_register_user(*, email, name, passwd):
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not passwd or not _RE_SHA1.match(passwd):
        raise APIValueError('passwd')

    users = await User.findAll('email=?', [email])
    if len(users) > 0:
        raise APIError('register: failed', 'email', 'Email is already in use.')
    uid = next_id()
    sha1_passwd = '%s:%s' % (uid, passwd)
    user = User(
        id=uid,
        name=name.strip(),
        email=email,
        passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(),
        image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest()
    )
    await user.save()

    # make session cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

# #### 获取用户：GET/api/users
# #### 验证邮箱及密码并在本地建立cookie：GET//api/authenticate
@post('/api/authenticate')
async def authenticate(*, email, passwd):
    if not email:
        raise APIValueError('email', 'Invalid email.')
    if not passwd:
        raise APIValueError('passwd', 'Invalid password.')
    users = await User.findAll('email=?', [email])
    if len(users) == 0:
        raise APIValueError('email', 'Email not exist.')
    user = users[0]

    # 开始检查密码
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(passwd.encode('utf-8'))
    if user.passwd != sha1.hexdigest():
        raise APIValueError('passwd', 'Invalid password.')
    # 验证完毕, 开始设置cookie 二十四小时内有效
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r


# @get('/api/user')
# async def api_get_users():
#     users = await User.findAll(orderBy='created_at desc')
#     for u in users:
#         u.passwd = '******'
#     return dict(users=users)


