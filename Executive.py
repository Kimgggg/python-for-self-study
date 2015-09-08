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
s2 = Classtest.Student()
s.name = raw_input('请输入姓名: \n')
#print s.name

##def set_age(self, age):
##    self.age = age


SetDef.set_age = MethodType(SetDef.set_age, s, Classtest.Student) ''' 把setdef的一个函数单独给S作为属性'''
SetDef.set_age(input('shuru nianling:'))

print s.age,s.name

Classtest.Student.set_score = MethodType(SetDef.set_score, None, Classtest.Student)  '''全部实例绑定方法：把setdef的一个函数增加给classtest作为实例方法'''
s.set_score(100)
s2.set_score(99)
print s.score,s2.score

#s2 = Classtest.Student()
s2.set_age(input('操你大爷到底通不通')) ''' 看见这话就证明单独对某一实例+方法和给全部实例+方法调通了'''

print s2.age