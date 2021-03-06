#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取日期、最高气温和最低气温

# csv文件的名称存储在filename中
#filename = 'sitka_weather_07-2014.csv'
filenames = (
    'death_valley_2014.csv',
    'sitka_weather_2014.csv',
)
for filename in filenames:
    with open(filename) as f_obj:
        # 利用文件对象f_obj创建阅读器对象reader
        # csv.reader()返回一个阅读器对象,是csv格式(记录&字段)
        reader = csv.reader(f_obj)
        # 模块csv内的函数next()返回csv文件中的下一行,第一次调
        #用返回文件头,是一个列表,每个字段作为一个列表元素

        # 阅读器对象reader停留在第一行
        header_row = next(reader)
        #print(header_row)

        # 打印文件头详细信息
        for index, colum_header in enumerate(header_row):
            # enumerate()获取列表元素的索引和值,生成一个索引序列
            #print(index, colum_header)
            pass

        # dates存储日期,highs存储最高气温,lows存储最低气温
        sitka_dates, sitka_highs, sitka_lows = [], [], []
        death_dates, death_highs, death_lows = [], [], []
        # 阅读器对象reader从其停留的地方继续向下读取CSV文件,每次
        # 都自动返回当前所处位置的下一行.
        # 此时位于第二行,即真实的数据行
        for row in reader:
            # 读取文件时的异常处理
            try:
                # 将数据行的第一列即日期转换成datetime对象
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                # csv文件中的数据是字符串格式,需要转化成数字,用于绘图
                high = int(row[1])
                # 从每行的第4列提取每天的最低气温
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                if filename == "sitka_weather_2014.csv":
                    sitka_dates.append(current_date)
                    sitka_highs.append(high)
                    sitka_lows.append(low)
                else:
                    #filename == "death_valley_2014.csv":
                    death_dates.append(current_date)
                    death_highs.append(high)
                    death_lows.append(low)

# 根据数据绘制图形

# 函数figure()设置绘图窗口的尺寸、分辨率&背景色
fig_1 = plt.figure(1, dpi=150, figsize=(10, 6))
# (x, y), c指定数据点的颜色,alpha指定颜色的透明度
plt.plot(sitka_dates, sitka_highs, c='red', alpha=0.5)
plt.plot(sitka_dates, sitka_lows, c='blue', alpha=0.5)
# 方法fill_between()对指定范围的数据进行着色
# fill_between()接收1个x值系列和2个y值系列,facecolor指定填充区域的颜色
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.3)
# 设置图形格式
plt.title("SITKA Daily high and low temperatures - 2014", fontsize=12)
# 绘制斜的日期标签
plt.xlabel('Date(2014)', fontsize=10)
fig_1.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=10)
# 函数tick_params()设置坐标轴刻度的样式
plt.tick_params(axis='both', which='major', labelsize=8)

fig_2 = plt.figure(2, dpi=80, figsize=(10, 8))
# "b--"指定线型
plt.plot(death_dates, death_lows, "b--", c='black', alpha=0.5)
plt.plot(death_dates, death_highs, c='green', alpha=0.5)
# 方法fill_between()对指定范围的数据进行着色
# fill_between()接收1个x值系列和2个y值系列,facecolor指定填充区域的颜色
plt.fill_between(death_dates, death_highs, death_lows, facecolor='blue', alpha=0.3)
# 设置图形格式
plt.title("DEATH Daily high and low temperatures - 2014", fontsize=12)
# 绘制斜的日期标签
plt.xlabel('Date(2014)', fontsize=10)
fig_2.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=10)
# 函数tick_params()设置坐标轴刻度的样式
plt.tick_params(axis='both', which='major', labelsize=8)
plt.show()

