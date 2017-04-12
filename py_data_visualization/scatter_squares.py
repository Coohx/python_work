#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# 函数scatter()在指定位置绘制一个点
# 实参s设置绘制点的尺寸
plt.scatter(2, 4, s=200)
# 设置图标标题并给坐标轴加上标签
plt.title("Square Numners", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()

