#!/usr/bin/env python
# encoding: utf-8

import tarfile
import os
import sys
import string
import re

filename = raw_input("输入tar文件路径:\n")
print type(filename)



p = re.compile('\s+')
filename = re.sub(p,'',filename)
print "filename --%s--" % filename

if filename[-1] == ' ':
	print '有空格'
else:
	print '没空格'

print filename

'''
正则可以删除空格,rstrip不行
'''