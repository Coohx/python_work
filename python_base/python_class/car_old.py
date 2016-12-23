# -*- coding: utf-8 -*-
# 使用类模拟现实情景

# Car类
class Car():
    """模拟汽车的一个类"""
    
    def __init__(self, test_make, test_model, test_year):
        """初始化汽车属性"""
        self.make = test_make
        self.model = test_model
        self.year = test_year
        # 创建属性odometer_reading,并设置初始值为0
        # 指定了初始值的属性，不需要为它提供初始值的形参
        self.odometer_reading = 0
    
    def get_descriptive(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    # 用于在内部更新属性值的方法
    def update_odometer(self, mileage):
        """
        将里程表的读数设置为指定的值
        禁止将里程表的读书调小
        """
        # 只有新指定的里程数大于当前里程数时，才允许修改这个属性值
        if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    # 用于递增属性值的方法
    def increment_odometer(self, miles):
        """将里程表读书增加制定的量"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


# 创建一个实例
my_new_car = Car('audi', 'A4', 2016)
# 调用类中的方法
print(my_new_car.get_descriptive())
my_new_car.read_odometer()

# 直接修改实例的属性值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 调用类内部编写的方法修改属性值
my_new_car.update_odometer(32)
my_new_car.read_odometer()
# 23小于当前属性值32，禁止修改
my_new_car.update_odometer(23)


# 创建实例——二手车
my_used_car = Car('subaru', 'outback', 2013)
print("\n" + my_used_car.get_descriptive())

# 二手车已经跑的里程数
my_used_car.update_odometer(23500)
my_used_car.read_odometer()

# 我又行驶了100英里
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
