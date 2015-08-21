# testone.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

#import SetDef
from collections import Iterable
import os

#for key,value in SetDef.d.iteritems():
#	print key,value
import math
def is_ss(s):
    if s==1:
        return False
    for i in range(2,int(sqrt(s)+1)):
        if s%i==0:
            return False
    return True

print(filter(is_ss,range(1,100)))