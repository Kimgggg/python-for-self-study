# Time.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import datetime, time

now = time.strftime('%Y-%m-%d %H:%M:%S')
print now

d1 = now - datetime.timedelta(hours = 1)
print d1.strftime('%Y-%m-%d %H:%S:%M')

#bug未修复