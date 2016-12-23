# -*- utf-8 -*-
# Date: 2016-12-22

print("Give me two numbers, I'll add up them.")
while True:
    print("Enter 'q' to quit.")
    fir_num = input("Enter the first number: ")
    if fir_num == 'q':
        break
    sec_num = input("Enter the second number: ")
    if sec_num == 'q':
        break
    try:
        answer = int(fir_num) + int(sec_num)
    # 捕获错误，进行处理
    except ValueError:
        print("Please input a integer not a string.\n")
    else:
        print(fir_num + ' + ' + sec_num + ' = ' + str(answer))

