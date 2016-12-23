# -*- coding: utf-8 -*-

# 描述外星人的字典
alien_0 = {'color': 'green', 'points': 5}

# 添加键-值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 删除键值对
print(alien_0)
del alien_0['points']
print(alien_0)

# 使用多行来定义字典
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'adward': 'ruby',
    'phil': 'python',
    }
# 多行输出
print("sarah's favorite language is " +
    favorite_language['sarah'].title() +
    ".")

# 遍历列表

# 便利所有的键-值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
# 方法items()返回一个键-值对列表，包含字典中所有的键-值对。
for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)
print('\n')

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'adward': 'ruby',
    'phil': 'python',
    }

# 定义两个朋友
friends = ['phil', 'sarah']
# 遍历字典中的所有键
# 方法keys()返回一个列表，包含字典中所有的键。
for name in favorite_language.keys():
    print(name.title())
    
    if name in friends:
        print(' Hi ' + name.title() +
        ', I see your favorite language is ' +
        favorite_language[name].title() + '!')


# 遍历字典时，默认也是只遍历所有的键
for name in favorite_language:
    print(name.title())
# 函数sorted()对keys()方法返回的键列表进行排序，返回按顺序排列的键
for name in sorted(favorite_language.keys()):
    print(name.title() + ', thank you for taking the poll.')

print('The following languages have been mentioned:')
# 只遍历字典中的值——方法values()
for language in favorite_language.values():
    print(language.title())

# 将values()返回的值列表集合化，去除重复的值
for language in set(favorite_language.values()):
    print(language.title())

