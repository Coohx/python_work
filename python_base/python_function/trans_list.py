# -*- coding: utf-8 -*-

def greet_users(names):
    """向列表中每位用户发出简单的问候"""
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usernames = ['hannah', 'coohx', 'margot']
# 将用户列表传递给函数
greet_users(usernames)


# 模拟3D打印工作
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # 模拟3D模型打印过程
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_modles):
    """显示打印好的所有模型"""
    print('\nThe following models have been printed:')
    for complete_model in completed_models:
        print(complete_model)

# 创建未打印的设计列表
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


# 调用打印函数和显示函数

# 列表传递给函数，函数就可对其修改，这个修改是永久性的
#print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 列表已经被函数修改，输出为空列表
# print(unprinted_designs)

# 传递列表副本，不影响原始列表

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# 列表已经被函数修改，输出为空列表
print(unprinted_designs)


# 用户简介profile

# **user_info中的两个星号让Python创建一个user_info的空字典，并将接收到的
#所有名称-值都封装到这个字典中
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    # 将用户的姓&名加入到字典中
    profile['first_name'] = first
    profile['last_name'] = last
    
    # 遍历字典user_info中的键-值对
    for key, value in user_info.items():
        profile[key] = value
    # 返回字典
    return profile

# 向函数传递必选参数和任意数量的key-value参数
user_profile = build_profile('xin', 'huang',
                            location = 'XAUT',
                            field = 'Linux')
print(user_profile)

# {'last_name': 'huang', 'location': 'XAUT', 'field': 'Linux', 'first_name': 'xin'}


# 我的信息
def my_info(first, last, **user_info):
    my_profile = build_profile(first, last, **user_info)
    print(my_profile)
    for info in my_profile:
        """info 会循环字典的key"""
        print(info + ': ' + str(my_profile[info]))
# 统计我的信息，并打印
my_info('xin', 'huang',
        age = 21,
        gender = 'M',
        field = 'Linux')
