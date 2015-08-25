# testone.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

#import SetDef
from collections import Iterable
import os
import Image

im = Image.open('/Users/wuyinan/Desktop/IMG_1026.JPG')
w, h = im.size
im.thumbnail((w//2, h//2))
im.save('/Users/wuyinan/Desktop/IMG_10267.JPG')