#!/usr/bin/env python3
# -*- coding: utf-8  -*-
# Date: 2016-12-23
# json模块

# 导入整个模块
import json

numbers = [2, 3, 5, 8, 13, 21]

# .json表示文件存储的数据为JSON格式
filename = 'number.json'
with open(filename, 'w') as f_obj:
    # 将数字列表存储到number.json中
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    # 读取json格式的文件对象，存储到变量中
    numbers = json.load(f_obj)

print(numbers)

# 存数用户信息

# 如果之前存储了用户名就读取它
# 否则，就提示用户输入用户名并存储它
userfile = 'username_old.json'
try:
    with open(userfile) as f_obj:
        # json格式用json.load()读取
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name: ")
    with open(userfile, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")


def greet_user():
    """问候用户，并指出其名字"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("Enter your name: ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")


r"""
重构函数 greet_user(), 将任务分拆到多个函数中，每个函数都只执行单一而清晰的任务。
"""
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        # 找不到就返回None，不做其他事
        return None
    else:
        # 返回预期的值
        return username


def get_new_username():
    """提示用户输入用户名,存储新用户"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，指出其名字"""
    username = get_stored_username()
    current_username = input("Please enter your name: ")
    if username:
        if current_username == username:
            print("Welcome back, " + username + "!")
        else:
            print("Username is wrong! Please reset it.")
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")

greet_user()


def favorite_number():
    """存储你喜欢的数字"""
    num_file = r'../text_files/numbers.json'
    favor_num = input("Enter a number that is your favorite. ")
    with open(num_file, 'w') as f_obj:
        json.dump(favor_num, f_obj)

def read_favor_number():
    """读取用户最喜欢的数字"""
    num_file = r'../text_files/numbers.json'
    try:
        with open(num_file) as f_obj:
            favor_num = json.load(f_obj)
    except FileNotFoundError:
        pass
    else:
        print("I know your favorite number! It's " + favor_num + ".")

def print_number():
    """向用户输出最喜欢的数字"""
    favorite_number()
    read_favor_number()

print_number()
