#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import pwd_config

SVN_PWD_1 = pwd_config.svn_DebugData
SVN_PWD_2 = pwd_config.svn_ReleaseData
FILE_PWD_1 = pwd_config.debugData_git
FILE_PWD_2 = pwd_config.releaseData_git

print "当前SVN目录为:\n" + SVN_PWD_1 + "\n" + SVN_PWD_2
print "当前本地git目录为:\n" + FILE_PWD_1 + "\n" + FILE_PWD_2
print ">>>>是否需要改变<<<<"

select = input("1.修改\n2.不变\n")
if select == 1:
	pwd = os.getcwd()
	os.system('open ' + pwd + "/testa.py")
	print '正在退出'
	sys.exit()

print 'test'




	


