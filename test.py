#test.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

import re
import math
import os
from collections import Iterable
from collections import Counter




def prime_numbers(s):
    if s==1:
        return False
    for i in range(2,int(math.sqrt(s)+1)):
        if s%i==0:
            return False
    return True

def letter_count(l):
	test = l
	print(dict(Counter(test)))

def cap_string(c):
	Caps = c.title()
	return Caps





Counts = raw_input('please input 2:\n')
Caps_Lock = raw_input('please input 3:\n')

print filter(prime_numbers,range(1,100))
print letter_count(Counts)
print cap_string(Caps_Lock)

