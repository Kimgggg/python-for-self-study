# encoding: utf-8
#!/usr/bin/env python
import os
import shutil
import hashlib
import pwd_config

# fileNameList_svn = []
# fileNameList_local = []
path_svn = pwd_config.svn_ReleaseData
path_localData = pwd_config.svn_release_copy
path_diff = pwd_config.release_Diff
dict_svn = {}
dict_local = {}
scaler = 0

shutil.rmtree(path_diff)
os.mkdir(path_diff)

def svn_update(svn_path):
	print "正在更新Release"
	current_Path = os.getcwd()
	os.chdir(svn_path)
	os.system("svn update")
	os.chdir(current_Path)

def getHashCode(filename, path, dict_name):
	with open(path + filename, 'rb') as f:
		sha1obj = hashlib.sha1()
		sha1obj.update(f.read())
		file_hash = sha1obj.hexdigest()
		dict_name[filename] = file_hash

def copyFile(svn_path, filename, targetpath):
	os.system("cp " + svn_path + filename + " " + targetpath)
	print "正在往" + targetpath + "复制" + filename

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
	execfile("release_diff_inspect_to_excel.py")
else:
	print "release暂时没有更新"
