# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

import sys
import SetDef
import SetClass
import Image
import types
import itertools
import hashlib
import urllib2
import HTMLParser
import re
import socket
# key = raw_input('是否要查询斐波那契数列？按y/n查询，其他键退出\n')
# if ord(key) == 121:
# 	SetDef.Fib(key)
# else:
# 	raw_input("Press any key to Exit: ")
# 未调通

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.sina.com', 80))
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

s.close()

header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)





      
