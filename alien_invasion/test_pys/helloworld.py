#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

import pygame

from settings import Settings
import game_functions as gf
from beauty_girl import Girl

def blue_sky():
    """蓝色窗口"""
    pygame.init()
    sky_settings = Settings()
    sky_settings.bg_color = (200, 200, 200)
    screen = pygame.display.set_mode(
        (sky_settings.screen_width, sky_settings.screen_height), )
    pygame.display.set_caption("Hello Xiong Jie")
   # 一个gilr对象 
    girl = Girl(screen)
    while True:
        gf.check_events()
        screen.fill(sky_settings.bg_color)
        girl.girl_blitme()
        pygame.display.flip()

blue_sky()
