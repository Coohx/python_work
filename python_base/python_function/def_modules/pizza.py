def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
    # toppings 在函数内部实现是一个元组
    for topping in toppings:
        print('- ' + topping)
