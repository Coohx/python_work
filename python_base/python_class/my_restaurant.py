# -*- coding: utf-8 -*-
# Date: 2016-12-20

from restaurant import Restaurant, IceCreamStand

# 福尔餐馆实例
restaurant = Restaurant('Fuer', 'cheese')
# 打印餐馆的属性
print("The first restaurant is " + restaurant.restaurant_name + ".")
print("The best cuisine of " + restaurant.restaurant_name +
    " is " + restaurant.cuisine_type + ".")
# 调用类定义中的方法
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 直接修改属性值
restaurant.read_number()
restaurant.number_serverd = 320
restaurant.read_number()
# 调用方法修改属性值
restaurant.set_number_serverd(500)
restaurant.read_number()
# 递增就餐人数
restaurant.increment_number_serverd(150)
restaurant.read_number()


# 冰淇淋小店实例
icecream_restaurant = IceCreamStand('Merlin ice', 'love')
# 父类方法
icecream_restaurant.describe_restaurant()
icecream_restaurant.open_restaurant()
icecream_restaurant.set_number_serverd(200)
icecream_restaurant.read_number()
# 子类特有方法
icecream_restaurant.read_icecream()
