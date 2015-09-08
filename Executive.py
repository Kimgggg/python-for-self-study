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

def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s, Classtest.Student)
s.set_age(input('shuru nianling:'))

print s.age,s.name