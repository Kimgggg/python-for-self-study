#!/usr/bin/env python
# encoding: utf-8
import sys

str_end = '),'
pathfile = sys.argv[1]
count_max = sys.argv[2]
count_min = sys.argv[3]

# pathfile = "D:/wyn/mongo.txt"
# count_max = 1600
level = '"level" : NumberInt('
stage = '"stage" : NumberInt('
star = '"star" : NumberInt('
smallStar =  '"smallStar" : NumberInt('
es1 = '"es1" : NumberInt('
el1 = '"el1" : NumberInt('
es2 = '"es2" : NumberInt('
el2 = '"el2" : NumberInt('
es3 = '"es3" : NumberInt('
el3 = '"el3" : NumberInt('
es4 = '"es4" : NumberInt('
el4 = '"el4" : NumberInt('
sl1 = '"sl1" : NumberInt('
sl2 = '"sl2" : NumberInt('
sl3 = '"sl3" : NumberInt('
sl4 = '"sl4" : NumberInt('
avn_0 = '"avn" : NumberInt(0),'
avn_1 = '"avn" : NumberInt(1),'
level_num = []
stage_num = []
star_num = []
smallStar_num = []
es1_num = []
el1_num = []
es2_num = []
el2_num = []
es3_num = []
el3_num = []
es4_num = []
el4_num = []
sl1_num = []
sl2_num = []
sl3_num = []
sl4_num = []
for x in range(1,91):
	level_num.append(x)
	el1_num.append(x)
	el2_num.append(x)
	el3_num.append(x)
	el4_num.append(x)

for x in range(1,7):
	star_num.append(x)

for x in range(0,51):
	smallStar_num.append(x)

for x in range(1,16):
	sl1_num.append(x)
	sl2_num.append(x)
	sl3_num.append(x)
	sl4_num.append(x)

for x in range(1,14):
	stage_num.append(x)
	es1_num.append(x)
	es2_num.append(x)
	es3_num.append(x)
	es4_num.append(x)




#将文件读取到内存中
def modify(a,b,c,d):
	with open(a,"r") as f:
		lines = f.readlines() 
	#写的方式打开文件
	with open(a,"w") as f_w:
		index = 0
		for line in lines:
			index += 1
			if index <= d and index >= 55:	
				if b in line:
					line = line.replace(b, c)
			f_w.write(line)
modify_level = []
for x in level_num:
	modify_level.append(level + str(x) + str_end)
	for y in modify_level:
		modify(pathfile,y,level+str(level_num[89]) + str_end,count_max)
print "兵团等级调整完毕".decode("gbk")

modify_el1 = []
for x in el1_num:
	modify_el1.append(el1 + str(x) + str_end)
	for y in modify_el1:
		modify(pathfile,y,el1+str(el1_num[89]) + str_end,count_max)
print "兵团装备1等级调整完毕"

modify_el2 = []
for x in el2_num:
	modify_el2.append(el2 + str(x) + str_end)
	for y in modify_el2:
		modify(pathfile,y,el2+str(el2_num[89]) + str_end,count_max)
print "兵团装备2等级调整完毕"

modify_el3 = []
for x in el3_num:
	modify_el3.append(el3 + str(x) + str_end)
	for y in modify_el3:
		modify(pathfile,y,el3+str(el3_num[89]) + str_end,count_max)
print "兵团装备3等级调整完毕"

modify_el4 = []
for x in el4_num:
	modify_el4.append(el4 + str(x) + str_end)
	for y in modify_el4:
		modify(pathfile,y,el4+str(el4_num[89]) + str_end,count_max)
print "兵团装备4等级调整完毕"

modify_star = []
for x in star_num:
	modify_star.append(star + str(x) + str_end)
	for y in modify_star:
		modify(pathfile,y,star+str(star_num[5]) + str_end,count_max)
print "兵团星级调整完毕"

modify_smallStar = []
for x in smallStar_num:
	modify_smallStar.append(smallStar + str(x) + str_end)
	for y in modify_smallStar:
		modify(pathfile,y,smallStar+str(smallStar_num[50]) + str_end,count_max)
print "兵团小星调整完毕"

modify_sl1 = []
for x in sl1_num:
	modify_sl1.append(sl1 + str(x) + str_end)
	for y in modify_sl1:
		modify(pathfile,y,sl1+str(sl1_num[14]) + str_end,count_max)
print "兵团1技能调整完毕"

modify_sl2 = []
for x in sl2_num:
	modify_sl2.append(sl2 + str(x) + str_end)
	for y in modify_sl2:
		modify(pathfile,y,sl2+str(sl2_num[14]) + str_end,count_max)
modify(pathfile,sl2 + str(-1) + str_end,sl2+str(sl2_num[14]) + str_end,count_max)
print "兵团2技能调整完毕"

modify_sl3 = []
for x in sl3_num:
	modify_sl3.append(sl3 + str(x) + str_end)
	for y in modify_sl3:
		modify(pathfile,y,sl3+str(sl3_num[14]) + str_end,count_max)
modify(pathfile,sl3 + str(-1) + str_end,sl3+str(sl3_num[14]) + str_end,count_max)
print "兵团3技能调整完毕"

modify_sl4 = []
for x in sl4_num:
	modify_sl4.append(sl4 + str(x) + str_end)
	for y in modify_sl4:
		modify(pathfile,y,sl4+str(sl4_num[14]) + str_end,count_max)
modify(pathfile,sl4 + str(-1) + str_end,sl4+str(sl3_num[14]) + str_end,count_max)
print "兵团4技能调整完毕"

modify_stage = []
for x in stage_num:
	modify_stage.append(stage + str(x) + str_end)
	for y in modify_stage:
		modify(pathfile,y,stage+str(stage_num[12]) + str_end,count_max)
print "兵团品质调整完毕"

modify_es1 = []
for x in es1_num:
	modify_es1.append(es1 + str(x) + str_end)
	for y in modify_es1:
		modify(pathfile,y,es1+str(es1_num[12]) + str_end,count_max)
print "兵团装备1品质调整完毕"

modify_es2 = []
for x in es2_num:
	modify_es2.append(es2 + str(x) + str_end)
	for y in modify_es2:
		modify(pathfile,y,es2+str(es2_num[12]) + str_end,count_max)
print "兵团装备2品质调整完毕"


modify_es3 = []
for x in es3_num:
	modify_es3.append(es3 + str(x) + str_end)
	for y in modify_es3:
		modify(pathfile,y,es3+str(es3_num[12]) + str_end,count_max)
print "兵团装备3品质调整完毕"


modify_es4 = []
for x in es4_num:
	modify_es4.append(es4 + str(x) + str_end)
	for y in modify_es4:
		modify(pathfile,y,es4+str(es4_num[12]) + str_end,count_max)
print "兵团装备4品质调整完毕"


modify(pathfile,avn_0,avn_1,count_max)
print "潜能已激活"



