# -*- coding -*-
# Python function

# abs()求绝对值
absolute = abs(-99)
print('abs(-99) =', absolute)

# max()求最大值 
maxmium = max(1, 2, 9, -8)
print('max(1, 2, 9, -8) =', maxmium)

# 数据类型转换函数

# int()把其他数据类型转换为整形
print('int(\'123\') =', int('123'))

print('int(12.34) =', int(12.34))

# float() 浮点数
print('float(\'12.34\') =', float('12.34'))
print('float(12) =', float(12))

# str() 字符串
print('str(3.21) =', str(3.21))
print('str(False) =', str(False))

# bool() 布尔型
print('bool(1) = ', bool(1))
# 空字符串为False
print('bool(\'\') = ', bool(''))


# 函数’别名‘ 
# 将函数名赋给一个变量即可
absolute = abs
print('abs(-3) =', absolute(-3))
