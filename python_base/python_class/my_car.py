# -*- coding: utf-8 -*-
# Date: 2016-12-20

from car import Car
from electric_car import ElectricCar

# 燃油汽车
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 电动汽车
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.update_battery(85)
my_tesla.battery.get_range()

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla_new = ElectricCar('tesla', 'rodaster', 2016)
print(my_tesla_new.get_descriptive_name())

# 导入整个模块
"""
import car

# 句点表示法引用模块中的类
my_beetle = car.Car('volkswagen', 'beetle', 2016)
my_tesla_new = car.ElectricCar('tesla', 'rodaster', 2016)

"""
