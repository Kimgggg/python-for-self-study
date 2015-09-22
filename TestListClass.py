# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

import	itertools

x = [1,2,3,4,5,6]
print	list(itertools.permutations(x,2))
'''
重复排列，显示全部
'''

y = (1,2,3,4)
print	tuple(itertools.combinations(y,2))
'''
去重
'''
