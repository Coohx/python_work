"""
    模块restaurant.py
    一组描述餐馆的类
"""

class Restaurant():
    """模拟餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐馆的属性"""
        # 属性是带有self前缀的restaurant_name和cuisine_type，并非上面的形参
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # 给属性设置默认值
        self.number_serverd = 0

    def describe_restaurant(self):
        """描述餐馆"""
        print("\nThe restaurant name is " + self.restaurant_name.title() + ".")
        print("The best cuisine of the restaurant is " +
            self.cuisine_type.title() + ".")

    def open_restaurant(self):
        """描述餐馆的营业状态"""
        print("The restaurant is opening, Welcome!")

    def read_number(self):
        """输出餐馆的就餐人数"""
        if self.number_serverd > 0:
            print("The restaurant has " + str(self.number_serverd) +
                " diners at the moment.")
        else:
            print("The restaurant has " + str(self.number_serverd) +
                " diner at the moment.")

    def set_number_serverd(self, number):
        """更新餐馆的就餐人数"""
        self.number_serverd = number

    def increment_number_serverd(self, numbers):
        """就餐人数进行递增"""
        self.number_serverd += numbers


# 冰淇淋小店——继承餐馆类的属性及方法
class IceCreamStand(Restaurant):
    """模拟冰淇淋小店"""

    def __init__(self, icecream_name, icecream_type):
        """初始化父类属性"""
        super().__init__(icecream_name, icecream_type)

        # 冰淇淋小店特有属性
        self.flavors = ['cheery', 'chocolate', 'juicy peach', 'strawberry']

    def read_icecream(self):
        """描述所有的冰淇淋口味"""
        print("\nHere are all icecreams:")
        for flavor in self.flavors:
            print("\t" + flavor + ".")
