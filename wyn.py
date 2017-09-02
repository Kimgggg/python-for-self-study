#!/usr/bin/env python
#coding: utf-8

from __future__ import unicode_literals
import os
import pwd_config
import svn.local
import svn


os.chdir(pwd_config.War_svn)
svn_text = svn.local.LocalClient("E:\war\svn\configCsv\csv")
svn_info = svn_text.info()
# print svn_info
svn_version = svn_info["commit_revision"]
last_changed_author = svn_info["commit_author"]
last_time = svn_info["commit_date"]

print last_time

a = str(last_time).split(' ')[0] + " " + str(last_time).split(' ')[1]
print a
print type(str(a))