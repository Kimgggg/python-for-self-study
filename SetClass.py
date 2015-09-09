# py.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import types
import functools

class Student(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__

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


class Animal(object):
	"""docstring for Animal"""
	pass
#总类

class Mammal(Animal):
	pass

class Bird(Animal):
	pass

class RunnableMixin(object):
	def run(self):
		print('Running...')

class FylableMixi(object):
	def fly(self):
		print('Flying...')


#大类

class Dog(Mammal, RunnableMixin):
	pass

class Bat(Mammal, RunnableMixin):
	pass

class Parrot(Bird, FylableMixi):
	pass

class Ostrich(Bird, FylableMixi):
	pass

class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def next(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 1024*1024*1024*1024:  #我是来搞笑的
			raise StopIteration();
		return self.a

	def __getitem__(self, n):
		if isinstance(n, int):
			a, b =1, 1 
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			a, b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L

