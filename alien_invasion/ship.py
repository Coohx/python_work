#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class Ship():
    """模拟飞船的类，控制飞船的大部分行为"""

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其位置"""
        # 指定绘制飞船的游戏窗口
        self.screen = screen
        # 让飞船的获取其速度设置
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        # image.load()返回一个表示飞船的surface
        self.image = pygame.image.load('images/ship.bmp')
        # get_rect()获取surface的属性
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部
        # rect.centerx表示每个矩形对象中心的x坐标
        self.rect.centerx = self.screen_rect.centerx
        #self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        # rect的centerx等属性只能存储整数值
        # 临时新属性，用于存储小数值，进行中间过程的小数运算
        self.center = float(self.rect.centerx)

        # 移动状态标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 右移 ,防止移出屏幕边缘
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.senter进行移动过程中的小数运算
            self.center += self.ai_settings.ship_speed_factor
        # 左移，防止移出屏幕边缘
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据计算后的self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """根据rect矩形对象在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

