# -*- coding: utf-8 -*-
# Author: Huang Xin
# Date: 2016-12-02
# 字符串处理

name = "huang xin"
# 方法 title()使每个英文单词的首字母大写
print(name.title())

name = "Huang Xin"
# upper()使所有英文字母大写
print(name.upper())
# lower()使所有英文字母小写
print(name.lower())

first_name = "huang"
last_name = "xin"
# 加号(+)用于合并字符串
full_name = first_name + " " + last_name
#print("Hello," + " " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

# Python 中使用换行符(\n)&制表符(\t,4个全角的宽度,8byte)
print("Language:\nPython\nC\nShell")
print("Language:\n\tPython\n\tC\n\tShell")

# Python 删除空白的方法
favorite_language = " Python "
# rstrip()剔除字符串结尾的空白
print(favorite_language.rstrip())
# lstrip()剔除字符串开头的空白
print(favorite_language.lstrip())
# strip()删除字符串两端的空白
print(favorite_language.strip())

print("中文测试！")
