# -*- coding: utf-8 -*-

prompt = '\nTell me something, and I will repeat it back to you:'
prompt += '\nEnter \'quit\' to end the program. '
message = ''
while message != 'quit':
    message = input(prompt)
    # 避免打印'quit'
    if message != 'quit':
        print(message)


# 使用标志，使程序简洁

prompt = '\nTell me something, and I will repeat it back to you:'
prompt += '\nEnter \'quit\' to end the program. '

# 标志程序处于活动状态
active = True
while active:
    message = input(prompt)
    
    # 事件发生，改变标志值，改变程序状态
    if message == 'quit':
        active = False
    else:
        print('Your input is: ' + message)

# 作业

status = True
while status:
    print('(Enter \'quit\' to quit.)')
    age = input('Please input your age: ')
    if age == 'quit':
        status =False
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        elif age > 12:
            price = 15
        print('The price is $%s' % price)

# while循环中处理列表和字典

# 待验证用户列表
#  和一个用于存储验证后用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# while循环中进行验证
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

# 显示已验证用户，for循环遍历
print('\nThe following users have been confirmed: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除列表中指定的元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

