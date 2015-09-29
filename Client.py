# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7


import hashlib
import urllib2
import HTMLParser
import re
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据:
    s.sendto(data, ('10.0.1.127', 9999))
    # 接收数据:
    print s.recv(1024)
s.close()