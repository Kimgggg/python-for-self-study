# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

from sys import argv

script ,filename = argv

print "we're going to erase %r." %filename
print "if you don't want that,hit CTRL-C(^C)."
print "if you do want that, hit return"

raw_input("?")
print "opening the file..."
target = open(filename,'w+')#打开文件赋值给target,w也会清空，（w,r,a or w+ ==）

#print "truncating the file. goodbye"
#target.truncate() #清空文件

print "now i'm going to ask you for three lines"

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "i'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "and finally, we close it."
target.close()#关闭保存