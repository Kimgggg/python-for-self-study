#!/usr/bin/env python
# encoding: utf-8


import sys
import os
import pprint
import svn.local
import re


current_path = os.getcwd()
os.chdir("E:\war\svn\configCsv\csv")

a = os.popen('svn log -l 10')
b = a.read()
print "<<<<<<<<>>>>>>>>>>" + b + ">>>>>>>>>>>>>>>>>>>>>>"
c = re.findall(r'[0-9][0-9][0-9][0-9][0-9]',b) # c =re.findall(r"r(\d\d\d\d\d)",b)
c.sort()

for x in c:
	os.system("svn update -r " + str(x))
	os.system("git status")
	os.system("git add . & git ci -m '" + str(x) + "'")

os.system("svn update")
