# -*- coding: utf-8 -*-
# Author: Huang xin
# Date: 2016-12-14

r'''
 统计调查用户喜欢的山脉
'''
# 空字典用于将回答和被调查者关联起来 
responses = {}

# 标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示被调查者输入名字和回答
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')
    
    # 将回答存储在字典中
    responses[name] = response
    
    # 询问是否有人要继续参与调查,退出循环
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False

# 显示结果
print('\n--- Poll Result ---')
for name,response in responses.items():
    print(name.title() + ' Would like to climb ' + response + '.')

