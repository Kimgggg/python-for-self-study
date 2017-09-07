#!/usr/bin/env python
# encoding: utf-8

def xpath(aaa):
	aaa = aaa.replace('"',"'")
	return aaa

a = xpath('//*[@id="l580"]')
print a
