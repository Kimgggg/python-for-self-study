#!/usr/bin/env python
# encoding: utf-8



from __future__ import unicode_literals
import os
import sys
import time
import pwd_config
import fuck_gbk

WORD = "apk"
APK_NAME = []
NUM = 0

dirdir = os.listdir(pwd_config.dowloads_Windows)
#文件夹内部不允许有中文名称的文件，否则会报错
for find_apk in dirdir:
    if find_apk.split(".")[-1] == WORD:
        APK_NAME.append(find_apk)
    else:
        pass


if APK_NAME == []:
    print "not found apk"
    sys.exit()

for y in APK_NAME:
    os.path.getctime(pwd_config.dowloads_Windows + "/" + y)
    timeTuple = time.localtime(os.path.getctime(pwd_config.dowloads_Windows + "/" + y))
    CreateTime = time.strftime("%Y-%m-%d %H:%M:%S", timeTuple)
    NUM = NUM + 1
    print str(NUM) + ". " + y + "    Create time is : " + CreateTime
install_apk = input("please  input apk number  : \n")
os.system("adb install -r " + pwd_config.dowloads_Windows + "/" + APK_NAME[install_apk - 1])
