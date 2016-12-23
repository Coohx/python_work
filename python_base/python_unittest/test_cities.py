# -*- coding: utf-8 -*-
# Date: 2016-12-23

import unittest
from name_function import custom_info

class CityTestCase(unittest.TestCase):
    """测试函数custom_info"""
    
    def test_cities_country(self):
        """能正确的返回City, Country这样的信息吗"""
        customer_info = custom_info('xian', 'china')
        self.assertEqual(customer_info, 'Xian, China')
    
    def test_cities_country_population(self):
        """
        能正确返回City, Country - population xxx这样的信息吗
        """
        customer_info = custom_info('xian', 'china', '6000000')
        self.assertEqual(customer_info, 'Xian, China - population 6000000')

unittest.main()
