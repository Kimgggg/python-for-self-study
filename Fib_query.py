# testone.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7
from pudb import set_trace; set_trace()
import SetClass


for n in SetClass.Fib():
	pass

f = SetClass.Fib()
Continue_query = 3 #初始化＝3

while Continue_query == 3:
	a = input('查询斐波那契数列\n单独查询按“1”，多个查询按“2”: \n')
	if a != 1 and a != 2:
		print 'Error'
	else:
		if a == 2:
			Number_Y = input('需要从第几个查询？\n') - 1
			if Number_Y < 0:
				print 'Error in Y<0'
			Number_Z = input('需要查询到第几个?\n')
			if Number_Z < Number_Y:
				print 'Error in Z<Y'
			print '从第', Number_Y + 1, '个到 第', Number_Z, '个的斐波那契数是:\n',  f[Number_Y:Number_Z]
		else:
			Number_X = input('要查询第几个斐波那契数？：\n')  - 1
			if Number_X < 0:
				print 'Error'
			else:
				print '第',Number_X + 1,'个斐波那契数是:',f[Number_X]
	Continue_query = input('继续查询请按“3”\n')
print 'bye～'
