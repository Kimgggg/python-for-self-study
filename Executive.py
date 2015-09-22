# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

from types import MethodType
import sys
import SetDef
import SetClass
import Image
import types
import itertools

# key = raw_input('是否要查询斐波那契数列？按y/n查询，其他键退出\n')
# if ord(key) == 121:
# 	SetDef.Fib(key)
# else:
# 	raw_input("Press any key to Exit: ")
#未调通

def cobmo2ls(ls1,ls2,concat):
	for i in range(0,len(ls1)):
		for j in range(0,len(ls2)):
			yield concat(ls1[i],ls2[j])

ls1 = ['1','2','3','4','5']
ls2 = ['a','b','c','d']

def concatStr(a,b):
	return a+b
for item in cobmo2ls(ls1,ls2,concatStr):
	print item