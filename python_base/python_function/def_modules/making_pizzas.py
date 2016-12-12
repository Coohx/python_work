# -*- coding: utf-8 -*-

# 将pizza.py整个模块导入当前程序
import pizza

# 调用模块pizza中函数
# module_name.function_name()

def make_pizza():
    print('test import module')
make_pizza()

# 并不会覆盖当前程序中的同名的函数
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 导入特定函数 make_pizza
from pizza import make_pizza

# 调用时只需指定函数名
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# as 关键字，导入函数时指定别名
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# as 给模块指定别名
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 导入模块中所有函数
from pizza import *
# 会覆盖当前程序中已有的同名函数
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
