#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """运行游戏"""
    # 初始化背景设置
    pygame.init()
    # 创建设置的一个对象
    ai_settings = Settings()
    # display.set_mode()返回screen对象(surface),设置游戏窗口的screen_width*screen_height像素
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height), )
    # 窗口说明文字
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        # 检测到键盘事件后更新飞船的状态
        ship.update()
        # 对编组中的每个子弹调用update(),删除已消失的子弹
        gf.update_bullets(bullets)
        # 及时更新屏幕上的图像
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()

