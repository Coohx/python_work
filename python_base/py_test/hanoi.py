#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 20180323

def hanoi(n, starting_point='a', transfer='b', destination='c'):
    """汉诺塔"""
    n = int(n)
    if n == 1:
        print(starting_point, '-->', destination)
        return
    else:
        # 大于一个盘子时,将最下面的一个盘子和上面的n-1个盘子看成两个盘子即可
        # 第一步,将上面的n-1个盘子从a借助c移动到b上面
        hanoi(n-1, starting_point, destination, transfer)
        # 第二步,将最下面的一个盘子从a借助b移动到c上面
        hanoi(1, starting_point, transfer, destination)
        # 第三部,将b上面的n-1个盘子借助a移动到c上面
        hanoi(n-1, transfer, starting_point, destination)
n = input("Please input the number of the plate on the pillar. ")
hanoi(n)
