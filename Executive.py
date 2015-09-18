# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

from collections import namedtuple
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

p = (1, 2)

Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(1, 2, 3)


print p.x
print p.y
print p.z

m2 = p.x * p.y * p.z
print m2
















