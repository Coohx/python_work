# -*- coding: utf-8 -*-

import math

# 求解一元二次方程
def quadratic(a, b, c):
    # 参数类型检查
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    elif not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    elif not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    elif a == 0:
        print('a can\'t be 0!')
    else:
        if b ** 2 - 4 * a * c < 0:
            print('no real roots')
        else:
            x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2  * a)
            x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2  * a)
    return x1, x2
# x1 x2 被放在一个元组中输出
x1, x2 = quadratic(4, 4, 1)
# 格式化输出时，两个以上的输出要用括号扩起
print('x1 = %s  x2 = %s' % (x1, x2))
