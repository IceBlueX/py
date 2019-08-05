#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ORM for MySql
异步驱动
连接数据库 及数据库的基础操作
"""

__author__ = 'LBK'

import asyncio, logging

import aiopg


def log(sql, args=()):
    logging.info('SQL: %s' % sql)


# 创建进程池 每个请求都可以从数据库获得相应的数据 无需频繁的打开和关闭数据库连接
# 节省连接时间并且代码复用
async def create_pool(loop, **kw):
    logging.info('creat database connection pool...')
    global __pool
    __pool = await aiopg.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 5432),
        user=kw['user'],
        password=kw['password'],
        database=kw['database'],
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


#
#
#
# 基础数据库操作
# select 查询语句
async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.acquire() as conn:
        async with conn.cursor() as cur:  # psycopg2.extras.DictCursor
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()

        logging.info('rows returned: %s' % len(rs))
        return rs


# 增删改
async def execute(sql, args, autocommit=True):
    log(sql)
    async with __pool.acquire() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor() as cur:  # psycopg2.extras.DictCursor
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected


#
#
#
# ORM开始
# 要从上层调用者的角度来写

def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)


class Field(object):

    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)


class StringField(Field):

    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)


class IntegerField(Field):

    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


class FloatField(Field):

    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)


class TextField(Field):

    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)


# 元类 通过元类的映射读取到user的映射信息
class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info('  found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    # 找到主键
                    if primaryKey:
                        raise ValueError('StandardError: Duplicate primary key for field: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise ValueError('StandardError: Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '%s' % f, fields))  # sql中写入列名

        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey  # 主键属性名
        attrs['__fields__'] = fields  # 除主键外的属性名

        # 主要sql语句
        attrs['__select__'] = 'select %s, %s from %s' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into %s (%s, %s) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update %s set %s where %s=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from %s where %s=?' % (tableName, primaryKey)

        return type.__new__(cls, name, bases, attrs)


# 所有ORM映射的基类
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)

        return value

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        """
        find objects by where clause.
        :param where:
        :param args:
        :param kw:
        :return:
        """

        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []

        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('orderBy')
            sql.append(orderBy)

        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))

        rs = await select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        """
        find number by select and where
        :param selectField:
        :param where:
        :param args:
        :return:
        """

        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]

        if where:
            sql.append('where')
            sql.append(where)

        rs = await select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    async def find(cls, pk):
        """
        find object by primary key.
        :param pk:
        :return:
        """
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s' % rows)

    async def update(self):
        args = list(map(self.getValue, self.__field__))
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warn('failed to update by primary key: affected rows: %s' % rows)

    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warn('failed to remove by prinmary key: affected rows: %s' % rows)


# yield from user.save()










