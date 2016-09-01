# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

a = ["我方","jinlei","sunshuang","mayongbin"]
b = ["技能覆盖范围大于消除覆盖范围","技能覆盖范围小于消除范围","可消除敌方消除球",""]
#c = ["sb","2b","dsb"]

for x in a:
	for y in b:
		#for z in c:
			if (x != y): #and (x != z) and (y != z):
				print	x,y#,z
			else:
				print "error"
				break

				
