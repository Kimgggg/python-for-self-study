# testone.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

import SetDef
from SetDef import Student
from collections import Iterable
import os
import Image


bart = SetDef.Student(raw_input('字符串：'),input('数值：'))
lisa = SetDef.Student('fuck',99)


bart.print_score()
lisa.print_score()


bart.score = 90
bart.name = 'wuyinan'

bart.print_score()
print bart.get_grade()