# -*- coding: utf-8 -*-
# Date: 2016-12-23
# 一个待测试的类

class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    
    def __init__(self, tmp_question):
        """存储一个问题， 并为存储答案做准备"""
        self.question = tmp_question
        self.responses = []
    
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    
    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)
    
    def show_results(self):
        """先是收集到的所有答卷"""
        print("Syrvey results:")
        for response in self.reponses:
            print('- ' + response)
