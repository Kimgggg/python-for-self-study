# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

from collections import deque
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

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

print q

#append 队尾
#appendleft 队伍左侧（头）
#删除同理














