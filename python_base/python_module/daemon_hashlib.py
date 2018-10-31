#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date: 20180803

import hashlib

"""
Python内置的hashlib模块为我们提供了多种安全方便的摘要方法
hashlib模块支持md5(),sha1(), sha224(), sha256(), sha384(), sha512(),
blake2b(), blake2s(), sha3_224(), sha3_256(), sha3_384(), sha3_512(), shake_128(),
shake_256()等多种hash构造方法
"""

# 通过构造函数获取一个hash对象
md5 = hashlib.md5()
# 使用update方法添加消息
# md5.update(b'python is powerful, ')
md5.update(bytes('python is powerful, ', encoding='utf-8'))
# 继续追加
md5.update(b'you should use it.')
# 等价于
# md5.update("python is powerful, you should use it.".encode('utf-8'))


# digest()方法获得 bytes 类型的摘要值
md5_result = md5.digest()
print(md5_result)

# digest_size 属性，消息摘要值的长度
print(md5.digest_size)

# block_size 属性，摘要值的内部块大小
print(md5.block_size)

# 简洁用法

print(hashlib.md5(b"python is powerful, you should use it.").hexdigest())
print(hashlib.sha256(b"python is powerful, you should use it.").hexdigest())


###  hashlib.new(name[, data])
# name是某个算法的字符串名称
# data是可选的bytes类型待摘要的数据

h = hashlib.new('sha256', b'tencent is lalala')
h_resualt = h.hexdigest()
print(h_resualt)


### hashlib模块的常量属性

# hashlib.algorithms_guaranteed  所有平台中，模块支持的hash算法列表
print(hashlib.algorithms_guaranteed)

# hashlib.algorithms_available   当前Python解释器环境中，模块支持的hash算法列表
print(hashlib.algorithms_available)


# hash.name hash对象使用的摘要算法名称
print(md5.name)
print(h.name)


# hash.copy() 哈希对象的拷贝
h_copy = h.copy()
print(h_copy.hexdigest())
h_copy.update(b"xiaomi is bababa")
print(h_copy.hexdigest())


def calc_md5(passwd):
    return hashlib.md5(passwd.encode('utf-8')).hexdigest()

import hashlib, random

# 初始化空字典,存储用户信息
db = {}
def register(username, password):
    """新用户注册"""
    db[username] = get_md5(username + password + 'the-salt')

def get_md5(info):
    """返回info摘要值"""
    return hashlib.md5(info.encode('utf-8')).hexdigest()

class User(object):
    """用户类"""
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        # rewrite digest
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice8888'),
}


def login(username, password):
    """用户登录或注册"""
    # 对用户实例化,初始化其属性
    user = db[username]
    # 取数据库中加盐后的密码摘要值与当前输入的密码进行加盐后对比，返回布尔值
    return user.password == get_md5(password + user.salt)

# 断言测试
# assert后的表达式值为True,不做任何处理
assert login('michael', '123456')

# assert后表达式值为False,输出错误信息，并抛出AssertionError
assert login('michael', '123ww456'), 'the user not login, please login in...'
