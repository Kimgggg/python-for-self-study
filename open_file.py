#!/usr/bin/env python
# encoding: utf-8

import os

print "选择需要打开的文件：\n"
print '''
1. devConfig.lua   修改客户端默认服务器地址
2.LoginFacade.lua  修改客户端登录方式  快捷复制“LoginFacade:requestServerInfoFromGlobal”
'''

while True:
	press = input("请输入选择:\n")
	if press == 1:
		os.system("open /data/work/koflua/src/dev/devConfig.lua ")
	elif press == 2:
		os.system("open /data/work/koflua/src/kof/core/controller/login/LoginFacade.lua")
	elif press == "q":
		os.exit()



# if press == 1:
# 	os.system("open /data/work/koflua/src/dev/devConfig.lua ")
# elif press == 2:
# 	os.system("open /data/work/koflua/src/kof/core/controller/login/LoginFacade.lua")


	
# os.system("open /data/work/koflua/src/dev/devConfig.lua ")

# os.system("open /data/work/koflua/src/kof/core/controller/login/LoginFacade.lua")