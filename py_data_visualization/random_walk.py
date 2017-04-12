r"""
模拟随机漫步的类,随机地选择前进方向,并前进随机距离
三个属性:
    - 存储随机漫步次数的变量
    - 列表1: 存储随机漫步经过的每个点的x坐标
    - 列表2: 存储随机漫步经过的每个点的y坐标
"""
# 使用choice()行走做出选择
from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_max_points = num_points

        # 所有随机漫步开始于(0, 0)
        # 存储x/y值的列表
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步,直到漫步包含所需数量的点
        while len(self.x_values) < self.num_max_points:
            # 决定前进方向以及这个方向前进的距离
            # 1,向右 -1,向左
            x_direction = choice([1, -1])
            # 随机选择0~4之间的整数,给出行走距离
            x_distance = choice([0, 1, 2, 3, 4])
            # 确定沿x轴行走的距离
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

