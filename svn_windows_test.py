#!/usr/bin/env python
#coding: utf-8

from __future__ import unicode_literals
import os
import webbrowser
import pwd_config
import svn.local
import svn


os.chdir(pwd_config.War_svn)
svn_text = svn.local.LocalClient("E:\war\svn\configCsv\csv")
svn_info = svn_text.info()
svn_version = svn_info["commit_revision"]
last_changed_author = svn_info["commit_author"]
os.system("svn update")
os.chdir("D:/config_git")
os.system("xcopy E:\war\svn\configCsv\csv D:\config_git /Y ")
os.system('git add . && git commit -m "svn v.' + str(svn_version) + ">>>>commit_author  ： " + str(last_changed_author) + '"')
