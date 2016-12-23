"""
    一组用于表示电动汽车的类
"""

from car import Car

class Battery():
    """模拟电动汽车的电瓶"""
    
    def __init__(self, battery_size=20):
        """初始化电瓶属性"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + " -kWh battery.")
    
    def update_battery(self, battery):
        """更新电瓶的容量"""
        self.battery_size = battery
    
    def get_range(self):
        """打印一条描述电瓶续航里程的消息"""
        # 要有这个初始值，否则变量ranges会在没有定义的情况下被引用而报错
        ranges = 100
        if self.battery_size == 70:
            ranges = 240
        elif self.battery_size == 85:
            ranges = 270
        message = "This car can go approximately " + str(ranges)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """模拟电动汽车的独特之处"""
    def __init__(self, elec_make, elec_model, elec_year):
        """
        初始化父类的属性， 再初始化电动汽车特有的属性
        """
        super().__init__(elec_make, elec_model, elec_year)
        self.battery = Battery()
