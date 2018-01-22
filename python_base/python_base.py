#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author：Huang Xin
# Date：2016-12-02
# 基础练习

# Python syntax is indentation(tab = 4)
# Python 使用井号作为注释符(#)

# int型
age = 22
# str()函数将int型数据转换为字符串类型，与字符串混合输出。
message = "Happy " + str(age) + "rd Birthday!"
print(message)

print(4 + 4)
print(10 - 2)
print(2 * 4)
print(8 / 1)

integer = 18829027464
message = "The phone number of my is " + str(integer) + "."
print(message)

# input()
message = input('Tell me something, and I will repeat it back to you: ')
print(message)

# 将较长的提示信息放在变量中
prompt = 'If you tell us who you are, we can personalize the message you see.'
# 追加一部分信息
prompt += '\nWhat is your first name? '

name = input(prompt)
print('\nHello, ' + name + '!')


age = input('How old are you? ')
age = int(age)
if age >= 18:
    print('Welcome, Adult!')
else:
    print('Using python, you can fly!')
print(r'''
     instance
     keep doing!
     three starts!''')
