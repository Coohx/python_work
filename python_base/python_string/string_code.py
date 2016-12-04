# -*- coding: utf-8 -*-
# string & code
# Python3 coding with Unicode, Supporting multiple Language.

# ord() 函数提取单个字符的整数表示(十进制)
a_unicode = ord('a')
print('a_unicode = %d' % a_unicode)
# %x 以十六进制格式化输出, 字符串外部的%后跟要输出的变量或常量，多于一个时用括号扩起来
print('a_unicode = 0x%x' % a_unicode)

Zhong = ord('中')
Wen = ord('文')
print('中_unicode =', Zhong)
# Unicode 编码中一个汉字两个字节
print('中_unicode = 0x%x' % Zhong )
print('文_unicode = 0x%x' % Wen )

# chr( )函数把编码转换为对应的字符
a = chr(97)
print('a = %s' % a)

Zhong = chr(20013)
print('中 = %s' % Zhong)

# \u 后直接跟十六进制编码, 单引号括起
ZhongWen = '\u4e2d\u6587'
print('中文 = %s' % ZhongWen)

# Python的字符串类型为str，内存中以Unicode表示(一个字符对应多个字节)
# encode()方法可以把str编码为指定的bytes(一个字符占一个字节)
# bytes类型的数据用带 b 前缀的单引号或双引号表示

# 纯英文可用 ASCII 编码
abc_bytes = 'abc'.encode('ascii')
print('abc_bytes = %s' % abc_bytes)

# utf-8 包含ASCII，建议使用utf-8
abc_bytes = 'abc'.encode('utf-8')
print('abc_bytes = %s' % abc_bytes)

# decode()方法可以把bytes类型的编码转换为str类型
abc_str = abc_bytes.decode('ascii') 
print('abc_str = %s' % abc_str)

abc_str = abc_bytes.decode('utf-8') 
print('abc_str = %s' % abc_str)

# 中文超出 ASCII 编码范围，需要使用 utf-8 编码，utf-8编码中一个中文字符占3个字节

ZhongWen_bytes = '中文'.encode('utf-8')
print('中文_bytes = %s' % ZhongWen_bytes)

ZhongWen_str = ZhongWen_bytes.decode('utf-8')
print('中文_str = %s' % ZhongWen_str)

# str类型编码时，len()函数计算字符串中字符的个数
abc_str_len = len(abc_str)
print('abc_str_len = %d' % abc_str_len)

ZhongWen_str_len = len(ZhongWen_str)
print('ZhongWen_str_len = %d' % ZhongWen_str_len)

# bytes类型时，len()函数计算字节数
abc_bytes_len = len(abc_bytes)
print('abc_bytes_len = %d' % abc_bytes_len)

ZhongWen_bytes_len = len(ZhongWen_bytes)
print('ZhongWen_bytes_len = %d' % ZhongWen_bytes_len)
