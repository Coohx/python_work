# -*- coding: utf-8 -*-
# Python 数据类型：tuple(元组)

# tuple 一旦定义不能修改
classmates = ('Coohuang', 'Bob', 'Adam')
print(classmates)
# tuple 除了不能apped()、insert()之外，其他操作和list相同
print(classmates[-1])
print(len(classmates))

# 元组定义时就要确定下来
tuple_01 = (1, 2, 3.333)
print(tuple_01[1])

# 定义一个空的tuple
tuple_02 = ()
print(tuple_02)

# 定义只有一个元素的tuple,这个元素后面要有一个逗号，却别于数学公式中的小括号
# tuple_01 = (1)  等价于 tuple_01 = 1
tuple_01 = (1,)
print(tuple_01)

# ‘可变的’tuple，实际是元素list在变
tuple_03 = ('Python', 'Google', ['A', 'B'])
print(tuple_03)
tuple_03[2][0] = 'a'
tuple_03[2][1] = 'b'
print(tuple_03)


it_home = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple
apple = it_home[0][0]
print(apple)
# 打印Python
python = it_home[1][1]
print(python)
# 打印Lisa
name = it_home[2][2]
print(name)
# pop()最多一个参数
print(it_home.pop(1))
print(it_home)
