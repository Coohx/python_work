r"""
dump a beauty girl.
"""

import pygame

class Girl():
    """初始化女孩头像并设置其位置"""

    def __init__(self, screen):
        self.screen = screen
        self.girl_image = pygame.image.load('images/girl.png')
        self.girl_rect = self.girl_image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将女孩头像放在屏幕中央
        self.girl_rect.centerx = self.screen_rect.centerx
        self.girl_rect.centery = self.screen_rect.centery

    def girl_blitme(self):
        """在指定窗口中绘制图像"""
        self.screen.blit(self.girl_image, self.girl_rect)

