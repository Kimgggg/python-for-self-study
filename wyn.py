# -*- coding: utf-8 -*-
# encoding: utf-8
#!/usr/bin/env python
# still running on Python 2.7
import os
import sys
import shutil
import hashlib

fileNameList_svn = []
fileNameList_local = []
path_svn = "/data/work/svn/数据表/数值开发/"
path_localData = "/Users/playcrab/Documents/kof_debug_excel/"
path_diff = "/Users/playcrab/Documents/debug_diff/"
dict_svn = {}
dict_local = {}
scaler = 0

shutil.rmtree(path_diff)
os.mkdir(path_diff)

def svn_update(svn_path):
	print "正在更新svn"
	current_Path = os.getcwd()
	os.chdir(svn_path)
	os.system("svn update")
	os.chdir(current_Path)

def getHashCode(filename, path, dict_name):
	with open(path + filename, 'rb') as f:
		sha1obj = hashlib.sha1()
		sha1obj.update(f.read())
		hash = sha1obj.hexdigest()
		dict_name[filename] = hash

def copyFile(svn_path, filename, targetPath):
	os.system("cp " + svn_path + filename + " " + targetPath)
	print "正在往" + targetPath + "复制" + filename

svn_update(path_svn)
fileNameList_svn = os.listdir(path_svn)
fileNameList_local = os.listdir(path_localData)

for filename_svn in fileNameList_svn:
	getHashCode(filename_svn, path_svn, dict_svn)

for filename_local in fileNameList_local:
	getHashCode(filename_local, path_localData, dict_local)

for key in dict_svn:
	for key_data in dict_local:
		if key == key_data:
			if dict_svn[key] == dict_local[key_data]:
				pass
			else:
				copyFile(path_svn, key, path_diff)
				scaler += 1
		elif key not in dict_local:
			copyFile(path_svn, key, path_diff)
			scaler += 1
		else:
			pass

shutil.rmtree(path_localData)
shutil.copytree(path_svn,path_localData)
if scaler != 0:
	# print "先不执行脚本>>>>>>>>>>>>>>>>>>>>>>>>>"
	execfile("diff_inspect_to_excel_debug.py")
else:
	pass


