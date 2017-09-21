#!/usr/bin/env python
# encoding: utf-8
import sys
import json
import urllib2

headers = [
    'mod:http',
    'method:Tools.upgradeLevel',
    '__noauth__:1',
    'pGroup:default',
    'sec:8201',
    'MAX_FILE_SIZE:9900000',
    'rid:8001_738',
    'level:1',
    'uploadFrom:提交'
]

print headers[0]&