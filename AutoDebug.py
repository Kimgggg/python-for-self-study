#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
from collections import OrderedDict
import requests
import other_config
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

DEBUG = False
temp_dict = {}
base_parameter_dict = OrderedDict([
('mod','http'),
('__noauth__','1'),
('pGroup','default'),
('MAX_FILE_SIZE','9900000'),
('uploadFrom','提交')
])

def del_dict_argv(*type_name):
	for x in type_name:
		del base_parameter_dict[x]


def add_dict_argv(**kwargs):
	for key in kwargs:
		temp_dict[key] = kwargs[key]
	base_parameter_dict.update(temp_dict)
	temp_dict.clear()


def send_requests():
	r = requests.get(dev_server, params = base_parameter_dict)
	if DEBUG:
		print "返回信息>>>>>>>>>>>>>>>>>>>\n" + r.text + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
		print "当前字典状态>>>>>>>>>>>>>>>>>>"
		print base_parameter_dict
		print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
		print "发送的请求>>>>>>>>>>>>>>>>>>>>>>>>>>\n" + r.url + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
	else:
		print "返回信息>>>>>>>>>>>>>>>>>>>\n" + r.text + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"

	

user_rid = raw_input("please input rid:\n")
print '''
1.开发机1
2.开发机2
3.开发机3
4.dev3
5.dev4
6.台湾
'''
dev_server = raw_input("please input debug server:\n")
if dev_server == "6":
	add_dict_argv(pGroup="test")
else:
	add_dict_argv(pGroup="default")
dev_server = other_config.debug_server_requests[int(dev_server) - 1]
add_dict_argv(rid=user_rid, sec=user_rid[:4])

while True:
	print """
    1.添加金币、钻石、兵团经验、体力
    2.玩家升级
    3.设置vip等级
    4.提升全部兵团潜力
    5.调整副本进度
    6.发全部材料
    7.全部宝物进阶
    8.发放全部英雄
    9.英雄升星
    10.英雄技能升级
    11.发放全部兵团
    12.所有兵团升级+所有兵团装备升级+所有兵团装备进阶
    13.更换user_rid与服务器
    14.所有兵团升星+激活潜能
    15.重置pve玩法次数
    16.法术激活升级（只允许在开发机1上使用）
    17.兵团进阶
    18.清除yac
    19.宝物升星
    q.退出
    """

	press = raw_input("select:")
	if press == "1":
		add_dict_argv(method="Tools.addRes",num=raw_input("please input resource number:\n"))
		for x in other_config.resource:
			print x
			add_dict_argv(type=x)
			send_requests()
		del_dict_argv("num","type","method")
			
	elif press == "2":
		add_dict_argv(method="Tools.upgradeLevel", level=raw_input("please input level number:\n"))
		send_requests()
		del_dict_argv("method","level")

	elif press == "3":
		add_dict_argv(method="Tools.setVipLevel",level=raw_input("please input level number:\n"))
		send_requests()
		del_dict_argv("method","level")

	elif press == "4":
		add_dict_argv(method="Team.upPotential")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			for y in other_config.potentialId:
				add_dict_argv(potentialId=y)
				for z in range(41):
					send_requests()
					print "兵团" + str(x) + "潜能" + str(y) + "第" + str(z) + "次提升"
		del_dict_argv("method","teamId","potentialId")

	elif press == "5":
		add_dict_argv(method="Tools.batchPassStage")
		for x in other_config.stageId:
			add_dict_argv(stageId=x)
			send_requests()
		del_dict_argv("method","stageId")

	elif press == "6":
		add_dict_argv(goodsNum=raw_input("please input item number:\n"), method="Tools.sendItems")
		new_list = 	other_config.bingtuansuipianId + "," + other_config.jinjiecailiaoId + "," + other_config.herosuipianId + "," + other_config.baowustr + "," + other_config.otheritem + "," + other_config.fashusuipian
		print '''
	1.发送全部
	2.发送全部兵团碎片
	3.发送全部进阶材料
	4.发送全部英雄碎片
	5.发送全部宝物
	6.发送全部其他道具
	7.发送全部法术碎片
		'''
		select_type = raw_input("please select num:\n")
		if select_type == "1":
			add_dict_argv(goodsId=new_list)
			send_requests()
			print "全部物品发送成功"
		elif select_type == "2":
			add_dict_argv(goodsId=other_config.bingtuansuipianId)	
			send_requests()
			print "发放兵团碎片成功"
		elif select_type == "3":
			add_dict_argv(goodsId=other_config.jinjiecailiaoId)
			send_requests()
			print "发放进阶材料成功"
		elif select_type == "4":
			add_dict_argv(goodsId=other_config.herosuipianId)
			send_requests()
			print "发放英雄碎片成功"
		elif select_type == "5":
			add_dict_argv(goodsId=other_config.baowustr)
			send_requests()
			print "发放宝物成功"
		elif select_type == "6":
			add_dict_argv(goodsId=other_config.otheritem)
			send_requests()
			print "发放杂物成功"
		elif select_type == "7":
			add_dict_argv(goodsId=other_config.fashusuipian)
			send_requests()
			print "发放法术碎片成功"
		del_dict_argv("goodsNum","goodsId","method")

	elif press == "7":
		add_dict_argv(goodsNum="9999999")
		add_dict_argv(goodsId="41001")
		add_dict_argv(method="Tools.sendItems")
		send_requests()
		del_dict_argv("goodsNum","goodsId","method")

		add_dict_argv(method="Treasure.promoteDisTreasure")
		for x in other_config.baowu:
			strx = x
			add_dict_argv(disId=x, comId=str(strx)[2:4])
			for y in range(21):
				send_requests()
				print "第" + str(y) + "次进阶" + str(x)
		del_dict_argv("method","disId","comId")

	elif press == "8":
		add_dict_argv(method="Tools.sendHero")
		for x in other_config.heroId:
			add_dict_argv(heroId=x)
			send_requests()
			print "已发送" + str(x)
		del_dict_argv("method","heroId")

	elif press == "9":
		add_dict_argv(method="Hero.upgradeStar")
		for x in other_config.heroId:
			add_dict_argv(heroId=x)
			for y in range(4):
				send_requests()
				print "英雄" + str(x) + "第" + str(y) + "次升星"
		del_dict_argv("method","heroId")

	elif press == "10":
		add_dict_argv(method="Hero.heroSkillUpgrade",exMode="1")
		for x in other_config.heroId:
			add_dict_argv(heroId=x)
			for y in other_config.skillposition:
				add_dict_argv(positionId=y)
				for z in range(22):
					send_requests()
					print "第" + str(z) + "次升级" + str(x) + " " + str(y) + "技能" 

		del_dict_argv("method","exMode","heroId","positionId")

	elif press == "11":
		add_dict_argv(method="Tools.createTeam")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			send_requests()
			print "已发放" + str(x)
		del_dict_argv("method","teamId")

	elif press == "12":
		add_dict_argv(method="Team.upgradeTeam",level="90")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			send_requests()
			print "兵团" + str(x) + "已升级"
		del_dict_argv("method","level","teamId")

		add_dict_argv(method="Team.batchUpgradeEquip")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			send_requests()
			print "兵团" + str(x) + "装备已升级"
		del_dict_argv("method","teamId")

		add_dict_argv(method="Team.upgradeStageEquip")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			for y in other_config.skillposition:
				add_dict_argv(positionId=y)
				for z in range(14):
					send_requests()
					print "兵团" + str(x) + "装备" + str(y) + "正在第" + str(z) + "次升阶"
		del_dict_argv("method","teamId","positionId")
	
	elif press == "13":
		user_rid = raw_input("please input rid:\n")
		print '''
		1.开发机1
		2.开发机2
		3.开发机3
		4.dev3
		5.dev4
		6.台湾
		'''
		dev_server = raw_input("please input debug server:\n")
		if dev_server == "6":
			add_dict_argv(pGroup="test")
		else:
			add_dict_argv(pGroup="default")
		dev_server = other_config.debug_server_requests[int(dev_server) - 1]
		add_dict_argv(rid=user_rid, sec=user_rid[:4])
		print base_parameter_dict

	elif press == "14":
		def update_small_star(list_name):
			add_dict_argv(method="Team.upgradeStar",batch="1")
			for x in list_name:
				add_dict_argv(teamId=x)
				send_requests()
				print "兵团" + str(x) + "小星升星完毕"
			del_dict_argv("method","batch","teamId")

		def update_big_star(list_name):
			add_dict_argv(method="Team.upgradeMaxStar")
			for x in list_name:
				add_dict_argv(teamId=x)
				send_requests()
				print "兵团" + str(x) + "大星升星完毕"
			del_dict_argv("method","teamId")

		update_small_star(other_config.bingtuanId1star)
		update_big_star(other_config.bingtuanId1star)
		new_bingtuansuipian2star = other_config.bingtuanId1star + other_config.bingtuanId2star
		update_small_star(new_bingtuansuipian2star)
		update_big_star(new_bingtuansuipian2star)
		new_bingtuansuipian3star = new_bingtuansuipian2star + other_config.bingtuanId3star
		for x in range(3):
			update_small_star(new_bingtuansuipian3star)
			update_big_star(new_bingtuansuipian3star)

		add_dict_argv(method="Team.activationPotential")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			send_requests()
			print str(x) + "潜能激活完毕"
		del_dict_argv("method","teamId")

	elif press == "15":
		add_dict_argv(method="Tools.resetBoss")
		send_requests()
		del_dict_argv("method")

	elif press == "16":
		add_dict_argv(method="Hero.combineSpellBook")
		for x in other_config.skillId:
			add_dict_argv(sid=x)
			send_requests()
		del_dict_argv("method","sid")

		add_dict_argv(method="Hero.upLevelSpellBook")
		for x in other_config.skillId:
			add_dict_argv(sid=x)
			for y in range(5):
				send_requests()
		del_dict_argv("method","sid")

	elif press == "17":
		add_dict_argv(method="Team.upgradeStageTeam")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			for y in range(13):
				send_requests()
		del_dict_argv("method","teamId")
	
	elif press == "18":
		add_dict_argv(method="Tools.clearYac",actDev="0")
		send_requests()
		del_dict_argv("method","actDev")

	elif press == "19":
		add_dict_argv(method="Tools.addRes",type="starfrag",num="99999999")
		send_requests()
		del_dict_argv("method","type","num")

		add_dict_argv(method="Treasure.upStar",num="10")
		for x in other_config.baowu:
			strx = x
			add_dict_argv(disId=x, comId=str(strx)[2:4])
			for y in range(50):
				send_requests()
		del_dict_argv("method","num","disId","comId")
	else:
		os.exit()