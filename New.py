# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

a = ["guoxiang","jinlei","sunshuang","mayongbin"]
b = ["shi","bushi","kenengshi"]
c = ["sb","2b","dsb"]

for x in a:
	for y in b:
		for z in c:
			if (x != y) and (x != z) and (y != z):
				print	x,y,z
			else:
				print "error"
				break

				
