#!/usr/bin/env python
# encoding: utf-8
import tarfile
import os

def untar(fname, dirs):#文件名,解压目标路径
    t = tarfile.open(fname)
    print '打开文件'
    t.extractall(path = dirs)
    print '正在往 /data/work/KOF/kof/svn/Resources/auto/config 解压'

def del_tar():
    os.remove("/Users/playcrab/Downloads/all.tar")


if __name__ == "__main__":
    untar("/Users/playcrab/Downloads/all.tar", "/data/work/KOF/kof/svn/Resources/auto/config")
    del_tar()
    print '解压完毕,已删除源文件'