#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 名 + 姓
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 名 + 中间名 + 姓
# 给中间名指定默认值，并移到形参列表末尾
def get_formatted_name(first_name, last_name, middle_name = ''):
    """返回整洁的姓名"""
    # Python 将非空字符串解读为True
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

# 调用函数时，默认值使实参变成可选的
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)


# 返回一个字典
def build_persion(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    # 将名和姓封装到字典
    persion = {'first': first_name, 'last': last_name}
    # 返回表示人的字典
    return persion

# 打印返回值，文本信息存储在一个字典中
musician = build_persion('jimi', 'hendrix')
print(musician)


# 扩展表示人的字典
# 存储一个人的年龄，如果有的话（可选项）
def build_persion(first_name, last_name, age = ''):
    """返回一个字典，其中包含有关一个人的信息"""
    # 将名和姓封装到字典
    persion = {'first': first_name, 'last': last_name}
    # 返回表示人的字典
    if age:
        persion['age'] = age
    return persion

# 打印返回值，文本信息存储在一个字典中
musician = build_persion('jimi', 'hendrix', age = 22)
print(musician)


# 问候用户
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# while 无限循环
while True:
    print('\nPlease tell me your name:')
    # 每次提供用户输入时，都提供退出途径
    print('(enter \'q\' at any time to quit)')
    
    f_name = input('First name: ')
    # 用户可以选择退出
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')


# 统计城市
def city_country(city, country):
    city_info = city + ', ' + country
    return city_info.title()
#print(city_country('Xian', 'China'))
#print(city_country('Santiago', 'Chile'))
#print(city_country('Los Angeles', 'Amrican'))

while True:
    print('\nPlease tell me your city and country.')
    print('(enter \'quit\' at any time  to quit.)')
    
    city_name = input('city_name: ')
    if city_name == 'quit':
        break
    # 输入为空时，重新输入
    if city_name == '':
        continue
    
    country_name = input('country_name: ')
    if country_name == 'quit':
        break
    if city_name == '':
        continue
    
    city_info = city_country(city_name, country_name)
    print('\nYour infomation: ' + city_info)
