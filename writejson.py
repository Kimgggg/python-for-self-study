# -*- coding: utf-8 -*-
# encoding: utf-8
#!/usr/bin/env python
# still running on Python 2.7

import json
import os

pwd = '/Users/playcrab/Desktop/test/'
WORD = 'txt'
listdir = os.listdir(pwd)
data_filename = ''
data_list = {}

print type(data_list)
for filename in listdir:
    if filename.split(".")[-1] == WORD:
    	data_filename = filename
    else:
    	pass

read_data_filename = open(pwd + data_filename)
data_list = read_data_filename.read()
read_data_filename.close()

write_json = open(pwd + 'fuck250.json', 'w')
write_json.write(data_list)
write_json.close()

fuckjson = open(pwd + 'ffuu.json', 'w')
fuckjson.write(json.dumps(data_list))
fuckjson.close()

print list(enumerate(data_list))