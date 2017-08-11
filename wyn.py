# -*- coding: utf-8 -*-
# encoding: utf-8
#!/usr/bin/env python
# still running on Python 2.7
import os
import sys
import shutil
import hashlib
# os.chdir("/data/work/pctools/")

# execfile('/data/work/pctools/tool.py')





fileNameList = []
fileNameList_data = []
path_svn = "/data/work/svn/数据表/数值开发/"
path_localData = "/Users/playcrab/Documents/kof_debug_excel/"
path_diff = "/Users/playcrab/Documents/debug_diff/"
dict_one = {}
dict_data = {}
count_a = 0

shutil.rmtree(path_diff)
os.mkdir(path_diff)

def svn_update(svn_path):
	current_Path = os.getcwd()
	os.chdir(svn_path)
	os.system("svn update")
	os.chdir(current_Path)


def getHash(filename, path, dict_name):
	with open(path + filename, 'rb') as f:
		sha1obj = hashlib.sha1()
		sha1obj.update(f.read())
		hash = sha1obj.hexdigest()
		# print filename + "的hash   是   " + hash
		# list_name.append(hash)
		dict_name[filename] = hash

svn_update(path_svn)
fileNameList = os.listdir(path_svn)
fileNameList_data = os.listdir(path_localData)

for x in fileNameList:
	getHash(x, path_svn, dict_one)

for y in fileNameList_data:
	getHash(y, path_localData, dict_data)

for key in dict_one:
	for key_data in dict_data:
		if key == key_data:
			#print "文件名一致"
			if dict_one[key] == dict_data[key_data]:
				print dict_one[key],"和",dict_data[key_data],"hash一样"
			else:
				print key," need going copy"
				os.system("cp " + path_svn + key + " " + path_diff)
				count_a = count_a + 1
				print ">>>>>>>>>>>>>>>",count_a 
		elif key not in dict_data:
			os.system("cp " + path_svn + key + " " + path_diff)
			count_a = count_a + 1
			print ">>>>>>>>>>>>>>>",count_a 
		else:
			pass

shutil.rmtree(path_localData)
shutil.copytree(path_svn,path_localData)
if count_a != 0:
	os.system("python inspect_to_excel_debug.py")
else:
	pass




# for key in dict_one:
# 	print key, '>>>>>>>>>>>' , dict_one[key]

# for key in dict_data:
# 	print key, "<<<<<<<<<<<", dict_data[key]

print len(dict_one),">>>>>>>",len(dict_data)

# print fileNameList.index("WorldBossEnemy.xlsx")

# print fileNameList[fileNameList.index("WorldBossEnemy.xlsx")]

# for name in fileNameList:
# 	print fileNameList[fileNameList.index(name)] + "的下标是: " + str(fileNameList.index(name))

