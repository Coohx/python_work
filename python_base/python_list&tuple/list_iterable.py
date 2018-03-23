#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 迭代:可迭代对象

def FindMinAndMin(L=[]):
    """查找一个列表中的最大最小数"""
    length = len(L)
    if length == 0:
        print("Please retry!")
        return None
    else:
        min_num = L[0]
        max_num = L[-1]
        for num in L:
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num
        return (min_num, max_num)
numbers = [12, 3443, 43, 4, 5.4, 4535, 9999, 22, 32, 3232,]
print(FindMinAndMin(numbers))
