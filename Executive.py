# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

from collections import defaultdict, OrdereDict
from types import MethodType
import sys
import SetDef
import SetClass
import Image
import types
import re
import time, threading
import random, Queue

# key = raw_input('是否要查询斐波那契数列？按y/n查询，其他键退出\n')
# if ord(key) == 121:
# 	SetDef.Fib(key)
# else:
# 	raw_input("Press any key to Exit: ")
#未调通


class LastUpdatedOrderedDict(OrdereDict):

	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity

	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last = False)
			print 'remove', last
		if containsKey:
			del self[key]
			print 'set:', (key, value)
		else:
			print 'add:', (key, value)
		OrdereDict.__setitem__(self, key, value)
		








