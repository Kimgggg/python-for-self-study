#!/usr/bin/env python
# encoding: utf-8
import sys

pathfile = sys.argv[1]
need_modify_argv = sys.argv[2]
target_source = sys.argv[3]

#将文件读取到内存中
with open(pathfile,"r") as f:
	lines = f.readlines() 
#写的方式打开文件
with open(pathfile,"w") as f_w:
	for line in lines:
		if need_modify_argv in line:
         #替换
			line = line.replace(need_modify_argv, target_source)
		f_w.write(line)