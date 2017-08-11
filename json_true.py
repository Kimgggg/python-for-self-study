# -*- coding: utf-8 -*-
# encoding: utf-8
#!/usr/bin/env python
# still running on Python 2.7

import json
import os

def is_json(myjson):
	try:
		json.loads(myjson)
	except ValueError:
		return False
	return True

data = {}

os.chdir("/Users/playcrab/Desktop/test/")
a = open('/Users/playcrab/Desktop/test/fuck250.json')
data = a.read()
a.close()

print is_json(data)

json_str = json.dumps(data)

print is_json(json_str)
print json_str

print type(data)
print type(json_str)