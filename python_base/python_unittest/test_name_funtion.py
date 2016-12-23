# -*- coding: utf-8 -*-
# Python 测试用例

# 导入模块unittest
import unittest
# 导入要测试的函数
from name_function import get_formatted_name

# 测试用例：一个集成TestCase的类
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    
    def test_first_last_name(self):
        """单元测试：能够正确处理像Merlin Huang这样的姓名吗？"""
        # 调用要测试的函数，存储要测试的返回值
        formatted_name = get_formatted_name('merlin', 'huang')
        # 断言方法assertEqual()用来核实实际结果与期望结果是否相同
        self.assertEqual(formatted_name, 'Merlin Huang')
    
    def test_first_last_middle_name(self):
        """能够正确的处理Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


# 自动运行这个测试用例
unittest.main()
