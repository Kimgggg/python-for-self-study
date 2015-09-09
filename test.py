# test.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

#print '200+100=',300  #显示表达式与显示值
#print '请输入姓名' #显示字符串
#name = raw_input('请输入您的姓名\n')  #调用输入函数
#print 'hello',name  #显示字符串+变量

#classmates = ['吴祎楠','左玢']

#d = {'wuyinan':100,'zuobin':99,'tutu':98}



#print(d[raw_input('请输入要查找的人名：\n')]) 


"""
f = open('/Users/wuyinan/Documents/AppleScript教程.pdf','r')
a = raw_input('请输入选择\n')
 f = open('/Users/wuyinan/Documents/123.txt', 'r')
if a == 1:
	#open('/Users/wuyinan/Documents/AppleScript教程.pdf','r')
	#print f.read('/Users/wuyinan/Documents/AppleScript教程.pdf')
	#with open('/Users/wuyinan/Documents/AppleScript教程.pdf', 'r') as f:
    #print f.read()
    try:
    f = open('/Users/wuyinan/Documents/123.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()
else:
	print '不读取'
"""


def add_end(L = None):
	if L is None:
		L = []
	L.append('end')
	return L

wufeifei = [1,2,3]


print add_end(wufeifei)

wufeifei = ['x','y','z']

print add_end(wufeifei)

print add_end()

print add_end()

L = []
n = 1
ff = 0
sum = 0

while n <= 100:
	L.append(n)
	n = n + 1

print L

'''
x = L[ff]

while ff <= 99:
	sum = sum + x
	ff  = ff + 1
	x = x + 1

print sum
'''







