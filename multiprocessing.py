#multiprocessing.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os

print 'Process (%s) Start...' % os.getpid()
pid = os.fork()

if pid == 0:
 	print 'I am child Process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
	print 'I(%s) just created a child Process (%s) .' % (os.getpid(), pid)
