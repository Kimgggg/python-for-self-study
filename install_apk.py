#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import time

WORD = "apk"
PATH = "/Users/playcrab/Downloads"
APK_NAME = []
NUM = 0

dirdir = os.listdir(PATH)

for find_apk in dirdir:
    if find_apk.split(".")[-1] == WORD:
        APK_NAME.append(find_apk)
    else:
        pass

if APK_NAME == []:
    print "没有找到安装包"
    sys.exit()

for y in APK_NAME:
    CreateTime = ""
    os.path.getctime(PATH + "/" + y)
    timeTuple = time.localtime(os.path.getctime(PATH + "/" + y))
    CreateTime = time.strftime("%Y-%m-%d %H:%M:%S", timeTuple)
    NUM = NUM + 1
    print str(NUM) + ". " + y + "    创建于" + CreateTime
install_apk = input("请输入要安装的apk序号：\n")
os.system("adb install -r " + PATH + "/" + APK_NAME[install_apk - 1])
