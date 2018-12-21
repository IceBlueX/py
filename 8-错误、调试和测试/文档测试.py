import re       # 引入正则表达式
m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))

#自动执行，写在注释中的代码

def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>>abs(1)
    1
    >>>abs(-1)
    1
    >>>abs(0)
    0
    '''

    return n if n >= 0 else (-n)

print(abs(-2))
#
# 这样写上注释，会更加明确的告诉函数的使用者
# 该函数的期望输入和输出
# 并且，Python内置的“文档测试”（doc）模块可以直接提取注释中的代码并执行测试
# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确
# 只有测试异常的时候，可以用 ...表示中间一大段烦人的输出

#用doctest来编写上次的Dict类
#详见 mydict2.py

