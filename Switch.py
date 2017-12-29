#!/usr/bin/env python
#coding: utf-8

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args: 
            self.fall = True
            return True
        else:
            return False



# while True:
# 	v = raw_input("please test:\n")
# 	for case in switch(v):
# 	    if case('1'):
# 	        print 1
# 	        break
# 	    if case('2'):
# 	        print 2
# 	        break
# 	    if case('3'):
# 	        print 3
# 	        break
# 	    if case('4'):
# 	        print 4
# 	        break
# 	    if case(): # 默认
# 	        print "something else!"