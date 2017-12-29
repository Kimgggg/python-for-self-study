#!/usr/bin/env python
#coding: utf-8

from __future__ import unicode_literals
import os

def del_files(path, filetype):
	for root, dirs, files in os.walk(path):
		for name in files:
			if name.endswith(filetype):
				os.remove(os.path.join(root, name))
		print ("Delete File: " + os.path.join(root, name))


def update_client_win():
	print "切换至client_win目录"
	os.chdir("E:\war\client_win")
	print "清空本地改动"
	os.system("svn cleanup")
	print "更新svn"
	os.system("svn update")
	print "切换至Resources目录"
	os.chdir("..\svn\Resources")
	print "删除.dll文件"
	del_files(os.getcwd(),".dll")
	print "删除.exe文件"
	del_files(os.getcwd(),".exe")
	print "从client复制war.exe"
	os.system("xcopy ..\..\client_win\war.exe " + os.getcwd() + " /Y")
	print "从client复制*.dll"
	os.system("xcopy ..\..\client_win\*.dll " + os.getcwd() + " /Y")
	print "切换至pctools文件夹"
	os.chdir("..\..\..\pctools")
	# print "执行tool.py脚本action-9"
	# os.system("python tool.py 9")
	print "执行tool.py脚本action-8"
	os.system("python tool.py 8 q")

def main():
	print "开始更新script目录"
	os.chdir("E:\war\svn\Resources\script")
	print "清空本地改动"
	os.system("git checkout .")
	print "删除本地多余文件"
	os.system("git clean -df")
	print "切换至develop分支"
	os.system("git checkout develop")
	print "更新develop分支"
	os.system("git pull")
	print "git 更新完毕"
	print "切换至svn目录"
	os.chdir("E:\war")
	print "清空本地改动"
	os.system("svn cleanup")
	print "更新svn"
	os.system("svn update")
	update_client_win()
	print "切换至client_win目录"
	os.chdir("E:\war\client_win")
	print "执行publish.py发布版本"
	os.system("python publish.py")

if __name__ == '__main__':
	main()
