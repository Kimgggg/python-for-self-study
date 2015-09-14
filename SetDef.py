# py.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import types
import functools
import Classtest
import SetClass

#import log

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

"""
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

 //暂时调不通   
"""

def Fib(n):
    for n in SetClass.Fib():
        pass
    f = SetClass.Fib()
    Continue_query = 3 #初始化＝3
    while Continue_query == 3:
        a = input('查询斐波那契数列\n单独查询按“1”，多个查询按“2”: \n')
        if a != 1 and a != 2:
            print 'Error'
        else:
            if a == 2:
                Number_Y = input('需要从第几个查询？\n') - 1
                if Number_Y < 0:
                    print 'Error in Y<0'
                Number_Z = input('需要查询到第几个?\n')  
                if Number_Z < Number_Y:
                    print 'Error in Z<Y'
                print '从第', Number_Y + 1, '个到 第', Number_Z, '个的斐波那契数是:\n',  f[Number_Y:Number_Z]
            else:
                Number_X = input('要查询第几个斐波那契数？：\n')  - 1
                if Number_X < 0:
                    print 'Error'
                else:
                    print '第',Number_X + 1,'个斐波那契数是:',f[Number_X]
        Continue_query = input('继续查询请按“3”\n')
        print 'bye～'
    else:   #bug
        print 'bye～'





        
        


        



