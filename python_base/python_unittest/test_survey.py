# -*- coding: utf-8 -*-
# Date: 2016-12-23
# 测试一个类

import unittest
# 导入要测试的类
from survey import AnonymousSurvey

# 测试用例
class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    
    def setUp(self):
        """
        创建一个被测试类的对象和一个用于测试的答案列表，供测试方法使用
        
        """
        question = "What language did you first learn to speak?"
        # 将被测试类实例化后作为当前类的一个属性，可以在后面的所有方法中使用
        self.my_survey = AnonymousSurvey(question)
        # self前缀保证了这个列表可以在后面的测试方法中被使用
        self.responses = ['English', 'Spanish', 'Chinese']
    
    def test_store_single_response(self):
        """测试存储单个答案是否成功？"""
        self.my_survey.store_response(self.responses[0])
        # 使用断言判断是否出错
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        """测试存储三个答案会被妥善存储"""
        # 存储三个答案
        for response in self.responses:
            self.my_survey.store_response(response)
        # 使用断言检查答案是否已经存储到类的实例中
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
