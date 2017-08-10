# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

import json

def store(data):
	with open('id.json', 'w') as json_file:
		json_file.write(json.dumps(data))

def load():
	with open('id.json') as json_file:
		data = json.load(json_file)
		return data



data = load()
data["uid"] = "33333333"
store(data)