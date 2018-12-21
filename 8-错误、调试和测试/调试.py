##调试方法

#1.print
#将所有有可能出错的变量打印出来 
#但将来还要删除，而且运行结果有很多垃圾信息


#2.断言 assert
#凡是用print()来辅助查看的地方，都可以用断言(assert)来替代

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('1')

main()
#
#assert的意思是，表达式n ！= 0 的结果True
#否则，根据程序运行的逻辑，后面的代码会出错
#如果断言失败，assert语句本身就会抛出AssertionError,并打印逗号后的语句

# 程序中如果 assert太多，和print相比也好不到哪里去。
#不过 启用Python解释器时可以用 -o 参数来关闭 assert
# $ python -o err.py
# 此时assert等同于pass


#3.使用logging
#把print()替换为logging是第三种方式，
#和 assert相比，logging不会抛出错误，而且可以输出到文件

import logging

logging.basicConfig(level=logging.INFO)

s = '1'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

#这就是logging的好处，它允许你指定记录信息的级别
#有debug, info, warning, error等几个级别
#当指定info时，debug就不起作用了，指定WARNING时，gebug和info就不起作用了
#logging的另一个好处是通过简单的配置，
#一条语句可以同时输出到不同的地方，比如console和文件

# 4.pdb
#启动Python的调试器pdb, 让程序以单步方式运行， 
# 可以随时查看运行状态。
#err.py
s = '1'
n = int(s)
print(10 / n)
#
#这种方法理论上是万能的,但是太麻烦了，
# 如果有一千行代码，要打很多行命令

#pdb 还有另一种调用方式pdb.set_trace()
#在import pdb 之后
#只需要 在可能出错的地方放置一个pdb.set.trace(),就可以设置一个断点
# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace()     # 运行到这里会自动暂停
print(10 / n)
#
#暂停后用命令 
# p查看变量 c 继续运行  q 退出pdb
# 这个方式比直接启动pdb单步调试效率要高很多，但是效率还是很低


##使用IDE
##断点，单步执行， 效率会高很多




