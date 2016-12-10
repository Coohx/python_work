# -*- coding: utf-8 -*-
# 字典 集合

# 字典是一种 key:value 的数据组织方式

score_dict = {
              'Huangxin': 98,
              'Linus': 99,
              'Jobs': 92
}
# 脱义字符具有相对性，当前字符是否需要转义，要和它前面的那个字符对比。
print('score_dict[\'Huangxin\'] =', score_dict['Huangxin'])
print('score_dict[\'Linus\'] =', score_dict['Linus'])
print("score_dict['Jobs'] =", score_dict['Jobs'])

# 给字典添加键值对
score_dict['Coohx'] = 89
print("d[\"Coohx\"] =", score_dict['Coohx'])

# 重复赋值会覆盖之前的value
score_dict['Andam'] = 100
print('Andam_old score is: %s' % score_dict['Andam'])
score_dict['Andam'] = 60
print('Andam_new score is: %s' % score_dict['Andam'])

#  in 可用于查看 key 是否存在于字典中，返回布尔值
find_message = 'XiMi' in score_dict
if find_message:
    print("%s! XiMi does exist the dictnary." % find_message)
else:
    print("%s! XiMi do not exist the dictnary." % find_message)


# 字典提供get()方法查找key，存在时返回key对应的value
find_message = score_dict.get('Linus')
print('score_dict.get(\'Linus\') =',find_message)

# 字典提供get()方法查找key，不存在时返回None,
find_message = score_dict.get('XiMi')
print('score_dict.get(\'XiMi\') =',find_message)
# 也可以返回自己指定的value
find_message = score_dict.get('XiMi', -1)
print('score_dict.get(\'Linus\', -1) =',find_message)


# pop(key) 从字典中删除一个key
print(score_dict)
score_dict.pop('Jobs')
print(score_dict)

print('\n\n')


# 集合set类似字典，但只存储 key，没有对应的value，相当于存储普通元素

# set()方法将一个列表初始化为集合
num_set = set([1, 2, 3])
print('集合:', num_set)

# 重复元素在set中自动被过滤
num_set = set([1, 2, 2, 3, 3, 4])
print('集合:', num_set)

# add()方法用于向集合中添加元素
print('集合:', num_set)
# 添加重复元素会被忽略
num_set.add(4)
print('集合:', num_set)
num_set.add(5)
print('集合:', num_set)

# remove()方法可以删除集合中元素
num_set.remove(2)
print('集合:', num_set)

# 集合可以进行交集、并集运算
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print('集合s1: ', s1)
print('集合s2: ', s2)
# & 集合交集(与)运算
s3 = s1 & s2
print('s1与s2的交集: ', s3)
# | 集合并集(或)运算
s4 = s1 | s2
print('s1与s2的并集: ', s4)

key_1 = [1, 2, 'linux', 99.99]
# 向集合中添加一个列表元素，会出错！
#s4.add(key_1)
print(s4)


# 字典中的 key 必须是不可变对象

a_list = [1, 2, 3]
# 元组一旦定义不能在改变，元组本身是不可变对象
a_tuple = (1, 2, 3)
# 元组的元素可能是一个可变对象
aa_tuple = (1, 2, a_list, 3)

# 字典的 key 必须是不可变对象
a_dict = {
          'name': 'Qmihuang',
          'gender': 'male',
          a_tuple: [4, 5, 6]
}
print('a_dict["aa_tuple"] =',a_dict[a_tuple])

