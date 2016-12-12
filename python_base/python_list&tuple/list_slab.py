# -*- coding: utf-8 -*-

# 列表部分元素——切片
players = ['a', 'b', 'c', 'd', 'e']
# 输出索引从0开始到索引为3-1=2的列表元素
print(players[0:3])
# ['a', 'b', 'c']

# 省略第一个索引，从头开始切片
print(players[:4])
# ['a', 'b', 'c', 'd']

# 省略终止索引，切片终止于列表末尾
print(players[2:])
# ['c', 'd', 'e']

# 负数索引返回列表末尾任何切片
print(players[-3:])
# ['c', 'd', 'e']
print(players[-4:])

# 使用切片，编列前三个列表元素

print('Here are the first three players on my team: ')
# 切片出列表前三个元素
for player in players[:3]:
    print(player.title())

# 1-10内切出3-9
nums = list(range(1,11))
print(nums)
for num in nums[2:9]:
    print(num)
print(nums)


# 利用切片复制列表

my_foods = ['pizza', 'carrot cake', 'falafel']
# 不指定任何索引的情况下，从列表中提取一个切片，从而创建了这个列表的副本
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print('My friend\'s favorite foods are:')
print(friend_foods)


my_foods = ['pizza', 'carrot cake', 'falafel']
# 简单的赋值列表，只是让另一个变量也指向这个列表
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print('My friend\'s favorite foods are:')
print(friend_foods)
