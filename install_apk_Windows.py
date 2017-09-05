#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import os
import sys
import time
import pwd_config

WORD = "apk"
PATH = pwd_config.dowloads_Windows
APK_NAME = []
NUM = 0

dirdir = os.listdir(PATH)

for find_apk in dirdir:
    if find_apk.split(".")[-1] == WORD:
        APK_NAME.append(find_apk)
    else:
        pass


if APK_NAME == []:
    print "not found apk"
    sys.exit()

for y in APK_NAME:
    os.path.getctime(PATH + "/" + y)
    timeTuple = time.localtime(os.path.getctime(PATH + "/" + y))
    CreateTime = time.strftime("%Y-%m-%d %H:%M:%S", timeTuple)
    NUM = NUM + 1
    print str(NUM) + ". " + y + "    Create time is : " + CreateTime
install_apk = input("please  input apk number  : \n")
os.system("adb install -r " + PATH + "/" + APK_NAME[install_apk - 1])
