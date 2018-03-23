#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# range() 打印一系列数字
for value in range(0,5):
    print(value)

# 指定步长为2，打印1-10以内的奇数
for value in range(1,21,2):
    print(value)

# list() 创建数字列表
numbers = list(range(1,6))
print(numbers)

# 创建一个列表，其中包含10个整数（1~10）的平方
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print('min(digits) =', min(digits))
print('max(digits) =', max(digits))
print('sun(digits) =', sum(digits))

# 列表解析：将for循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [value ** 2 for value in range(1,11)]
print(squares)


print('1 - 20:')
for num in range(1,1000001):
    #print(num)
    pass


nums = list(range(1,1000001))
print(max(nums))
print(min(nums))
print(sum(nums))

nums_3 = []
for num in range(3, 31):
    if num % 3 == 0:
        nums_3.append(num)
print('3-30 内能被3整除的数: ')
for num in nums_3:
    print('\t' + str(num))

# 3次幂列表
cubes = []
for value in range(1,11):
    cubes.append(value ** 3)
print(cubes)

# 列表解析

cubes_new = [value ** 3 for value in range(1,11)]
print(cubes_new)
