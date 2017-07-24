# encoding: utf-8

import sys
import os
import pprint
import svn.local


r = svn.local.LocalClient('/data/work/svn/数据表/数值开发')
info = r.info()
# pprint.pprint(info)
print type(info)
print info["commit_revision"]