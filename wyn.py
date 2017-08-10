# -*- coding: utf-8 -*-
# encoding: utf-8
#!/usr/bin/env python
# still running on Python 2.7
import os
import sys
import hashlib
# os.chdir("/data/work/pctools/")

# execfile('/data/work/pctools/tool.py')

hashList = []
hashList_data = []
fileNameList = []
fileNameList_data = []
path_one = "/data/work/svn/数据表/数值开发/"
path_data = "/Users/playcrab/Documents/kof_debug_excel/"
dict_one = {}
dict_data = {}

def getHash(filename, path, list_name,dict_name):
	with open(path + filename, 'rb') as f:
		sha1obj = hashlib.sha1()
		sha1obj.update(f.read())
		hash = sha1obj.hexdigest()
		# print filename + "的hash   是   " + hash
		list_name.append(hash)
		dict_name[filename] = hash



fileNameList = os.listdir(path_one)
fileNameList_data = os.listdir(path_data)


for x in fileNameList:
	getHash(x, path_one, hashList, dict_one)

for y in fileNameList_data:
	getHash(y, path_data, hashList_data, dict_data)

for key in dict_one:
	print key, '>>>>>>>>>>>' , dict_one[key]
# print fileNameList

# print "WorldBossEnemy.xlsx" in fileNameList

# print fileNameList.index("WorldBossEnemy.xlsx")

# print fileNameList[fileNameList.index("WorldBossEnemy.xlsx")]

# for name in fileNameList:
# 	print fileNameList[fileNameList.index(name)] + "的下标是: " + str(fileNameList.index(name))

# print hashList
# print fileNameList
