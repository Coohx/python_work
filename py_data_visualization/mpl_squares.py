#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块pyplot包含许多绘图函数
import matplotlib.pyplot as plt

# 输入值x
input_values = [1, 2, 3, 4, 5]
# 输出y
squares = [1, 4, 9, 16, 25]
# linewidth决定了plot()绘制出图形线条的粗细
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题,并给坐标轴加上标签
# 参数fontsize指定图表中文字的大小
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# 设置坐标轴刻度标记的字号大小
# axis='both',对x、y轴都生效
plt.tick_params(axis='both', labelsize=10)

# 函数show()打开matplotlib查看器，显示绘制的图形
plt.show()

