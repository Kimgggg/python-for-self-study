# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

import json
f = file("/Users/wuyinan/Documents/bf/bf-excel/json/level/level105.json")
s = json.load(f)
for x in s["walls"]:   #panel piece
    print x
f.close()


#2个均可正常打印，但是还没学会这么写文件
#上面的只打印出json内walls数组数据，可+if判断
#下面的可以写进一个新数组，新数组写进json即可

import json
testList = []
a = 0
b = 1
f = file("/Users/wuyinan/Documents/bf/bf-excel/json/level/level106.json")
s = json.load(f)
for x in s["walls"]:
    if x == a:
        testList.append(x)
    else:
        pass

    #print x

f.close()
print testList
