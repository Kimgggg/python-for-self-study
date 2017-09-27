#!/usr/bin/env python
# encoding: utf-8


import sys
import os
import svn.local
import re
import shutil


csv_develop = "E:\war\svn\configCsv\csv"
csv_preRelease = "E:\war\svn\configCsv_test\csv"
csv_Release = "E:\war\svn\configCsv_walle_china\csv"
csv_compare = "D:\csv_compare"

# current_path = os.getcwd()
# os.chdir("E:\war\svn\configCsv\csv")

# svn_version = os.popen('svn log -l 10')
# svn_version_list = svn_version.read()
# # print "<<<<<<<<>>>>>>>>>>" + svn_version_list + ">>>>>>>>>>>>>>>>>>>>>>"
# find_version = re.findall(r'[0-9][0-9][0-9][0-9][0-9]',svn_version_list) # find_version =re.findall(r"r(\d\d\d\d\d)",svn_version_list)
# find_version.sort()

# for x in find_version:
# 	os.system("svn update -r " + str(x))
# 	os.system("git st")
# 	os.system("git add . & git ci -m '" + str(x) + "'")

# os.system("svn update")
# os.chdir(current_path)

def del_files(path, filetype):
	#传入路径与需要删除的文件类型“.csv”
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(filetype):
                os.remove(os.path.join(root, name))
  	print ("Delete File: " + os.path.join(root, name))


del_files(csv_compare, ".csv")
os.system("xcopy " + csv_preRelease + " " + csv_compare + " /Y")
os.system("git add . & git ci -m 'test'")
del_files(csv_compare, ".csv")
os.system("xcopy " + csv_develop + " " + csv_compare + " /Y")
os.system("git add . & git ci -m 'test2'")


