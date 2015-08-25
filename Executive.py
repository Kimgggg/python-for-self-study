# testone.py
# -*- coding: utf-8 -*-
#!/usr/bin/env python

#import SetDef
from collections import Iterable
import os
import Image


im = Image.open('/Users/wuyinan/Desktop/IMG_1681.PNG')
print im.format, im.size, im.mode
im.thumbnail((200, 100))
im.save('/Users/wuyinan/Desktop/thumb.PNG', 'PNG')