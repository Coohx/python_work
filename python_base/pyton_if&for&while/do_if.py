# -*- coding: utf-8 -*-
# if 语句进行条件判断
# Python用冒号(:)组织缩进，后面是一个代码块，一次性执行完

# if/else 简单判断
age = 17
if age >= 18:
    print('you are a adult.')
    print('Welcome!')
else:
    print('You should not stay here, Go home!')

# if/elif/else 多值条件判断

age = 3
if age >= 18:
    print('adult!')
elif age > 6:
    print('teenager!')
else:
    print('kid! Go home!')

# if 从上往下判断，若某个判断是True，就忽略后面的判断。
age = 20
if age >= 6:
    print('teenager!')
elif age > 18:
    print('adult!')
else:
    print('kid! Go home!')

# if 支持简写
tmp = 12
if tmp:
    print('The bool is True.')


# input() 返回字符串, if进行数值判断时要转为整数
age = int(input('Please enter your age: '))
if age > 18:
    print('Welcome!')
else:
    print('Go home!')

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 计算小明的BMI指数，用if-elif判断并打印

height = 1.75
weight  =80.5
bmi = weight / (height ** 2)

if bmi < 18.5:
    status = '过轻'
elif bmi < 25:
    status = '正常'
elif bmi < 28:
    status = '过重'
elif bmi <= 32:
    status = '肥胖'
else:
    status = '严重肥胖'
print('Xiao Ming BMI is: %.2f,%s!' % (bmi, status))

# 关键字in
requested_toppings = ['mushroom', 'onions', 'pineapple']
print('mushroom' in requested_toppings)

# if-elif 省略 else代码块
age = 12
price = 0
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print('Your admission cost is $' + str(price) + '.')

# 多个并列的if，检查所有条件

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print ('Adding extra pepperoni.')

print('\nFinished making your pizza!')
