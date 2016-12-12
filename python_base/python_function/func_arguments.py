# -*- coding: utf-8 -*-
# 函数参数

def muti(x, n):
    """求解x的n次方"""
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
# 位置参数2,3按照位置顺序赋值给x,n
print(muti(2, 3))
print(muti(3, 3))


# 默认参数：函数定义时指定形参的默认值
# 默认参数要放在后面，因为它前面的参数依然是一个位置参数
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + '\'s name is ' + pet_name.title() + '.')

# 调用函数时只提供了一个参数，是位置实参，被关联到函数定义中的第一个形参
# 由于没有提供第二个实参，Python将使用默认形参值
describe_pet('wille')

# 也可以显式的给默认形参提供实参值，需要指出参数的名字
describe_pet('harry', animal_type = 'hamster')
# 等效的函数调用
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')


# 默认参数的大坑——默认值为可变对象引起的
# 默认值为一个列表（可变数据对象）
def add_end(l=[]):
    l.append('end')
    return l

# 提供实参，覆盖默认值
print(add_end([1, 2, 3]))
# 使用默认值时出现”坑“
print(add_end())
print(add_end())
# 连续多次调用，默认值被修改掉，因为它(列表)是一个可变的对象
print(add_end())


# 可变数量的参数
# *toppings 实际是一个空元组
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
# pepperoni 意大利香肠  cheese 奶酪  
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# 0 个参数
make_pizza()


# 对函数封装后的元组进行循环
def make_pizza(*toppings):
    """概述要制作的比萨"""
    print(toppings)
    print('\nMaking a pizza with the following toppings:')
    # toppings 在函数内部实现是一个元组
    for topping in toppings:
        print('- ' + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 将已有的元组/列表作为实参调用可变参数
# 在列表名前加一个*，作为可变参数
toppings_owned = ['mushrooms', 'meat', 'green peppers', 'extra cheese']
# *toppings_owned 表示把toppings_owned 这个列表的所有元素作为可变参数传进去
make_pizza(*toppings_owned)


# 关键字参数 key-value
# 用两个星号(**)标识关键字参数kw,kw是一个空字典
def person(name, age, **kw):
    """打印个人信息"""
    print('name:', name, 'age:', age, 'other:', kw)

# 只传入位置参数
person('QmiHuang', 30)
# name: QmiHuang age: 30 other: {}

# 传入任意个数的关键字参数
person('Coohx', 35, city = 'BeiJing')
person('HuangXin', 22, city = 'ShenZhen', job = 'Ops')

# 也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
person_dict = {'city': 'BeiJing', 'job': 'Engineer'}
# **person_dict 表示把 person_dict 的所有 key-value 用关键字参数传入到函数的 **kw 参数
person('Jack', 24, **person_dict)


# 命名关键字参数
# 指定关键字实参的key的名字
# 函数内部非字典组织
# 星号(*)后面的参数被视为命名关键字参数，调用时需指定形参的名字
def person(name, age, *, city, job):
    """输出个人信息"""
    print(name, age, city, job)

# 调用时需指定形参名
person('Jack', 24, city = 'BeiJing', job = 'Engineer')
# Jack 24 BeiJing Engineer

# 关键字实参的顺序无关紧要
person('Jack', 24, job = 'Engineer', city = 'BeiJing')


# 可变数量的参数后面的 命名关键字参数 不需要星号(*)分隔
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('Andam', 25, city = 'BeiJing', job = 'Engineer')
# Andam 25 () BeiJing Engineer


# 指定命名关键字的默认值，简化调用
def person(name, age, *, city = 'BeiJing', job):
    print(name, age, city, job)

# 调用时可以不传入city值
person('Jack', 34, job = 'Ops')
# Jack 34 BeiJing Ops


# 组合参数
# 定义顺序：必选参数、默认参数、可变参数、命名关键字参数、关键字参数

# 位置参数a、b  默认参数c   可变参数args  关键字参数kw
def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# 位置参数a、b  默认参数c   命名关键词参数d  关键字参数kw
def f2(a, b, c = 0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# Python 自动按照参数位置和参数名把对应的实参传进去
# *args组织为一个元组   关键字参数kw组织为一个字典
f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}

# 默认参数c被调用时提供的实参覆盖
f1(1, 2, c = 3)
# a = 1 b = 2 c = 3 args = () kw = {}

# 可变参数按位置接收非key-value实参
f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}

# **kw 接收key-value 实参
f1(1, 2, 3, 'a', 'b', x = 99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}

# 命名关键字形参d 接收 d = 99 的实参   kw按顺序接收最后一个key-value
f2(1, 2, d = 99, ext = None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# 将参数放在tuple 和 dict 调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}

# tuple 元素按顺序传入并关联到对应的形参
# 字典key-value 赋给关键字参数
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'x': '#', 'd': 99}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}

# 元组和字典元素按顺序传入，被相应的形参接收
f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
