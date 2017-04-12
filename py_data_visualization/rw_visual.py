#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态,就不断模拟随机漫步
while True:
    # 创建一个RandomWalk实例,生成数据
    rw = RandomWalk(6000)
    rw.fill_walk()

    # 列表用于颜色映射，包含各点x行走的先后顺序
    point_numbers = list(range(rw.num_max_points))
    # 给各个点着色，反应它们的先后顺序
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)

    # 重新绘制起点和终点,呈现随机漫步的起点和终点
    plt.scatter(0, 0, c='green', edgecolor='none', s=5)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none',
               s=5)

    # 隐藏坐标轴 函数axes()将每条坐标轴的可见性设置为False
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # 设置窗口的尺寸
    # 函数figure()用于指定图标的宽度、高度、分辨率和背景色
    # 元组figsize指出了窗口的尺寸,单位为英寸
    #plt.figure(figsize=(2, 5))

    # Display a figure
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

