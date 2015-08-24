# testone.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

#import SetDef
from collections import Iterable
import os

#for key,value in SetDef.d.iteritems():
#	print key,value

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


a=1
b=2
c=3

print lazy_sum(a,b,c)

print lazy_sum()

f1 = lazy_sum(a,b,c)
f2 = lazy_sum(a,b,c)

print f1==f2

print f1
print f2

test github