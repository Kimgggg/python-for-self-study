#!/usr/bin/env python
# encoding: utf-8

import os
import pwd_config

CURRENT_BRANCH = ""
path_all = os.getcwd()

def gitBranch_update(branch_name):
	os.chdir(pwd_config.KOF_LUA)
	os.system("git co .")
	os.system("git co " + str(branch_name))
	os.system("git pull")


os.chdir(pwd_config.KOF_LUA)
local_git_branch = os.popen('git branch')
git_branch = local_git_branch.read()
filter_branch =  git_branch.split("\n")

for k in filter_branch:
	if k == "  master":
		filter_branch.remove(k)

filter_branch.sort()

for x in filter_branch:
	mystring = "*"
	if mystring in x:
		x = x.replace("*"," ")
		CURRENT_BRANCH = x
		gitBranch_update(x)
		print x + "<<<<<<<<<<更新完毕"
	else:
		x = x.lstrip()
		gitBranch_update(x)
		print x + "<<<<<<<<<<更新完毕"

os.system("git co " + CURRENT_BRANCH)
os.chdir(pwd_config.python_Script)



