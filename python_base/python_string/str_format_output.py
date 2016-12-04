# -*- coding: utf-8 -*-
# Formatting output 

# Py中采用 % 是先格式化输出

# 字符串中有几个占位符%?，%后面就要跟几个变量或者值，顺序要对应，多于一个时用括号扩起来
# 在字符串内部，%s 表示用字符串替换
message = 'you win!'
print('Hi, Hung Xin, %s' % message)

name = 'Coohx'
# %d 用整数替换 
print('Hello %s, you have $%d.' % (name, 10000))

# 格式化输出整数 & 浮点数

answer = 5 / 3
print('5 / 3 = %s' % answer)
# 小数点后保留一位
print('5 / 3 = %3.1f' % answer)
# 指定输出占4位，不够时以空白补齐
print('5 / 3 = %4.1f' % answer)
# 指定输出占4位， 不够时以0补齐
print('5 / 3 = %04.1f' % answer)
print('%.2f' % 3.141592653)

# 输出 % 号
s1 = 88
s2 = 99
r = (s2 - s1) / s1 * 100 
print('The growth rate is: %.2f%%' % r)
