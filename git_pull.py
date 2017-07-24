#!/usr/bin/env python
# encoding: utf-8

import os

KOF_C = "/data/work/kof"
KOF_LUA = "/data/work/koflua"
KOF_TOOL = "/data/work/pctools"

PWD = [KOF_C,KOF_LUA,KOF_TOOL]
for git_pwd in PWD:
	print "开始更新" + git_pwd
	os.chdir(git_pwd)
	os.system("git pull")
	print git_pwd + "更新完毕"







