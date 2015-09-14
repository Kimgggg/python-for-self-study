# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

import unittest
from mydict import Dict

class TestDict(unittest.TestCase):
	def test_init(self):
		d = Dict(a = 1, b = 'test')
		self.assertEquals(d.a, 1)
		pass

		
