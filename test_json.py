# -*- coding: utf-8 -*-
#!/usr/bin/env python
# still running on Python 2.7

import json


for x in xrange(1,361):
	f = file("/Users/wuyinan/Documents/bf/bf-excel/json/level/level"+str(x)+".json")
	s = json.load(f)
	m = "'''"+str(s)+"'''"
	try:
		eval(m)
		print x, "is passed"
	except Exception, e:
		print x, "is error"
	f.close()	
print "end"

    		
	






'''
f = file("/Users/wuyinan/Documents/bf/bf-excel/json/level/level105.json")
s = json.load(f)
for x in s["spawnPiecesconfig"]:   #panel piece
    print x
f.close()
'''









#{u'prob': 7, u'pieces': [[1, 19.8], [2, 19.8], [3, 19.8], [4, 19.8], [5, 19.8], [27, 0.75, 1, 1], [29, 0.25, 1]]}

#bb = '''{u'needEnergy': 5, u'maxStep': 34, u'monster': [1004100109, 1004100002, 1004100110, 1004100001, 1004100110, 1004100001, 1004100110], u'starPrice': 0, u'scene': {u'deco': [u'blocks/sh_zudang_01.png', u'blocks/sh_zudang_02.png'], u'board': u'scene_common1/pve_sea.png', u'board_tray': u'scene_common/pve_sea_taizi.png'}, u'award': [[u'key', 2], [u'energy', 3]], u'pieces': [[0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0 0, 0, -1], [-1, -1, 0, 0, 0, -1, -1], [-1, 0, 0, 28, 0, 0, -1], [-1, -1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1, -1], [-1, -1, 0, -1, 0, -1, -1]], u'walls': [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 16, 0, 0, 16, 0, 0, 0, 4, 0, 4, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 16, 0, 0, 0, 16, 0, 0, 4, 0, 0, 0, 4, 0, 4, 4, 16, 0, 16, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0], u'star_score': [14709, 19509, 24629], u'spawnPiecesconfig': [{u'prob': 7, u'pieces': [[1, 19.8], [2, 19.8], [3, 19.8], [4, 19.8], [5, 19.8], [27, 0.75, 1, 1], [29, 0.25, 1]]}, {u'prob': 3, u'pieces': [[1, 16.5], [2, 16.5], [3, 16.5], [4, 16.5], [5, 33], [27, 0.75, 1, 1], [29, 0.25, 1]]}], u'battleScene': u'SeaBattle1', u'goals': [{u'num': 2, u'type': u'panel', u'id': 15}, {u'num': 60, u'type': u'piece', u'id': 5}, {u'num': 7, u'type': u'monster'}], u'allow_item': [1, 3, 4, 16, 20, 14], u'false_probability': 3, u'starGoals': [0, 2, 5], u'panels': [[[0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [6], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0]], [[0], [0], [0], [0], [0], [0], [0]], [[6, 15, 0], [0], [62], [0], [62], [0], [6, 15, 0]]], u'needStar': 0, u'id': 105, u'level_item': [15, 1, 4], u'name': u'\u6bd2\u6c14\u5ba4'}'''

#try:
#	eval(bb)
#	print "yes"
#except Exception, e:
#	print "fuck"
