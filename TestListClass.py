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

	def Permutations(a, b, self = None):
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

'''
黑哥示例
'''
def cobmo2ls(ls1,ls2,concat):
	for i in range(0,len(ls1)):
		for j in range(0,len(ls2)):
			yield concat(ls1[i],ls2[j])

ls1 = ['我','你','他']
ls2 = ['和','不',' 能']

def concatStr(a,b):
	return a + b
for item in cobmo2ls(ls1,ls2,concatStr):
	print item

# ls1 = []
# Continue_ls1 = 0
# while Continue_ls1 == 0:
# 	ls1.append(raw_input('请继续输入条件步骤:\n'))
# 	Continue_ls1 = input('是否继续输入？继续输入请按数字“0”,按其他“数字”键退出\n')

# print base64.b64encode(ls1)


		

		
	




		

	

		