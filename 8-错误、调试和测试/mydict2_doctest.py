# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support as x.y style.

    >>> dl = Dict()
    >>> dl['x'] = 100
    >>> dl.x
    100
    >>> dl.y = 200
    >>> dl['y']
    200
    >>> d2 = Dict(a = 1, b = 2, c = '3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
#
#什么输出也没有有说明我们编写的mydict运行都是正确的
#当模块正常导入时，doctest不会被执行
#只有在命令行直接运行时，才执行doctest
#不必担心doctest会在非测试环境下运行