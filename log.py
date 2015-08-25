# testone.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

import functools



def log(text):
    if callable(text) == True:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print 'begin call: ' + text.__name__
            text(*args, **kw)
            print 'end call: ' + text.__name__
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'begin call: ' + text
                func(*args, **kw)
                print 'end call: ' + text
            return wrapper
        return decorator

@log
def  now1():
    print 'doing1...'

@log('text')
def now2():
    print 'doing2...'

print	now1()
print	now2()