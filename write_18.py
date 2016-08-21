# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

def print_two(*args):
    arg1, arg2,arg3 = args
    print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2,arg3)

def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "i got nothin"

print_two("zeg", "shaw","aaa")
print_two_again("a","b")
print_one("first")
print_none()