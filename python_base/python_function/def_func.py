# -*- coding: utf-8 -*-
# Python 自定义函数

# 导入math包,调用里面的数学函数
import math

r"""
 自定义函数
   def 函数名(参数):
   \"""文档字符串(docstring)\"""
       函数体(缩进块)
"""
def my_abs(num):
    """求绝对值"""      # 文档字符串，用于描述函数做什么
    if num >= 0:
        # return 返回函数结果，退出函数
        return num
    else:
        num = - num
        # 没有return语句时，函数返回'None'
        return num

print("abs(-5) = %d" % my_abs(-5))


# 空函数  pass语句
def nop():
    # pass相当于占位符，什么都不做，可以让函数先运行起来
    pass


# pass 可以用于语句中
num = 10
if num >= 0:
    # pass 
    pass


# 参数类型检查

def my_abs(num):
    # 检查函数传入参数类型，出错时报错。
    # 只允许参数 num 是整数或浮点数
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')
    if num >= 0:
        return num
    else:
        return - num

print(my_abs(-99))


# angle = 0 默认参数
def move(x, y, step, angle=0):
    """求位移坐标"""
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    # 函数值存到一个元组中进行返回
    return nx, ny

# x, y 按位置顺序接收函数返回的多个存在元组中的值
x, y = move(100, 100, 60, math.pi / 6)
# x y 分别输出对应位置上的元组中的值
print(x, y)
r = move(100, 100, 60, math.pi / 6)
# r 直接输出多个值组成的元组
print(r)

 
def display_message():
    """打印学习内容"""
    print("I learned how to define a function!")
display_message()


def favorite_book(title):
    """打印我最喜欢的书名"""
    print("One of my favorite books is " + title.title() + ".")
favorite_book('Python Crash Course')
