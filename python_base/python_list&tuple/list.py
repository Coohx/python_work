# -*- coding: utf-8 -*-
# Python 内置数据类型：list(列表)


# 列表可直接赋值
language = ['Python', 'Perl', 'Shell', 'Java']
print(language)

# len() 用于计算列表元素的个数
count_language = len(language)
print(count_language)

# 使用索引引用列表元素，索引从0开始
print(language[0])

# 索引 -1 代表末尾的元素,一次向前递减
print(language[-1])
print(language[-2])

# 列表中元素类型可以不同，也可以是另一个列表
class_01 = ['Python', 1000, True, 8.888]
print(class_01)
print(class_01[-1])

# 方法append() 向列表尾部追加元素
language.append('lua')
print(language[-1])

# 方法insert() 向列表指定位置插入元素
language.insert(len(language)-1, 'Go')
print(language[-2])

# 方法pop()默认弹出(删除)列表末尾的元素
print(language)
print(language.pop())
print(language)
# pop(i) 删除索引位置i处的元素
print(language.pop(1))
print(language)

# 替换列表元素直接复赋值
print(class_01)
class_01[2] = False
print(class_01)

# 列表元素也可以是一个列表
class_02 = ['Shell', class_01, 0xff]
print(class_02)
print(class_02[1][0])

# 列表元素为空值
class_01 = [ ]
print(len(class_01))

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
# del 直接删除一个元素
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# 方法remove() 删除列表元素'ducati'
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print('The motorcycles' + too_expensive +'is too expensive!')
