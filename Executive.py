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
import base64

# key = raw_input('是否要查询斐波那契数列？按y/n查询，其他键退出\n')
# if ord(key) == 121:
# 	SetDef.Fib(key)
# else:
# 	raw_input("Press any key to Exit: ")
# 未调通

def cobmo2ls(ls1,ls2,concat):
	for i in range(0,len(ls1)):
		for j in range(0,len(ls2)):
			yield concat(ls1[i],ls2[j])

ls1 = ['我','你','他']
ls2 = ['和','不',' 能']

def concatStr(a,b):
	return a+b
for item in cobmo2ls(ls1,ls2,concatStr):
	print item

# ls1 = []
# Continue_ls1 = 0
# while Continue_ls1 == 0:
# 	ls1.append(raw_input('请继续输入条件步骤:\n'))
# 	Continue_ls1 = input('是否继续输入？继续输入请按数字“0”,按其他“数字”键退出\n')

# print base64.b64encode(ls1)