#!/usr/bin/env python
# encoding: utf-8


import sys
import os
import pprint
import svn.local
import re


# r = svn.local.LocalClient('/data/work/KOF/svn/数据表/数值开发')
# info = r.info()
# # pprint.pprint(info)
# # print type(info)
# # print info["commit_revision"]
# os.system('svn update')

os.chdir("/data/work/KOF/svn/数据表/数值开发")
a = os.popen('svn log -l 10')

b = a.read()
print "<<<<<<<<>>>>>>>>>>" + b + ">>>>>>>>>>>>>>>>>>>>>>"
c = re.findall(r"r(\d\d\d\d\d\d)",b)
c.sort()
print type(c)
print c
print len(c)

