#!/usr/bin/env python
#coding: utf-8
# from __future__ import unicode_literals
import os
import svn.local
import re
import pwd_config
import csv_operation
import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')

'''
写死version_time，csv_pwd，row，col
用 -> a.txt 可以在当前目录下到出文本文件，方便查询
如:
python svn_spy.py -> a.txt
'''

current_path = os.getcwd()
os.chdir(pwd_config.War_CheckList_CSV_Source)
os.popen("svn cleanup")
os.popen("svn update")

# version_time = raw_input("version:\n")
version_time = "500"
svn_version = os.popen('svn log -l ' + version_time)
svn_version_list = svn_version.read()
find_version = re.findall(r'[0-9][0-9][0-9][0-9][0-9]',svn_version_list) # find_version =re.findall(r"r(\d\d\d\d\d)",svn_version_list)
find_version.sort()

# csv_pwd = raw_input("csv:\n")
# row = input("hang:\n")
# col = input("lie:\n")
csv_pwd = 'E:\war\svn\configCsv\csv\lang_3.csv'
row = 840
col = 1
util = ""
for x in find_version:
	os.popen("svn update -r " + str(x))
	# tempd = csv_operation.get_csvValue(csv_pwd,row,col)
	for line in open('E:\war\svn\configCsv\csv\lang_3.csv'):  
		if 'HEROSPECIALDES_505034' in line:
			print line
			print str(x)
		else:
			pass
	# util = tempd
	# print str(x)
	# print util


print "执行完毕"
os.chdir(current_path)
