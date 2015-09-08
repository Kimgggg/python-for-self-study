# testone.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

from collections import Iterable
from types import MethodType
import SetDef
import Classtest
import os
import Image
import types


s = Classtest.Student()
s.name = raw_input('请输入姓名: \n')
#print s.name

##def set_age(self, age):
##    self.age = age


SetDef.set_age = MethodType(SetDef.set_age, s, Classtest.Student)
SetDef.set_age(input('shuru nianling:'))

print s.age,s.name

s2 = Classtest.Student()
s2.set_age(input('操你大爷到底通不通'))

print s2.age