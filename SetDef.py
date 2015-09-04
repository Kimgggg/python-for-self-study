# py.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import types
import functools
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
"""




class Student(object):
    """test"""
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score

class Animal(object):
    """Base class and Super class test"""
    def run(self):
        print 'Animal is running ... '

class Dog(Animal):
    """docstring for Dog"""
    pass

class Cat(Animal):
    """docstring for ClassName"""
    pass
        
        
        


        



