#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import os
import pwd_config

CURRENT_BRANCH = ""


def gitbranch_update(branch_name):
    os.chdir(pwd_config.War_script)
    os.system("git checkout .")
    os.system("git checkout " + str(branch_name))
    os.system("git pull")


os.chdir(pwd_config.War_script)
local_git_branch = os.popen('git branch')
git_branch = local_git_branch.read()
filter_branch = git_branch.split("\n")

# for k in filter_branch:
# 	if k == "  master":
# 		filter_branch.remove(k)

# filter_branch.sort()

for x in filter_branch:
    mystring = "*"
    if mystring in x:
        x = x.replace("*", " ")
        CURRENT_BRANCH = x
        gitbranch_update(x)
        print x + "<<<<<<<<<<更新完毕"
    else:
        x = x.lstrip()
        gitbranch_update(x)
        print x + "<<<<<<<<<<更新完毕"

os.system("git checkout " + CURRENT_BRANCH)
os.chdir(pwd_config.python_Script_Windows)
