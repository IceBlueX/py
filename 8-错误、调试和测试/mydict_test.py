import unittest

from mydict import Dict

class TestDict(unittest.TestCase):                  #编写测试类，从unittest.Testcase继承

    def setUp(self):                                #setUp和tearDown每个测试函数都会执行一遍
        print('setUp...')                           #开始前执行setUP 结束后执行tearDown
                                                    #可用于执行数据库的开闭
    def tearDown(self):
        print('tearDown...')

    def test_init(self):                            #以test开头的被认为是测试方法
        d = Dict(a=1, b='test')                     #不以test开头的，测试的时候不会执行
        self.assertEqual(d.a, 1)                    #断言 d.a==1
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_Keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):           #该断言，期待抛出指定类型的Error
            value = d['empty']                      #当d['empty']访问不存在时，断言抛出KeyError
    
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):     #该断言，期待抛出指定类型的Error
            Value = d.empty                         #当d.empty访问不存在时，断言抛出AttributeError

###运行单元测试
# 1，直接加两行代码，就可以当正常脚本运行

if __name__ == '__main__':
    unittest.main()                 

