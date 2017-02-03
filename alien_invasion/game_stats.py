class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        # 第一次运行时需要调用，运行中也需要调用
        self.reset_stats()
        # 游戏启动时处于活动状态
        self.game_active = True

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的信息"""
        self.ship_left = self.ai_settings.ship_limit
