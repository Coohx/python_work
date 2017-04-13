r"""
定义一个骰子，玩游戏，采集数据
"""
from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """
        骰子默认6个面
        num_sides是一个可选参数
        """
        self.num_sides = num_sides

    def roll(self):
        """返回一次投骰子的随机值"""
        # 函数randint()返回1~self.num_sides之间的随机数
        return randint(1, self.num_sides)

