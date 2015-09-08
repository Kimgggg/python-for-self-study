# py.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import types
import functools

class Student(object):
    """test"""
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score

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