#!/usr/bin/env python
# encoding: utf-8

import os
import pwd_config

while True:
	print '''选择需要打开的文件:
1. devConfig.lua   修改客户端默认服务器地址
2.LoginFacade.lua  修改客户端登录方式  \n快捷复制“LoginFacade:requestServerInfoFromGlobal”
3.打包机2
4.打开数值开发文件夹
5.打开release文件夹
6.打包机6
7.gm后台
8.dev2 gm后台
9.订餐
10.上班套餐
11.tower
12.adb -r
13.解压tar
14.还原路径
		'''
	press = raw_input("请输入选择:\n")
	if press == "1":
		os.system("open /data/work/KOF/koflua/src/dev/devConfig.lua ")
	elif press == "2":
		os.system("open /data/work/KOF/koflua/src/kof/core/controller/login/LoginFacade.lua")
	elif press == "3":
		# webbrowser.open("www.baidu.com") #有报错但不影响使用，需调试
		os.system("open /Applications/Safari.app http://deploy2.kof.playcrab-inc.com/walle/ui/")
	elif press == "4":
		os.system("open " + pwd_config.svn_DebugData)
	elif press == "5":
		os.system("open " + pwd_config.svn_ReleaseData)
	elif press == "6":
		# webbrowser.open("www.baidu.com") #有报错但不影响使用，需调试
		os.system("open /Applications/Safari.app http://deploy6.kof.playcrab-inc.com/walle/ui/")
	elif press == "7":
		os.system("open /Applications/Safari.app http://deploy2.kof.playcrab-inc.com/gm/")
	elif press == "8":
		os.system("open /Applications/Safari.app http://172.16.110.87:10000/tool/index.php/players/showList/")
	elif press == "9":
		os.system("open /Applications/Safari.app https://ucenter.playcrab.com")
	elif press == "10":
		path = os.getcwd()
		os.chdir(pwd_config.python_Script)
		execfile("allbranch_pull.py")
		execfile("git_pull.py")
		execfile("debug_diff.py")
		execfile("release_diff.py")
		os.system("open /Applications/Safari.app http://deploy2.kof.playcrab-inc.com/gm/")
		os.system("open /Applications/Safari.app https://tower.im/teams/85798e163e1d430abf652b57a16b5ba2/projects/") 
		os.chdir(path)
		print "开工套餐done"
	elif press == "11":
		os.system("open /Applications/Safari.app https://tower.im/teams/85798e163e1d430abf652b57a16b5ba2/projects/") 
	elif press == "12":
		execfile("/Users/playcrab/Documents/python-for-self-study/install_apk.py")
	elif press == "13":
		execfile("AutoMoveAndRemove.py")
	elif press == "14":
		os.chdir(pwd_config.python_Script)
		print "已经已还原" + pwd_config.python_Script
	elif press == "15":
		print "下班套餐开发中"
	elif press == "16":
		print "自动下载对应版本的tar文件"
	elif press == "17":
		print "自动导dev2的lua表"
	elif press == "q":
		os.exit()
	else:
		print "输入错误"