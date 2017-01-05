import sys

import pygame

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 检测到按键事件(KEYDOWN)
        elif event.type == pygame.KEYDOWN:
            # 每个事件只与一个键相关联
            if event.key == pygame.K_RIGHT:
                # 只负责修改标志位
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        # 检测松开按键事件(KEYUP)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到最新的屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

