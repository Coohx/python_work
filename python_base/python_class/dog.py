# -*- coding: utf-8 -*-
# Date: 2016-12-16

r"""
    python class 面向对象编程
    类:模拟现实世界中的事物和情景,定义一大类对象都有的通用行为
    对象:基于类创建，自动具备类中的通用行为
    实例:根据类创建对象被称为实例化
    程序中使用类的实例
"""
# 创建Dog类

# 类名首字母大写
class Dog():
    # Python2.7中的类创建：class Dog(object):
    """一次模拟小狗的简单尝试"""
    
    # 创建实例时方法__init__()会自动运行
    # self 形参必须位于最前面,创建实例时，自动传入实参self
    # 每个与类相关联的方法都会自动传递实参self
    def __init__(self, name, age):
        """初始化属性names和age"""
        # 两个属性names和age都有前缀self
        self.name = name
        self.age = age
    
    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        """模拟小狗被命令打滚"""
        print(self.name.title() + " rolled over!")

# 创建一条特定小狗的实例

# 调用Dog类中的方法__init__()自动运行，创建一个表示特定小狗的实例
# 使用‘Willie’和6来设置属性name和age
# 方法__init__()自动返回一个实例存储在变量my_dog中，包含类中的所有'行为'
my_dog = Dog('Willie', 6)

# 访问实例的属性——句点表示法
# 但在Dog类内部引用这个属性时，使用self.name
# 实例名.属性名
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 调用方法——创建实例后，使用句点表示法访问Dog类中定义的方法
# 语法： 实例名.方法
# Python在Dog类中查找方法sit()并运行其代码
my_dog.sit()
my_dog.roll_over()


# 创建多个实例

# 每个实例(小狗)都有自己的一组属性(姓名、年龄)
your_dog = Dog('lucy', 7)

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
