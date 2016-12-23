# -*- coding: utf-8 -*-
# Date: 2016-12-20

"""导入Python标准库中的模块，并使用其中的函数和类"""

from collections import OrderedDict
from random import randint

# 利用OrderedDict类创建一个空的有序字典实例
favorite_languages = OrderedDict()

# 给有序字典赋值
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['merlin'] = 'python'
favorite_languages['phil'] = 'ruby'
favorite_languages['vicky'] = 'python'

# 遍历字典，将会按照添加顺序有序输出
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")


# 类，掷骰(tou)子

class Die():
    """模拟掷骰子"""
    
    def __init__(self, sides=6):
        """初始化骰子属性"""
        # 默认6个面
        self.sides = sides
    
    def roll_die(self):
        """模拟随机掷一次出现的面"""
        # 函数randint()返回一个位于指定范围内的整数
        rand_side = randint(1, self.sides)
        print("The side is " + str(rand_side) + ".")


# 6面骰子
die_6 = Die()
die_6.roll_die()

# 10面骰子
die_10 = Die(10)
die_10.roll_die()
