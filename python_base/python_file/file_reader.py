# -*- coding: utf-8 -*-
# Date: 2016-12-21
# python 文件处理

# 读取整个文件

# open()打开指定的文件，返回一个表示文件及其内容的对象，存储到关键字as后面的变量中
file_path = r'..\text_files\pi_digits.txt'
with open(file_path) as file_object:
    # 方法read()读取文件对象file_object的全部内容，以字符串形式返回
    contents = file_object.read()
    print(contents.rstrip())

print(contents)

# 利用for循环逐行读取
file_path = r'..\text_files\pi_digits.txt'
with open(file_path) as file_object:
    # 对文件对象的每行进行遍历
    for line in file_object:
        # 剔除每行末尾的换行符和print语句添加的换行符
        print(line.rstrip())

# 将文件内容的每一行存储到一个列表中
with open(file_path) as file_object:
    # 方法readlines()读取文件对象的每一行，作为一个元素，存储到列表中
    lines = file_object.readlines()
# 遍历存储文件内容的列表
for line in lines:
    print(line.rstrip())

# 使用内存中的文件内容数据

file_name = r'..\text_files\pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

# 存储合并后的文件内容
pi_string = ''
for line in lines:
    # strip()去掉每行两头的空白
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 只输出圆周率小数点后10位，通过字符串切片实现
print(pi_string[:12])

# 检查你的生日是否在圆周率值中
birthday = input("Enter your birthday, in the from mmddyy: ")
# in 直接检查某个字符串是否在已知字符串中
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!") 
else:
    print("Your birthday does not appears in the first million digits of pi!")


# 读取文件
new_file = r'..\text_files\learning_python.txt'

with open(new_file) as file_object:
    new_contents = file_object.read()
    print(new_contents)

with open(new_file) as file_object:
    for line in file_object:
        print(line.strip())

with open(new_file) as file_object:
    lines_new = file_object.readlines()
# replace()替换字符串指定的内容
for line in lines_new:
    print(line.strip().replace('Python', 'C'))
