# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

from sys import  argv

script, filename = argv
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()
a = ["guoxiang","jinlei","sunshuang","mayongbin"]
b = ["shi","bushi","kenengshi"]
c = ["sb","2b","dsb"]

for x in a:
	for y in b:
		#for z in c:
			if (x != y): #and (x != z) and (y != z):
				print	x,y#,z
			else:
				print "error"
				break
