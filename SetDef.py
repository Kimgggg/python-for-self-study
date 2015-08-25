# py.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import types
import functools
import log

def int2(x,base = 2):
	return int(x,base)

def int8(x,base = 8):
	return int(x,base)

def int10(x,base = 10):
	return int(x,base)

def int16(x,base = 16):
	return int(x,base)

#def fact(n):
#	if n == 1:
#		return 1
#	return n * fact(n - 1)

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def log_text(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

def log(fn):
    def wrapper():
        print "begin call, %s" % fn.__name__
        fn()
        print "end call, %s" % fn.__name__
    return wrapper

@log
def now():
	print 'today is' 



