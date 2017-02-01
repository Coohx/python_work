#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
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

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    #alien = Alien(ai_settings, screen)

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        # 检测到键盘事件后更新飞船的状态
        ship.update()
        # 对编组中的每个子弹调用update(),删除已消失的子弹
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        # 及时更新屏幕上的图像
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()

