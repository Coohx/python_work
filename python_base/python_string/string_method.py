# -*- coding: utf-8 -*-
# Author: Huang Xin
# Date: 2016-12-02
# 字符串处理
# Python3 字符串是Unicode编码

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

# r'' 表示 '' 中的字符免手动转义(让输出不换行)
message_0 = r'I like Python, \nabout you?'
message_1 = 'I like Python, \\nabout you?'
print(message_0)
print(message_1)

# 多行字符串: '''多行字符串''' 
print('''line1
line2
line3''')

# int() 将非数值型转换为整形
age = int(input("Please enter your age: "))
if age > 18:
    print(' You are a adult!')
else:
    print(' you are a teenager!')
    
var = 12
print(var)
var = "insist!"
print(var)

print("\n\n\n")


num1 = 123
num2 = 123.456
print(num1, num2)

str1 = 'Hello, world!'
str2 = 'Hello, \'Adam\''
str3 = r'Hello, "Bart"'
str4 = r'''Hello,
Lisa!
Linus!
Taylor!'''
# 做相同的操作时，数据类型要一致。
print(str(num1) + "\n" + str(num2) + "\n" + str1 + "\n" + str2 + "\n" + str3 + "\n" + str4)
