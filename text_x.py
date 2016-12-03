# test.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os

#f = open('/Users/wuyinan/Desktop/test.txt', 'w')


f = open('/Users/wuyinan/Desktop/test.txt', 'w')
f.write('fuck off!too!\n')
f.close()
f = open('/Users/wuyinan/Desktop/test.txt', 'r')
print f.read()
f.close()

print 'next to os'

print os.name
print '==============================='
print os.uname()
print '==============================='
print os.environ