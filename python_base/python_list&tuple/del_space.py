#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def trim(s):
    """Delete spaces in a string"""
    # 从开头逐个去除空格
    if s[:1] == " ":
        return trim(s[1:])
    # 从结尾逐个去除空格
    elif s[-1:] == " ":
        return trim(s[:-1])
    # 返回去除完空格的字符串
    else:
        print(s)
origin_str = str(input("Please input a sting: "))
trim(origin_str)
