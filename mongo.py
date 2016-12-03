# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

import pymongo

connection = pymongo.Connection('121.199.30.254',27017)
db = connection.BF_A01
connection = db.accounts

print connection.find_one()

