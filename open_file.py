#!/usr/bin/env python
# encoding: utf-8

import os
import webbrowser

while True:
	print "选择需要打开的文件：\n"
	print '''
1. devConfig.lua   修改客户端默认服务器地址
2.LoginFacade.lua  修改客户端登录方式  快捷复制“LoginFacade:requestServerInfoFromGlobal”
		'''
	press = raw_input("请输入选择:\n")
	if press == "1":
		os.system("open /data/work/koflua/src/dev/devConfig.lua ")
	elif press == "2":
		os.system("open /data/work/koflua/src/kof/core/controller/login/LoginFacade.lua")
	elif press == "3":
		webbrowser.open("www.baidu.com")
		#os.system("open /Applications/Safari.app http://www.baidu.com")
	elif press == "q":
		os.exit()



# if press == 1:
# 	os.system("open /data/work/koflua/src/dev/devConfig.lua ")
# elif press == 2:
# 	os.system("open /data/work/koflua/src/kof/core/controller/login/LoginFacade.lua")


	
# os.system("open /data/work/koflua/src/dev/devConfig.lua ")

# os.system("open /data/work/koflua/src/kof/core/controller/login/LoginFacade.lua")