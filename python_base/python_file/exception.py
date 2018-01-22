# -*- coding: utf-8 -*-
# Date: 2016-12-22
# Python 异常处理

# 异常处理
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
 
# try-except-else
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        # 可能引发异常的代码
        answer = int(first_number) / int(second_number)
    # 可能引发的异常对象
    except ZeroDivisionError:
        print("You can't divide by zero!")
    # 没有引发异常时该执行的代码
    else:
        print(answer)

# 处理 FileNotFoundError 异常

filename = r'..\text_files\alice_old.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

# 方法split()将字符串以空格为分隔符拆分，存储到列表中
title = "Alice in wonderland"
print(title.split())
# ['Alice', 'in', 'wonderland']

# 方法count()确定单词或短语在字符串中出现的次数
print(title.count('in'))

# 分析文本
filename = r'..\text_files\alice.txt'

try:
    with open(filename) as f_obj:
        # contents是一个长字符串
        contents = f_obj.read()
        # 计算单词in出现的次数
        number_words = contents.lower().count('in')
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
    print("The word 'in' appears " + str(number_words) +
        " times in the novel.")

print("\n")

def count_words(filename):
    """计算一个文件中大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)
        # 记录错误日志
        error_file = r'..\text_files\error.log'
        with open(error_file, 'a') as f_obj:
            f_obj.write("The file " + filename + " is not found!\n")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
            " words.")

# 将文件名存在列表中
filenames = [r'..\text_files\alice.txt',
    r'..\text_files\siddhartha.txt',
    r'..\text_files\moby.txt',
    r'..\text_files\little_women.txt']
for filename in filenames:
    count_words(filename)

