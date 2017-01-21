r"""
游戏设置模块
    存储所有设置类
"""
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始游戏的设置的属性"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 500
        # 背景色，三基色值
        self.bg_color = (230, 230, 230)
        
        # 飞船的相关属性
        self.ship_speed_factor = 2.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
