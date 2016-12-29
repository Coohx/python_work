#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import pygame

# 自定义的设置类
from settings import Settings

def run_game():
    
    #初始化游戏，并创建一个游戏对象
    # 初始化背景设置
    pygame.init()
    
    # 创建类设置的一个实例
    ai_settings = Settings()
    # display.set_mode()返回screen对象(surface),设置游戏窗口screen_width*screen_height像素
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height), )
    
    # 窗口说明文字
    pygame.display.set_caption("Alien Invasion")
    #设置窗口背景色(RGB三基色)
    #bg_color = (230, 230, 230)
    
    # 开始游戏的主循环
    while True:
        
        # 监视键盘和鼠标事件(事件循环)
        for event in pygame.event.get():
            #事件类的一个属性:type
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 对象screen的fill()方法:每次循环时重新绘制屏幕
        screen.fill(ai_settings.bg_color)
        
        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()

