#!/usr/bin/env python
# encoding: utf-8

import urllib2

req = urllib2.Request("https://meican.com/corps/Playcrab_inc")

response = urllib2.urlopen(req)
the_page = response.read()
print the_page