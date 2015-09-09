# py.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import types
import functools
import SetDef


class Student(object):
	@property
	def score(self):
	    return self._score
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('整数～～')
		if value<0 or value>100:
			raise ValueError('超出范围')
		self._score = value
	
	@property
	def birth(self):
	    return self._birth
	@birth.setter
	def birth(self, value):
	    self._birth = value
	@property
	def age(self):
	    return 2015 - self._birth

	
	








