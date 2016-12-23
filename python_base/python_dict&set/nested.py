# -*- coding: utf-8 -*-

# 字典列表

# 外星人字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# 外星人列表，每个元素都是一个描述外星人的字典
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 创建一个空列表，存储外星人
aliens = []

# 循环0-29次：创建30个绿色的alien
for alien_number in range(30):
    # print(alien_number)
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 列表切片：显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print('...')

# 显示创建了多少个外星人
print('Total number og aliens: ' + str(len(aliens)))

# 列表切片：修改前三个外星人的属性
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'


# 显示修改后的外星人列表
for alien in aliens[:5]:
    print(alien)
print('...')

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'

# 显示修改后的外星人列表
for alien in aliens[:5]:
    print(alien)
print('...')


# 在字典中存储列表
# 列表作为值存储在字典中，与键相关联

# 字典中存储配料列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# 概述所点的比萨
print('You ordered a ' + pizza['crust'] + '-crust pizza ' +
    'with the fllowing toppings:')
# 用键‘toppings’访问配料列表
for topping in pizza['toppings']:
    print('\t' + topping)

# 循环字典中的列表值
favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'adward': ['ruby', 'go'],
    'phil': ['python', 'shell'],
}
# 变量languages存储字典中的每个值，是一个列表
for name, languages in favorite_language.items():
    if len(languages) == 1:
        print('\n' + name.title() + '\'s favorite language are:')
    else:
        print('\n' + name.title() + '\'s favorite languages are:')
    # 循环字典值:languages——列表
    for language in languages:
        print('\t' + language.title())


# 字典中存储字典

# 用户字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

# 遍历users，键存储在变量username，字典值存储在user_info
for username, user_info in users.items():
    print('\nUsername: ' + username)
    # 访问内部用户信息字典
    full_name = user_info['first'] + '' + user_info['last']
    location = user_info['location']
    
    print('\nFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())

