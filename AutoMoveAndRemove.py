#!/usr/bin/env python
# encoding: utf-8
'''
输入指定tar,解压至/data/work/kof/svn/Resources/auto/config
/data/work/kof/svn/Resources/auto/config 为工程目录内需要的config
'''

import tarfile
import os
import sys

#filename = sys.argv[1]

# filename = raw_input("输入tar文件路径:\n")
# #filename = "Users/playcrab/Downloads/all.tar"
# # def getpwd():
# #     path = os.getcwd()
# #     return path
# # #获取当前目录

def untar(fname, dirs):#文件名,解压目标路径
    t = tarfile.open(fname)
    print '打开文件'
    t.extractall(path = dirs)
    print '正在往 /data/work/KOF/kof/svn/Resources/auto/config 解压' 
#解压tar文件

def del_tar():
    os.remove("/Users/playcrab/Downloads/all.tar")


if __name__ == "__main__":
    untar("/Users/playcrab/Downloads/all.tar", "/data/work/KOF/kof/svn/Resources/auto/config")
    del_tar()
    print '解压完毕,已删除源文件'



