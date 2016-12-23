# -*- coding: utf-8 -*-
# 继承

# python2.7 中的继承
r"""
class Car(object):
    def __init__(self, make, model, year):
        --snip--
   
class ElectricCar(Car):
    def __init__(self, sub_make, sub_model, sub_year):
        \"""super()函数需要两个参数：子类名和对象self\"""
       super(ElectricCar, self).__init__(sub_make, sub_model, sub_year)
        --snip--
"""


# 父类 Car()
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
    
    # 用于在类内部更新属性值的方法
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
    
    def fill_gas_tank(self):
        """给汽车加油"""
        print("Please begin fill gas.")


# Battery类：提取电动车电瓶相关的属性和方法，单独作为一个类，实例化后作为电动汽车的一个属性
class Battery():
    """模拟电动汽车的电池"""
    
    # 可选形参，默认值70
    def __init__(self, battery_size_tmp=20):
        """初始化电瓶属性"""
        self.battery_size = battery_size_tmp
    
    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def update_battery(self, battery):
        """更新电池容量"""
        self.battery_size = battery
    
    def get_range(self):
        """打印电瓶的续航里程"""
        if self.battery_size <= 70:
            range = 240
        elif self.battery_size <= 85:
            range = 270
        elif self.battery_size > 85:
            range = 300
        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


# 子类
class ElectricCar(Car):
    """Car的子类电动车的独特之处"""
    
    # 子类方法__init__接受创建父类实例所需的全部信息
    def __init__(self, sub_make, sub_model, sub_year):
        """
        先初始化父类的属性
        设置电动汽车特有的属性，并初始化
        """
        # 调用父类的__init__()，让子类实例继承父类的所有属性
        super().__init__(sub_make, sub_model, sub_year)
        
        # 使用类Battery()的定义创建一个新的Battery实例，将该实例存储在属性battery中
        self.battery = Battery()
    
    def fill_gas_tank(self):
        """重写父类中的加油方法，电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
    
    def read_make_year(self):
        """子类内部调用从父类继承来的属性：制造年份"""
        print("Superclass contribute: " + str(self.year))


# 子类实例，继承父类的属性和方法
# 调用ElectricCar类中的方法__init__()，进而调用父类Car()中的方法__init__()，
#传入实参'tesla' 'model s' 和 2016
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive())
print(my_tesla.odometer_reading)

# 调用从父类继承来的方法
my_tesla.update_odometer(300)
my_tesla.read_odometer()
my_tesla.increment_odometer(200)
my_tesla.read_odometer()

# 子类特有的方法
#my_tesla.update_battery(100)
#my_tesla.describe_battery()
my_tesla.read_make_year()

# 调用重写后的父类方法
my_tesla.fill_gas_tank()

# 对存储在battery属性中的Battery实例调用方法
my_tesla.battery.describe_battery()
# 通过属性battery调用Battery类中的方法update_battery()更新电池容量
my_tesla.battery.update_battery(85)
my_tesla.battery.describe_battery()
# 通过汽车的属性battery调用Battery类中的方法get_range()描述续航里程
my_tesla.battery.get_range()

