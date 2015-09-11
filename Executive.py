# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

from collections import Iterable
from types import MethodType
import SetDef
import UsersClass
import SetClass
import os
import Image
import types

# key = raw_input('是否要查询斐波那契数列？按y/n查询，其他键退出\n')
# if ord(key) == 121:
# 	SetDef.Fib_query(key)
# else:
# 	raw_input("Press any key to Exit: ")
# #未调通

u = UsersClass.user(id = input('请输入注册ID:\n'), name = raw_input('请输入姓名:\n'), email = raw_input('请输入email:\n'), password = raw_input('请输入密码: \n'))

u.save()


