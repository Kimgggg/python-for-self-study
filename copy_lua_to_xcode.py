#!/usr/bin/env python
# encoding: utf-8

import shutil
import os
import sys

'''
将已解压的Lua数据文件复制到工程目录下
'''

# source_path = sys.argv[1]
# target_path = sys.argv[2]
# print source_path
# print target_path

source_path = raw_input('输入导出的lua文件夹路径:\n')
while source_path[-1] == ' ':
	source_path = raw_input('路径末尾包含空格,需重新输入\n')
#target_path = raw_input('输入目标位置路径:\n')
target_path = '/data/work/kof/svn/Resources/auto/config'

if os.path.exists(target_path):
	print '目标路径文件已存在,开始删除文件夹...'
	shutil.rmtree(target_path)
	print '删除完成,开始复制文件'
	shutil.copytree(source_path, target_path)
	print '替换成功' 
else:
	print '目标位置不存在文件,直接复制'
	shutil.copytree(source_path, target_path) 
	print '文件复制移动成功'
 
