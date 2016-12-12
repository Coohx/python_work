# -*- coding: utf-8 -*-
# Python for循环


# for var in 循环对象
names = ['Coohx', 'Bob', 'Adan']
for name in names:
    print(name)

# range(n)函数生成0 ~ n-1范围内的整数
sum_1 = 0
for var in range(101):
    sum_1 = sum_1 + var
print('0 + 1 + 2 + ... + 100 = %s' % sum_1)

# 求100以内所有奇数的和
sum_2 = 0
num = 99
# while 循环体
while num > 0:
    sum_2 = sum_2 +num
    num = num - 2
print('1 + 3 + 5 + ... + 99 = %s' % sum_2)

# contunue 结束本次循环，进入下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)


sum_1 = 0
# break 直接跳出循环
for var in range(101):
    if var > 50:
        break
    sum_1 = sum_1 + var
print(sum_1)
