#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

x_values = list(range(1,1001))
# 使用列表解析式自动生成列表
y_values = [x**2 for x in x_values]

# 函数scatter()在指定位置绘制点
# 实参s指定点的尺寸
# 参数edgecolor='none'删除数据点的轮廓
# 参数c指定点的颜色
#plt.scatter(x_values, y_values, c='red', edgecolor='none', s=10)
#plt.scatter(x_values, y_values, c=(0, 0.3, 01.6), edgecolor='none', s=10)

# 参数c设置为一个y值列表(y值较小的点为浅蓝色,较大的点为深蓝色),参数cmap告诉pyplot使用哪个颜色映射
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.GnBu,
            edgecolor='none', s=10)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numners", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=10)
# 设置每个坐标轴的取值范围
# 函数axis()需要提供四个值:x和y坐标轴的最小值&最大值
plt.axis([1, 1100, 0, 1100000])

# 保存图表,第一个参数指定文件名，第二个参数指定将图表空白区域剪裁掉
#plt.savefig('square_plot.png', bbox_inches='tight')

plt.show()

