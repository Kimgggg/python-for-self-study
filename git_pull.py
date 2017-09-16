#!/usr/bin/env python
# encoding: utf-8

import os
import pwd_config

PWD = [pwd_config.KOF_C, pwd_config.KOF_LUA, pwd_config.KOF_TOOL]
path = os.getcwd()
for git_pwd in PWD:
    print "开始更新" + git_pwd
    os.chdir(git_pwd)
    os.system("git pull")
    print git_pwd + "更新完毕"
os.chdir(path)