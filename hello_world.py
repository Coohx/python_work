# -*- coding: utf-8 -*-
# Author：Huang Xin   
# Date：2016-12-02
# First Python program.


message_more = "The language 'Python' is named after Monty Python, not the snake."
name = input("Please enter your name: ")
print("hello " + name + ", " + message_more)


# Pythonz字符串可以单引号或双引号，很灵活。
message_new = 'I told my friend, "Python is my favorite language!"'
print(message_new)

message_more = 'Albert Einstein once said, "A person who never made a mistake never tried anything new."'
print(message_more)

message_less = "One of Python's strengths is its diverse and supportive community."
print(message_less)

message = '"A person who never made a mistake never tried anything new."'
famous_person = "Albert Einstein"
print(famous_person + " " + "once said," + " " + message)

old_person = " Jing Ke "
handsome_son = " Jing Tianming"
beautiful = "Gao Yue "
# 合并字符串，要么加号，要么逗号(逗号自动空一格)。
print("Qinsmoon" + "\n\t" + old_person.strip() + "\n\t" + handsome_son.lstrip() + "\n\t" + beautiful.rstrip())
print("Qinsmoon is charming," + " " + handsome_son.lstrip() + " " + "is brave and smart!")
