# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

from collections import Iterable
from types import MethodType
import SetDef
import SetClass
import Image
import types
import re
import time, threading

# key = raw_input('是否要查询斐波那契数列？按y/n查询，其他键退出\n')
# if ord(key) == 121:
# 	SetDef.Fib(key)
# else:
# 	raw_input("Press any key to Exit: ")
#未调通

Bank = 0
lock = threading.Lock()

def change_it(n):
	global Bank
	Bank = Bank + n
	Bank = Bank - n

def run_thread(n):
	for i in range(100000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()

t1 = threading.Thread(target = run_thread, args = (5, ))
t2 = threading.Thread(target = run_thread, args = (8, ))
t1.start()
t2.start()
t1.join()
t2.join()

print Bank










