#!/usr/bin/env python
#coding: utf-8

from __future__ import unicode_literals
import os
import pwd_config
import svn.local
import svn


os.chdir(pwd_config.War_svn)
os.system("svn cleanup")
os.system("svn update")
svn_text = svn.local.LocalClient(pwd_config.War_CheckList_CSV_Source)
svn_info = svn_text.info()
svn_version = svn_info["commit_revision"]
last_changed_author = svn_info["commit_author"]
last_time = svn_info["commit_date"]
last_time_message = str(last_time).split(' ')[0] + " " + str(last_time).split(' ')[1]
os.chdir(pwd_config.War_CheckList_CSV_Target)
os.system("xcopy " + pwd_config.War_CheckList_CSV_Source + " " +  pwd_config.War_CheckList_CSV_Target + " /Y" )
os.system('git add . && git commit -m "svn v.' + str(svn_version) + "    commit_author  : " + str(last_changed_author) + "    modify by : " + str(last_time) + '"')
os.chdir(pwd_config.python_Script_Windows)
