# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

import	itertools

x = [1,2,3,4]
y = 
print	list(itertools.permutations(x,2))
'''
重复排列，显示全部
'''

y = ['a','b','c','d']
print	tuple(itertools.combinations(y,x))
'''
去重
'''

'''
a = [1,2,3,4]
b = ['a','b','c','d']

a.extend(b)
print a
list相加
'''

#Permutations_and_combinations
class Permutations(object):
	def __init__(self):
		self.List_a = []
		self.List_b = []

	def Permutations(a, b):
		self.List_a = a
		self.List_b = b

	def len_list(slef):
		len_list_a = len(self.List_a)
		len_list_b = len(self.List_b)

						

	def Permutations_sum(self):
		self.List_a.extend(self.List_b)
		return self.List_a

	def len():
		pass




		

		
	




		

	

		