# -*- coding: utf-8 -*-
# recursion function

# 递归函数计算 n! = n * (n-1) * ... * 3 * 2 * 1
def factorial(n):
    if n == 1:
        return 1
    # fact(n) = n * fact(n -1)
    return n * factorial(n - 1)

print('factorial(3) =', factorial(3))
print('factorial(10) =', factorial(10))


# 使用尾递归，优化递归函数的栈溢出
def fact(n):
    return fact_iter(n, 1)

# 要实现尾递归，return 语句不能包含表达式
def fact_iter(num, product):
    if num == 1:
        return product
    # 把每一步的乘积传入到递归函数中
    return fact_iter(num - 1, num * product)

print('fact(10) =', fact(10))

# 汉诺塔
# a 上面n个盘子，借助b，全部将盘子按同样的顺序放到c上

def move(n, a, b, c):
    if n == 1:
        # 最后一步都是 a--> c （这里是a-->c 是形参）
        print('move:', a, '-->', c)
        return
    else:
        # 将a上面的 n-1个 移到 b （会借助c）
        move(n-1, a, c, b)
        # 将a的最下面一个移到c上
        move(1, a, b, c) 
        # 将b上的n-1个移到c上  （会借助a）
        move(n-1, b, a, c)

move(4, 'a', 'b', 'c')
