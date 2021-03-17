# 测试脚本test开头
import unittest


class Test_Demo(unittest.TestCase): # 测试类test开头

    def test_01(self): # 测试方法test开头
        """"测试加法"""
        a=1+2
        self.assertEqual(a,3)

    @unittest.skip('跳过')
    def test_02(self): # 测试方法test开头
        """"测试加法"""
        a=1+2
        self.assertEqual(a,3)

if __name__ == '__main__':
    # 参数是0，什么都不输出
    # 参数是1，成功输出.,报错输出F
    # 参数是2，输出详情信息
    unittest.main(verbosity=2)