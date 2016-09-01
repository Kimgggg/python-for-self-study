# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

from sys import argv
from os.path import exists
import json

script, fileName = argv
testList = []
testList2 = []
line = 0


f = open(fileName, 'r')
testList =  f.read()
line = fileName.readline()
if line != 0:
	print line
f.close
#print testList




#for x in range(0,len(testList)):
#	for y in testList:
#		if y == "\"":
#			testList2.append(testList[x + 1])
#

#Const_File_Format=["json","txt"]  
#def WriteXXLog(tarname,logfile_read,logfile_apend):  
#    print tarname
#    print logfile_read
#    print logfile_apend
#    file_object_read = open(logfile_read, 'r')
#    file_object_save = None
#    text = file_object_read.readlines()
#    text = ''.join(text)
#    text = text.replace('"bd_src": 1,', '"bd_src": 770,')
#    file_object_save = open(logfile_apend, 'w') 
#    file_object_save.write(text)
#    file_object_read.close()  
#    file_object_save.close()  