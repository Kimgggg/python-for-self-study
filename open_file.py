#!/usr/bin/env python
# encoding: utf-8

import os
import webbrowser

while True:
	print '''选择需要打开的文件：\n
1. devConfig.lua   修改客户端默认服务器地址
2.LoginFacade.lua  修改客户端登录方式  \n快捷复制“LoginFacade:requestServerInfoFromGlobal”
3.打包机2
4.打开数值开发文件夹
5.打开release文件夹
6.打包机6
7.gm后台
8.dev2 gm后台
9.订餐
10.开工套餐
11.tower
12.adb -r
13.解压tar
		'''
	press = raw_input("请输入选择:\n")
	if press == "1":
		os.system("open /data/work/koflua/src/dev/devConfig.lua ")
	elif press == "2":
		os.system("open /data/work/koflua/src/kof/core/controller/login/LoginFacade.lua")
	elif press == "3":
		# webbrowser.open("www.baidu.com") #有报错但不影响使用，需调试
		os.system("open /Applications/Safari.app http://deploy2.kof.playcrab-inc.com/walle/ui/")
	elif press == "4":
		os.system("open /data/work/svn/数据表/数值开发/")
	elif press == "5":
		os.system("open /data/work/svn/数据表/Release")
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
		os.chdir("/Users/playcrab/Documents/python-for-self-study")
		execfile("allbranch_pull.py")
		execfile("git_pull.py")
		execfile("wyn.py")
		execfile("inspect_to_excel_release.py")
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
	elif press == "q":
		os.exit()
	
