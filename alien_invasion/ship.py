#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

class Ship():
    """模拟飞船的类，控制飞船的大部分行为"""

    def __init__(self, screen):
        """初始化飞船并设置其位置"""
        # 指定绘制飞船的游戏窗口
        self.screen = screen

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
        # 移动状态标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 右移 1个像素
        if self.moving_right:
            self.rect.centerx += 1
        # 左移
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """根据rect矩形对象在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

