# -*- coding: utf-8 -*-
# Date: 2016-12-21

# programming.txt 不存在，将被自动创建
file_name = r'..\text_files\programming.txt'
# 'w'指定open()以写入模式打开文件
with open(file_name, 'w') as file_object:
    # write()方法向文件对象中写入一个字符串
    file_object.write("I love programming.")


# 在write()语句中包含换行符，写入多行
file_name = r'..\text_files\programming.txt'
# 此次会清空目标文件已经存在的数据
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 给文件追加内容(不清空原有文件内容)

file_name = r'..\text_files\programming.txt'
# 'a'指定open()以附加模式打开文件，进行内容追加
with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

class web():
    """web站点"""
    
    def __init__(self, ip_addr):
        """初始化用户属性"""
        self.ip_addr = ip_addr
    
    def login(self):
        """用户注册"""
        users_file = r'..\text_files\user.txt'
        username = input("Please enter your name: ")
        with open(users_file, 'a') as file_object:
            file_object.write(username + ' ' + self.ip_addr + "\n")
        print("login Success!" + "\nHere is your name: " + username.title())
        print("The web ip is: " + self.ip_addr)

user_vip = web('192.168.8.8')
user_vip.login()


login_flag = True
users_file = r'..\text_files\user.txt'

# 作业： 循环采集用户名字
while login_flag:
    print("(Enter 'q' to quit the login.)")
    username =input("Please enter your name: ")
    
    if username == 'q':
        login_flag = False
    else:
        with open(users_file, 'a') as file_object:
            file_object.write(username + "\n")
        print("Login Success!")

