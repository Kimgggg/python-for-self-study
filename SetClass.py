# py.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import types
import functools

class Student(object):
	"""docstring for Student"""
	def get_score(self):
		return self._score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('整数～～')
		if value < 0 or value > 100:
			raise ValueError('超出范围')
		self._score = value

	
		

    	

class Animal(object):
    """Base class and Super class test"""
    def run(self):
        print 'Animal is running ... '


class Dog(Animal):
    """docstring for Dog"""
    def run(self):
        print 'Dog is 辛巴'
    def eat(self):
        print '辛巴是头猪'


class Cat(Animal):
    """docstring for ClassName"""
    def run(self):
        print 'Cat is 二傻'
    def eat(self):
        print '在家吃屎'
        
def run_twice(Animal):
    Animal.run()
    Animal.run()



