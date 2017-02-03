r"""
游戏设置模块
    存储所有设置类
"""
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始游戏的设置的属性"""
        # 屏幕设置
        self.screen_width = 920
        self.screen_height = 580
        # 背景色，三基色值
        self.bg_color = (230, 230, 230)
        
        # 飞船的相关属性
        self.ship_speed_factor = 2.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        # 下移速度
        self.fleet_drop_speed = 10
        # 1 表示右移，-1表示左移
        self.fleet_direction = 1

