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

for c in itertools.chain('123','456'):
	print c