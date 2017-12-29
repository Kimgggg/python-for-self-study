#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
from collections import OrderedDict
from datetime import datetime
import requests
import other_config
import other_config_taiwan
import other_config_kor
import os
import sys
import random
import debug_menu
import csv
import csv_operation
import json
from ProgressBar import ProgressBar

reload(sys)
sys.setdefaultencoding('utf-8')

DEBUG = False
PLATFROM = other_config
#默认国内
temp_dict = {}
base_parameter_dict = OrderedDict([
('mod','http'),
('__noauth__','1'),
('pGroup','default'),
('MAX_FILE_SIZE','9900000'),
('uploadFrom','提交')
])
testlist = []
new_list = ''

def Alzheimer_disease(select_number):
	print select_number + " done"
	print "user_rid : %s,\ndev_select : %s,\ndev_server : %s" %(user_rid,dev_select,dev_server)
	print datetime.now()


def del_dict_argv(*type_name):
	for x in type_name:
		del base_parameter_dict[x]


def add_dict_argv(**kwargs):
	for key in kwargs:
		temp_dict[key] = kwargs[key]
	base_parameter_dict.update(temp_dict)
	temp_dict.clear()


def temp_sendItems(itemsId,numbers):
	add_dict_argv(method="Tools.sendItems",goodsId=itemsId,goodsNum=str(numbers))
	try_send_requests()
	del_dict_argv("method","goodsId","goodsNum")


def temp_addRes(Restype,numbers):
	add_dict_argv(method="Tools.addRes",num=str(numbers),type=Restype)
	try_send_requests()
	del_dict_argv("method","num","type")


def try_send_requests():
	try:
		r = requests.get(dev_server, params = base_parameter_dict)
		if DEBUG:
			print "返回信息>>>>>>>>>>>>>>>>>>>\n" + r.text + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
			print "当前字典状态>>>>>>>>>>>>>>>>>>"
			print base_parameter_dict
			print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
			print "发送的请求>>>>>>>>>>>>>>>>>>>>>>>>>>\n" + r.url + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
		else:
			# print "返回信息>>>>>>>>>>>>>>>>>>>\n" + r.text + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
			pass
	except Exception as e:
		print e


def upgradeTeam(team_ID, args=None):
    if args == None:
        set_level = "100"
    else:
    	set_level = args

    add_dict_argv(method="Team.upgradeTeam",level=set_level,teamId=str(team_ID))
    try_send_requests()
    print "兵团" + str(team_ID) + "已升级"
    del_dict_argv("method","level","teamId")


def batchUpgradeEquip(team_ID):
    add_dict_argv(method="Team.batchUpgradeEquip",teamId=str(team_ID))
    try_send_requests()
    print "兵团" + str(team_ID) + "装备已升级"
    del_dict_argv("method","teamId")


def upgradeStageEquip(team_ID,args=None):
    if args == None:
        set_stage = 14
    else:
        set_stage = args
    skillposition = [1,2,3,4]
    add_dict_argv(method="Team.upgradeStageEquip",teamId=str(team_ID))
    for x in skillposition:
        add_dict_argv(positionId=x)
        for y in range(set_stage):
            try_send_requests()
            print "兵团" + str(team_ID) + "装备" + str(x) + "正在第" + str(y) + "次升阶"
    del_dict_argv("method","teamId","positionId")


def upgradeStageTeam(team_ID,args=None):
    if args == None:
        set_stage = 14
    else:
        set_stage = args
    add_dict_argv(method="Team.upgradeStageTeam",teamId=str(team_ID))
    bar = ProgressBar(total = set_stage)
    for x in range(set_stage):
        try_send_requests()
        # print "兵团" + str(team_ID) + "第" + str(x) + "次进阶"
        bar.move()
        bar.log()
        # time.sleep(0.5)

    del_dict_argv("method","teamId")


def TeamupgradeStar(team_ID):
    add_dict_argv(method="Team.upgradeStar",batch="1",teamId=str(team_ID))
    try_send_requests()
    print "兵团" + str(team_ID) + "小星升星完毕"
    del_dict_argv("method","batch","teamId")


def upgradeMaxStar(team_ID):
    add_dict_argv(method="Team.upgradeMaxStar",teamId=str(team_ID))
    try_send_requests()
    print "兵团" + str(team_ID) + "大星升星完毕"
    del_dict_argv("method","teamId")


def activationPotential(team_ID):
    add_dict_argv(method="Team.activationPotential",teamId=str(team_ID))
    try_send_requests()
    print str(team_ID) + "潜能激活完毕"
    del_dict_argv("method","teamId")


def openSkill(team_ID):
    skillposition = [1,2,3,4]
    add_dict_argv(method="Team.openSkill",teamId=str(team_ID))
    for x in skillposition:
        add_dict_argv(positionId=str(x))
        try_send_requests()
        print str(team_ID) + "已激活" + str(x) + "技能"
    del_dict_argv("method","teamId","positionId")


def upgradeSkill(team_ID):
    skillposition = [1,2,3,4]
    add_dict_argv(method="Team.upgradeSkill",args="{\"items\":[[3025,100]]}",teamId=str(team_ID))
    for x in skillposition:
        add_dict_argv(positionId=str(x))
        try_send_requests()
        print str(team_ID) + "技能" + str(x) + "已升级"
    del_dict_argv("method","args","teamId","positionId")


def upPotential(team_ID):
	potentialId = [1,2,3]
	temp_addRes("gold",999999999)
	for x in potentialId:
		add_dict_argv(method="Team.upPotential",teamId=str(team_ID),potentialId=str(x))
		for y in range(40):
			try_send_requests()
			print "兵团" + str(team_ID) + "潜能" + str(x) + "第" + str(y) + "次提升"
		del_dict_argv("method","teamId","potentialId")


def HeroupgradeStar(hero_ID,args=None):
	if args == None:
		set_stage = 4
	else:
		set_stage = args
	add_dict_argv(method="Hero.upgradeStar",heroId=str(hero_ID))
	for x in range(set_stage):
		try_send_requests()
		print "英雄" + str(hero_ID) + "第" + str(x) + "次升星"
	del_dict_argv("method","heroId")

	
def initHeroSlot(hero_ID):
	add_dict_argv(method="Hero.initHeroSlot",heroId=hero_ID)
	try_send_requests()
	print "英雄" + str(hero_ID) + "已激活刻印孔"
	del_dict_argv("method","heroId")


def refreshMastery(hero_ID):
	add_dict_argv(method="Hero.refreshMastery",args='{"reduceType":0,"locks":{},"refreshNum":1}',heroId=str(hero_ID))
	try_send_requests()
	print "英雄" + str(hero_ID) + "已刷新专精"
	del_dict_argv("method","args","heroId")


def saveMastery(hero_ID):
	add_dict_argv(method="Hero.saveMastery",index="1",heroId=str(hero_ID))
	try_send_requests()
	print "英雄" + str(hero_ID) + "随机保存专精成功"
	del_dict_argv("method","index","heroId")


def heroSkillUpgrade(hero_ID,args=None):
	if args == None:
		set_stage = 22
	else:
		set_stage = args
	skillposition = [1,2,3,4]
	add_dict_argv(method="Hero.heroSkillUpgrade",exMode="1",heroId=str(hero_ID))
	for x in skillposition:
		add_dict_argv(positionId=str(x))
		for y in range(set_stage):
			try_send_requests()
			print "第" + str(y) + "次升级" + str(hero_ID) + " " + str(x) + "技能" 
	del_dict_argv("method","exMode","heroId","positionId")


def trainTalent(team_ID):
	temp_list = [1,2,3,4,5,6,7,8,9,10]
	temp_tId = random.sample(temp_list,random.randint(4,7))
	temp_tId.sort()

	add_dict_argv(method="Team.trainTalent",type="2",num="10",teamId=str(team_ID))
	try_send_requests()
	del_dict_argv("method","type","num","teamId")


	add_dict_argv(method="Team.saveTalent",tId=str(temp_tId),teamId=team_ID)
	try_send_requests()
	print "兵团" + str(team_ID) + "已保存天赋" + str(temp_tId)
	del_dict_argv("method","tId","teamId")


def wearDisTreasure(TreasureID):
	add_dict_argv(method="Treasure.wearDisTreasure",disId=str(TreasureID),comId=str(TreasureID)[2:4],positionId=str(TreasureID)[-1])
	try_send_requests()
	print str(TreasureID) + "已装备"
	del_dict_argv("method","disId","comId","positionId")


def activationComTreasure(TreasureID):
	add_dict_argv(method="Treasure.activationComTreasure",comId=str(TreasureID))
	try_send_requests()
	print str(TreasureID) + "已激活组合宝物"
	del_dict_argv("method","comId")

def promoteDisTreasure(TreasureID,args = None):
	if args == None:
		set_stage = 20
	else:
		set_stage = args
	temp_addRes("gold",999999999)
	temp_sendItems("41001",500000)
	add_dict_argv(method="Treasure.promoteDisTreasure",disId=str(TreasureID), comId=str(TreasureID)[2:4])
	for x in range(set_stage):
		try_send_requests()
		print "第" + str(x) + "次进阶" + str(TreasureID)
	del_dict_argv("method","disId","comId")

def promoteComTreasure(TreasureID,args = None):
	if args == None:
		set_stage = 20
	else:
		set_stage = args
	temp_addRes("gold",999999999)
	temp_sendItems("41001",500000)
	add_dict_argv(method="Treasure.promoteComTreasure",comId=str(TreasureID))
	for x in range(set_stage):
		try_send_requests()
		print "组合宝物" + str(TreasureID) + "第" + str(x) + "次进阶"
	del_dict_argv("method","comId")

def TreasureupStar(TreasureID,args = None):
	if args == None:
		set_stage = 50
	else:
		set_stage = args
	temp_addRes("starfrag",1000000)
	temp_addRes("gold",999999999)
	add_dict_argv(method="Treasure.upStar",num="10",disId=str(TreasureID), comId=str(TreasureID)[2:4])
	for x in range(set_stage):
		try_send_requests()
		print str(TreasureID) + "第" + str(x) + "次升星"
	del_dict_argv("method","num","disId","comId")


def select_server(argv):
	global new_list
	global PLATFROM
	if argv == "6" or argv == "8":
		add_dict_argv(pGroup="test")
		PLATFROM = other_config_taiwan
		new_list = '%s,%s,%s,%s,%s' %(
			PLATFROM.bingtuansuipianId,
			PLATFROM.jinjiecailiaoId,
			PLATFROM.herosuipianId,
			PLATFROM.baowustr,
			PLATFROM.otheritem)
	elif argv == "9":
		add_dict_argv(pGroup="test")
		PLATFROM = other_config_kor
		new_list = '%s,%s,%s,%s,%s' %(
			PLATFROM.bingtuansuipianId,
			PLATFROM.jinjiecailiaoId,
			PLATFROM.herosuipianId,
			PLATFROM.baowustr,
			PLATFROM.otheritem)
	elif argv == "4" or argv == "5" or argv == "7":
		add_dict_argv(pGroup="aqq")
		PLATFROM = other_config
		new_list = '%s,%s,%s,%s,%s,%s' %(
			PLATFROM.bingtuansuipianId,
			PLATFROM.jinjiecailiaoId,
			PLATFROM.herosuipianId,
			PLATFROM.baowustr,
			PLATFROM.otheritem,
			PLATFROM.fashusuipian)
	else:
		add_dict_argv(pGroup="default")
		PLATFROM = other_config
		new_list = '%s,%s,%s,%s,%s,%s' %(
			PLATFROM.bingtuansuipianId,
			PLATFROM.jinjiecailiaoId,
			PLATFROM.herosuipianId,
			PLATFROM.baowustr,
			PLATFROM.otheritem,
			PLATFROM.fashusuipian)


user_rid = raw_input("输入rid:\n".decode('utf-8').encode('gbk'))
debug_menu.server_menu()
dev_select = raw_input("选择服务器:\n".decode('utf-8').encode('gbk'))
select_server(dev_select)
dev_server = PLATFROM.debug_server_requests[int(dev_select) - 1]
add_dict_argv(rid=user_rid, sec=user_rid[:4])

while True:
	debug_menu.main_menu()

	press = raw_input("select:")
	if press == "1":
		debug_menu.res_menu()
		select_type = raw_input("选择资源类型:\n".decode('utf-8').encode('gbk'))
		add_dict_argv(method="Tools.addRes",num=raw_input("输入资源数量:\n".decode('utf-8').encode('gbk')))
		if select_type == "1":
			for x in PLATFROM.resource:
				add_dict_argv(type=x)
				try_send_requests()
				print x + "发送成功"
		elif select_type == "2":
			add_dict_argv(type="gem")
			try_send_requests()
			print "gem发送成功"
		elif select_type == "3":
			add_dict_argv(type="gold")
			try_send_requests()
			print "gold发送成功"
		elif select_type == "4":
			add_dict_argv(type="physcal")
			try_send_requests()
			print "physcal发送成功"
		elif select_type == "5":
			add_dict_argv(type="texp")
			try_send_requests()
			print "texp发送成功"
		elif select_type == "6":
			print json.dumps(csv_operation.get_csv("csvdata/ResName.csv"),ensure_ascii=False,indent=4)
			add_dict_argv(type=raw_input("输入资源类型:\n".decode('utf-8').encode('gbk')))
			try_send_requests()
			print "发送成功"
		del_dict_argv("num","type","method")
		Alzheimer_disease(press)
			
	elif press == "2":
		debug_menu.set_level()
		select_type = raw_input("select:\n")
		if select_type == "1":
			add_dict_argv(method="Tools.upgradeLevel", level=raw_input("输入要提升的等级:\n".decode('utf-8').encode('gbk')))
			try_send_requests()
			print "等级调整完毕"
			del_dict_argv("method","level")
			Alzheimer_disease(press)
		elif select_type == "2":
			add_dict_argv(type="exp",num=raw_input("输入经验:\n".decode('utf-8').encode('gbk')),method="Tools.addRes")
			try_send_requests()
			del_dict_argv("method","num","type")
			print "exp发送成功"
			Alzheimer_disease(press)
			
	elif press == "3":
		add_dict_argv(method="Tools.setVipLevel",level=raw_input("输入要设置的vip等级:\n".decode('utf-8').encode('gbk')))
		try_send_requests()
		print "vip等级调整完毕"
		del_dict_argv("method","level")
		Alzheimer_disease(press)

	elif press == "4":
		temp_stageId = ["710","720"]
		print "第15章第5小关 则输入 1505"
		stage = raw_input("请输入关卡id:\n".decode('utf-8').encode('gbk'))
		while int(stage[-2:]) > 15 or int(stage[:2]) > 26 or len(stage) < 4:
			stage = raw_input("请重新输入关卡id:\n".decode('utf-8').encode('gbk'))
		add_dict_argv(method="Tools.batchPassStage",stageId=(temp_stageId[0] + stage))
		try_send_requests()
		add_dict_argv(stageId=temp_stageId[1] + str((int(stage[:2]) - 1)) + "05")
		try_send_requests()
		del_dict_argv("method","stageId")
		Alzheimer_disease(press)

	elif press == "5":
		debug_menu.item_menu()
		select_type = raw_input("选择道具类型:\n".decode('utf-8').encode('gbk'))
		add_dict_argv(goodsNum=raw_input("输入道具数量:\n".decode('utf-8').encode('gbk')), method="Tools.sendItems")
		if select_type == "1":
			add_dict_argv(goodsId=new_list)
			try_send_requests()
			print "全部物品发送成功"
		elif select_type == "2":
			add_dict_argv(goodsId=PLATFROM.bingtuansuipianId)
			try_send_requests()
			print "发放兵团碎片成功"
		elif select_type == "3":
			add_dict_argv(goodsId=PLATFROM.jinjiecailiaoId)
			try_send_requests()
			print "发放进阶材料成功"
		elif select_type == "4":
			add_dict_argv(goodsId=PLATFROM.herosuipianId)
			try_send_requests()
			print "发放英雄碎片成功"
		elif select_type == "5":
			add_dict_argv(goodsId=PLATFROM.baowustr)
			try_send_requests()
			print "发放宝物成功"
		elif select_type == "6":
			add_dict_argv(goodsId=PLATFROM.otheritem)
			try_send_requests()
			print "发放杂物成功"
		elif select_type == "7":
			add_dict_argv(goodsId=PLATFROM.fashusuipian)
			try_send_requests()
			print "发放法术碎片成功"
		elif select_type == "8":
			add_dict_argv(goodsId=raw_input("输入道具ID:\n".decode('utf-8').encode('gbk')))
			try_send_requests()
			print "发送成功"
		del_dict_argv("goodsNum","goodsId","method")
		Alzheimer_disease(press)

	elif press == "6":
		debug_menu.Treasure_menu()
		TreasureCOM = []
		for x in PLATFROM.baowu:
			TreasureCOM.append(str(x)[2:4])
		TreasureCOM = list(set(TreasureCOM))
		select_type = raw_input("select:\n".decode('utf-8').encode('gbk'))
		if select_type == "1":
			for x in PLATFROM.baowu:
				wearDisTreasure(x)
			for x in TreasureCOM:
				activationComTreasure(x)
			for x in PLATFROM.baowu:
				promoteDisTreasure(x)
				TreasureupStar(x)
			for x in TreasureCOM:
				promoteComTreasure(x)
		elif select_type == "2":
			debug_menu.Treasure()
			type_choose = raw_input("select:\n".decode('utf-8').encode('gbk'))
			if type_choose == "1":
				wearDisTreasure(raw_input("请输入宝物ID:\n".decode('utf-8').encode('gbk')))
			elif type_choose == "2":
				activationComTreasure(raw_input("请输入组件宝物ID:\n".decode('utf-8').encode('gbk')))
			elif type_choose == "3":
				promoteDisTreasure(raw_input("请输入散件宝物ID:\n".decode('utf-8').encode('gbk')),input("请输入进阶次数:\n".decode('utf-8').encode('gbk')))
			elif type_choose == "4":
				promoteComTreasure(raw_input("请输入组合宝物ID:\n".decode('utf-8').encode('gbk')),input("请输入进阶次数:\n".decode('utf-8').encode('gbk')))
			elif type_choose == "5":
				TreasureupStar(raw_input("请输入散件宝物ID:\n".decode('utf-8').encode('gbk')),input("请输入进阶次数:\n".decode('utf-8').encode('gbk')))
	
	elif press == "7":
		add_dict_argv(method="Tools.sendHero")
		for x in PLATFROM.heroId:
			add_dict_argv(heroId=x)
			try_send_requests()
			print "已发送" + str(x)
		del_dict_argv("method","heroId")
		Alzheimer_disease(press)
 
	elif press == "8":
		debug_menu.hero_choose()
		select_type = raw_input("select:\n".decode('utf-8').encode('gbk'))
		if select_type == "1":
			for x in PLATFROM.heroId:
				HeroupgradeStar(x)
				initHeroSlot(x)
				for z in range(5):
					refreshMastery(x)
					saveMastery(x)
				heroSkillUpgrade(x)
			Alzheimer_disease(press)
		elif select_type == "2":
			heroID = raw_input("输入英雄id:\n".decode('utf-8').encode('gbk'))
			debug_menu.hero_type_choose()
			type_choose = raw_input("select:\n")
			if type_choose == "1":
				time = input("输入升星次数:\n".decode('utf-8').encode('gbk'))
				HeroupgradeStar(heroID,time)
			elif type_choose == "2":
				initHeroSlot(heroID)
			elif type_choose == "3":
				time = input("输入刷新次数:\n".decode('utf-8').encode('gbk'))
				for x in range(time):
					refreshMastery(heroID)
					saveMastery(heroID)
			elif type_choose == "4":
				time = input("输入技能提升次数(十连抽):\n".decode('utf-8').encode('gbk'))
				heroSkillUpgrade(heroID,time)
			elif type_choose == "5":
				HeroupgradeStar(heroID)
				initHeroSlot(heroID)
				heroSkillUpgrade(heroID)
			Alzheimer_disease(press)
				
	elif press == "9":
		add_dict_argv(method="Tools.createTeam")
		for x in PLATFROM.bingtuanId:
			add_dict_argv(teamId=x)
			try_send_requests()
			print "已发放" + str(x)
		del_dict_argv("method","teamId")
		Alzheimer_disease(press)

	elif press == "10":
		debug_menu.team_choose()
		select_type = raw_input("select:\n")

		if select_type == "1":
			for x in PLATFROM.bingtuanId:
				upgradeTeam(x)
				batchUpgradeEquip(x)
				upgradeStageEquip(x)
				upgradeStageTeam(x)
				temp_addRes("texp",99999999)
				temp_addRes("gold",999999999)

			temp_addRes("gold",999999999)
			for x in PLATFROM.bingtuanId1star:
				TeamupgradeStar(x)
				upgradeMaxStar(x)
			new_bingtuansuipian2star = PLATFROM.bingtuanId1star + PLATFROM.bingtuanId2star

			for x in new_bingtuansuipian2star:
				TeamupgradeStar(x)
				upgradeMaxStar(x)
			
			temp_addRes("gold",999999999)
			for x in PLATFROM.bingtuanId:
				for y in range(3):
					TeamupgradeStar(x)
					upgradeMaxStar(x)

			temp_addRes("gold",999999999)
			temp_sendItems("3025",5000000)
			for x in PLATFROM.bingtuanId:
				activationPotential(x)
				openSkill(x)
				upgradeSkill(x)
				upPotential(x)
			Alzheimer_disease(press)


		elif select_type == "2":
			team_ID = raw_input("输入兵团id:\n".decode('utf-8').encode('gbk'))
			debug_menu.team_type_choose1()
			type_choose = raw_input("select:\n")
			if type_choose == "1":
				set_level = raw_input("输入提升的等级:\n".decode('utf-8').encode('gbk'))
				upgradeTeam(team_ID,set_level)
			elif type_choose == "2":
				batchUpgradeEquip(team_ID)
			elif type_choose == "3":
				set_stage = input("输入需要进阶的次数:\n".decode('utf-8').encode('gbk'))
				upgradeStageEquip(team_ID,set_stage)
			elif type_choose == "4":
				set_stage = input("输入要升阶的次数:\n".decode('utf-8').encode('gbk'))
				upgradeStageTeam(team_ID,set_stage)
			elif type_choose == "5":
				upgradeStarTime = input("输入升星次数:\n".decode('utf-8').encode('gbk'))
				for x in range(upgradeStarTime):
					TeamupgradeStar(team_ID)
					upgradeMaxStar(team_ID)
			elif type_choose == "6":
				activationPotential(team_ID)
			elif type_choose == "7":
				openSkill(team_ID)
			elif type_choose == "8":
				temp_sendItems("3025",400)
				upgradeSkill(team_ID)
			elif type_choose == "9":
				upPotential(team_ID)
			elif type_choose == "10":
				upgradeTeam(team_ID)
				batchUpgradeEquip(team_ID)
				upgradeStageEquip(team_ID)
				upgradeStageTeam(team_ID)
				for x in range(6):
					TeamupgradeStar(team_ID)
					upgradeMaxStar(team_ID)
				activationPotential(team_ID)
				openSkill(team_ID)
				temp_sendItems("3025",400)
				upgradeSkill(team_ID)
				upPotential(team_ID)
			Alzheimer_disease(press)

	elif press == "11":
		user_rid = raw_input("输入rid:\n".decode('utf-8').encode('gbk'))
		debug_menu.server_menu()
		dev_select = raw_input("选择服务器:\n".decode('utf-8').encode('gbk'))
		select_server(dev_select)
		dev_server = PLATFROM.debug_server_requests[int(dev_select) - 1]
		add_dict_argv(rid=user_rid, sec=user_rid[:4])


	elif press == "12":
		add_dict_argv(method="Hero.combineSpellBook")
		for x in PLATFROM.skillId:
			add_dict_argv(sid=x)
			try_send_requests()
			print str(x) + "激活成功"
		del_dict_argv("method","sid")
		Alzheimer_disease(press)

		add_dict_argv(method="Hero.upLevelSpellBook")
		for x in PLATFROM.skillId:
			add_dict_argv(sid=x)
			for y in range(5):
				try_send_requests()
				print str(x) + "第" + str(y) + "升级成功"
		del_dict_argv("method","sid")
		Alzheimer_disease(press)

	elif press == "13":
		poke_id = [4,5]
		add_dict_argv(method="Pokedex.activePokedexPos")
		for x in range(14):
			add_dict_argv(pokedexId=x)
			for y in poke_id:
				add_dict_argv(positionId=y)
				try_send_requests()
				print "图鉴" + str(x) + " " + str(y) + "激活成功"
		del_dict_argv("method","pokedexId","positionId")

		add_dict_argv(method="Pokedex.upPokedexLevel",)
		for x in range(14):
			add_dict_argv(pokedexId=x)
			for y in range(25):
				try_send_requests()
				print "图鉴" + str(x) + "第" + str(y) + "次升级"
		del_dict_argv("method","pokedexId")
		Alzheimer_disease(press)
		
	elif press == "14":
		temp_addRes("starNum",200000)

		add_dict_argv(method="Talent.upTalentChildLv")
		for x in PLATFROM.magicTalent:
			add_dict_argv(tid=x,kind=str(x)[:2])
			for y in range(10):
				try_send_requests()
				print "天赋" + str(x) + "第" + str(y) + "次升级"
		del_dict_argv("method","tid","kind")
		Alzheimer_disease(press)

	elif press == "15":
		debug_menu.clear_data()
		select_type = raw_input("select:\n")
		if select_type == "1":
			add_dict_argv(method="Tools.clearUserData",type="4")
			try_send_requests()
			print "清空背包成功"
			del_dict_argv("method","type")
			Alzheimer_disease(press)
		elif select_type == "2":
			add_dict_argv(method="Tools.clearUserData",type="1")
			try_send_requests()
			print "每日状态重置成功,需重新登录"
			del_dict_argv("method","type")
			Alzheimer_disease(press)
		elif select_type == "3":
			add_dict_argv(method="Tools.clearUser")
			try_send_requests()
			del_dict_argv("method")
			print "账号已重置"
			Alzheimer_disease(press)
		elif select_type == "4":
			add_dict_argv(method="Tools.resetBoss")
			try_send_requests()
			print "pve次数清空完毕"
			del_dict_argv("method")
			Alzheimer_disease(press)
		elif select_type == "5":
			add_dict_argv(method="Tools.clearYac",actDev="0")
			try_send_requests()
			print "debug yac清除成功"
			del_dict_argv("method","actDev")
			Alzheimer_disease(press)
		elif select_type == "6":
			add_dict_argv(method="Tools.clearQuitGuildCD")
			try_send_requests()
			del_dict_argv("method")
			Alzheimer_disease(press)
		elif select_type == "7":
			add_dict_argv(method="Tools.initCrossPK")
			try_send_requests()
			del_dict_argv("method")
			Alzheimer_disease(press)

	elif press == "16":
		debug_menu.team_choose()
		select_type = raw_input("select:\n")
		if select_type == "1":
			add_dict_argv(method="Tools.activateAwaking")
			for x in PLATFROM.activateAwaking:
				add_dict_argv(teamId=x)
				try_send_requests()
				print "兵团" + str(x) + "已觉醒"
			del_dict_argv("method","teamId")

			for x in PLATFROM.activateAwaking:
				temp_sendItems("94"+str(x),200000)

			for x in PLATFROM.activateAwaking:
				add_dict_argv(method="Awaking.upAwakingLevel",teamId=x)
				for y in range(7):
					try_send_requests()
					print "兵团" + str(x) + "第" + str(y) + "次觉醒强化"	
			del_dict_argv("method","teamId")
			Alzheimer_disease(press)
		elif select_type == "2":
			team_ID = raw_input("输入兵团id:\n".decode('utf-8').encode('gbk'))
			while int(team_ID) not in PLATFROM.activateAwaking:
				team_ID = raw_input("输入错误,重新输入兵团id:\n".decode('utf-8').encode('gbk'))
			debug_menu.activateAwaking()
			activateAwaking_choose = raw_input("select:\n")
			if activateAwaking_choose == "1":
				add_dict_argv(method="Tools.activateAwaking",teamId=team_ID)
				try_send_requests()
				print "兵团" + str(team_ID) + "已觉醒"
				del_dict_argv("method","teamId")
			elif activateAwaking_choose == "2":
				temp_sendItems("94"+str(team_ID),200000)
				set_stage = input("输入觉醒强化次数:\n".decode('utf-8').encode('gbk'))
				add_dict_argv(method="Awaking.upAwakingLevel",teamId=team_ID)
				for x in range(set_stage):
					try_send_requests()
					print "兵团" + str(team_ID) + "第" + str(x) + "次觉醒强化"	
				del_dict_argv("method","teamId")

	elif press == "17":
		temp_addRes("gem",999999)
		temp_addRes("gold",999999)
		temp_sendItems("3044,3045,3046,3047,3048",20000)
		debug_menu.team_choose()
		select_type = raw_input("select:\n")
		trainTalentTime = input("输入循环次数:\n".decode('utf-8').encode('gbk'))
		if select_type == "1":
			for x in other_config.bingtuanId:
				for y in range(trainTalentTime):
					trainTalent(x)
		elif select_type == "2":
			team_ID = raw_input("输入兵团id:\n".decode('utf-8').encode('gbk'))
			for x in range(trainTalentTime):
				trainTalent(team_ID)
		Alzheimer_disease(press)

	elif press == "18":
		debug_menu.reward_menu()
		select_type = raw_input("选择抽卡类型:\n".decode('utf-8').encode('gbk'))
		print "清空背包中...."
		add_dict_argv(method="Tools.clearUserData",type="4")
		try_send_requests()
		del_dict_argv("method","type")
		print "背包清空完毕，请输入抽取次数并选择类型"
		number = input("输入抽卡次数:\n".decode('utf-8').encode('gbk'))
		if select_type == "1":
			temp_addRes("gem",number*2700)
			add_dict_argv(method="Team.drawAward",num="10",typeId="2")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","typeId")
			Alzheimer_disease(press)
		elif select_type == "2":
			temp_addRes("gem",number*300)
			add_dict_argv(method="Team.drawAward",num="1",typeId="2")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","typeId")
			Alzheimer_disease(press)
		elif select_type == "3":
			temp_sendItems("3001",number*10)
			add_dict_argv(method="Team.drawAward",num="10",typeId="1")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","typeId")
			Alzheimer_disease(press)
		elif select_type == "4":
			temp_sendItems("3001",number)
			add_dict_argv(method="Team.drawAward",num="1",typeId="1")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","typeId")
			Alzheimer_disease(press)
		elif select_type == "5":
			temp_addRes("gem",number*880)
			add_dict_argv(method="Hero.drawSpeelBook",num="10",type="2")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","type")
			Alzheimer_disease(press)
		elif select_type == "6":
			temp_addRes("gem",number*100)
			add_dict_argv(method="Hero.drawSpeelBook",num="1",type="2")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","type")
			Alzheimer_disease(press)
		elif select_type == "7":
			temp_sendItems("40005",number*10)
			add_dict_argv(method="Hero.drawSpeelBook",num="10",type="1")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","type")
			Alzheimer_disease(press)
		elif select_type == "8":
			temp_sendItems("40005",number)
			add_dict_argv(method="Hero.drawSpeelBook",num="1",type="1")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","type")
			Alzheimer_disease(press)
		elif select_type == "9":
			temp_addRes("gem",number*880)
			for x in range(number):
				if x%16 == 0:
					add_dict_argv(method="Tools.clearUserData",type="1")
					try_send_requests()
					print "清除次数限制成功"
					del_dict_argv("method","type")
				add_dict_argv(method="Treasure.drewDisTreasure",num="5")
				try_send_requests()
				del_dict_argv("method","num")
				print "第" + str(x) + "抽卡成功"
			Alzheimer_disease(press)
		elif select_type == "10":
			temp_addRes("gem",number*200)
			add_dict_argv(method="Treasure.drewDisTreasure",num="1")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num")
			Alzheimer_disease(press)

		elif select_type == "11":
			temp_addRes("gem",number*880)
			for x in range(number):
				if x%20 == 0:
					add_dict_argv(method="Tools.clearUserData",type="1")
					try_send_requests()
					print "清除次数限制成功"
					del_dict_argv("method","type")
				add_dict_argv(method="Weapon.drawSiegeWeapon",type="2")
				try_send_requests()
				print "第" + str(x) + "次抽配件成功"
				del_dict_argv("method","type")
			Alzheimer_disease(press)

	elif press == "19":
		with open('E:/war/svn/configCsv/csv/nests.csv','rb') as csvFile:
			reader = csv.reader(csvFile)
			column1 = [row[0] for row in reader]
			col1 = column1[5:46]
		with open('E:/war/svn/configCsv/csv/nests.csv','rb') as csvFile:
			reader = csv.reader(csvFile)
			column2 = [row[1] for row in reader]
			col2 = column2[5:46]

		for x in range(len(col1)):
			add_dict_argv(cid=col2[x],nid=col1[x],method="nests.constructNest")
			try_send_requests()
			print "第" + str(x) + "个巢穴建造成功"
			for y in range(5):
				add_dict_argv(method="nests.upgradeNest")
				try_send_requests()
				print "第" + str(y) + "次升级"
		del_dict_argv("method","cid","nid")
		Alzheimer_disease(press)
				
	elif press == "test":
		# testusid = ['a914151342092', 'a914151342287', 'a914151342140', 'a914151342271', 'a914151342223', 'a914151342124', 'a914151342319', 'a914151342239', 'a914151342335', 'a914151342303',  'a914151342108', 'a914151342236', 'a914151342172', 'a914151342156', 'a914151342204', 'a914151342220', 'a914151342252', 'a914151342268', 'a914151342188', 'a914151342332','a914151342253','a914151342189','a914151342141','a914151342109','a914151342205','a914151342093','a914151342125','a914151342300','a914151342157','a914151342173','a914151342284','a914151342237','a914151342269','a914151342317','a914151342333','a914151342285','a914151342316','a914151342221']
		# for x in testusid:
		# 	add_dict_argv(method="Tools.usidTransfer",usid=x)
		# 	r = requests.get(dev_server, params = base_parameter_dict)
		# 	# print r.text
		# 	a = str(r.text)
		# 	testlist.append(a)
		# 	del_dict_argv("method","usid")

		# print testlist
		# # for x in testlist:
		# # 	add_dict_argv(method="Tools.modiLevel", level="22",rid=x,sec="9141")
		# # 	try_send_requests()
		# # 	print x + "done"
		# # 	del_dict_argv("method","level","rid","sec")
			
		# for x in testlist:
		# 	add_dict_argv(goodsNum="999", method="Tools.sendItems",goodsId="99999",rid=str(x),sec="9141")
		# 	try_send_requests()
		# 	print x + " done"
		# 	del_dict_argv("goodsNum","method","goodsId")

		# # for x in testlist:
		# 	add_dict_argv(method="Tools.addRes",num="999999999",type="guildPower",rid=x,sec="9141")
		# 	try_send_requests()
		# 	print str(x) + " done"
		# 	del_dict_argv("method","num","type")
		for x in PLATFROM.skillId:
			add_dict_argv(method="Tools.initSpellBook",id=str(x))
			try_send_requests()
			del_dict_argv("method","id")
			

	else:
		os.exit(1)
		