# Time.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import datetime

now = datetime.datetime.now()

d1 = now - datetime.timedelta(hours = 1)
print d1.strftime('%y-%m-%d %H:%S:%M')

d2 = now - datetime.timedelta(days = 1)
print d2.strftime('%Y-%m-%d %H:%S:%M') 

#bug未修复
