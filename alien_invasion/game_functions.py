import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果子弹还没有达到上限，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 检测到按键事件(KEYDOWN)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # 检测松开按键事件(KEYUP)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到最新的屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 编组bullets的方法sprite()返回一个列表
    for bullet in bullets.sprites():
        # 绘制每个子弹
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    # 更新编组中每个子弹的位置
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 检查是否有子弹击中了外星人,若击中，就删除相应的子弹和外星人
    # groupcollide()返回一个字典，字典中每个键都是一颗子弹，相应的值都是
    # 被击中的外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 检查外星人编组是否为空，执行相应的操作"""
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    # Python中用括号将公示括起来，可将代码分成多行以免超过79个字符
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # 计算每一个外星人的坐标
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    # 将新创建的外星人添加到编组aliens中
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
        alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                row_number)

def change_fleet_direction(ai_settings, aliens):
    """
    当外星人到达屏幕边缘时，将整群外星人下移，并改变他们的方向
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    """有外星人人到达屏幕边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ship_left > 0:
        # 将余下的飞船数减1
        stats.ship_left -= 1
        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人，并将飞船重新放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.2)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """
    检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    # 方法spritecollideany()找到与飞船发生碰撞的成员后停止遍历编组
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

