#!/usr/bin/env python
# encoding: utf-8
import sys
import urllib2


argv_url = sys.argv[1]

response = urllib2.urlopen(argv_url)
html = response.read()
print html