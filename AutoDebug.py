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

def Alzheimer_disease(select_number):
	print select_number + " done"

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

def temp_sendItems(itemsId):
	add_dict_argv(method="Tools.sendItems",goodsId=itemsId,goodsNum="9999999")
	try_send_requests()
	del_dict_argv("method","goodsId","goodsNum")

def temp_addRes(*Restype):
	for x in Restype:
		add_dict_argv(method="Tools.addRes",num="9999999",type=Restype)
		if (Restype == "gold") or (Restype == "texp"):
			add_dict_argv(num="9999999999")
		try_send_requests()
		del_dict_argv("method","num","type")

def try_send_requests():
	try:
		send_requests()
	except Exception as e:
		print e

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
elif dev_server == "4" or dev_server == "5":
	add_dict_argv(pGroup="aqq")
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
    7.全部宝物进阶+升星
    8.发放全部英雄
    9.英雄升星+开启法术槽
    10.全部英雄技能升级+随机刷新5次专精
    11.发放全部兵团
    12.所有兵团升级+所有兵团装备升级+所有兵团装备进阶
    13.更换user_rid与服务器
    14.所有兵团升星+激活潜能+解锁技能+技能升级
    15.重置pve玩法次数星下下
    16.法术激活升级
    17.图鉴解锁+图鉴升级
    18.清除yac
    19.英雄天赋升级
    20.清空背包
    21.直接觉醒兵团+觉醒强化
    22.全部兵团指定次数随机增加兵团天赋
    24.抽卡测试
    q.退出
    """

	press = raw_input("select:")
	if press == "1":
		#发送资源
		add_dict_argv(method="Tools.addRes",num=raw_input("please input resource number:\n"))
		print '''
		1.全部
		2.钻石
		3.金币
		4.体力
		5.兵团经验
		'''
		select_type = raw_input("please input type_num:\n")
		if select_type == "1":
			for x in other_config.resource:
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
		del_dict_argv("num","type","method")
		Alzheimer_disease(press)
			
	elif press == "2":
		add_dict_argv(method="Tools.upgradeLevel", level=raw_input("please input level number:\n"))
		try_send_requests()
		print "等级调整完毕"
		del_dict_argv("method","level")
		Alzheimer_disease(press)

	elif press == "3":
		add_dict_argv(method="Tools.setVipLevel",level=raw_input("please input level number:\n"))
		try_send_requests()
		print "vip等级调整完毕"
		del_dict_argv("method","level")
		Alzheimer_disease(press)

	elif press == "4":
		temp_addRes("gold")
		add_dict_argv(method="Team.upPotential")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			for y in other_config.potentialId:
				add_dict_argv(potentialId=y)
				for z in range(41):
					try_send_requests()
					print "兵团" + str(x) + "潜能" + str(y) + "第" + str(z) + "次提升"
		del_dict_argv("method","teamId","potentialId")
		Alzheimer_disease(press)

	elif press == "5":
		add_dict_argv(method="Tools.batchPassStage")
		for x in other_config.stageId:
			add_dict_argv(stageId=x)
			try_send_requests()
			print "关卡已调整至" + x
		del_dict_argv("method","stageId")
		Alzheimer_disease(press)

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
			try_send_requests()
			print "全部物品发送成功"
		elif select_type == "2":
			add_dict_argv(goodsId=other_config.bingtuansuipianId)	
			try_send_requests()
			print "发放兵团碎片成功"
		elif select_type == "3":
			add_dict_argv(goodsId=other_config.jinjiecailiaoId)
			try_send_requests()
			print "发放进阶材料成功"
		elif select_type == "4":
			add_dict_argv(goodsId=other_config.herosuipianId)
			try_send_requests()
			print "发放英雄碎片成功"
		elif select_type == "5":
			add_dict_argv(goodsId=other_config.baowustr)
			try_send_requests()
			print "发放宝物成功"
		elif select_type == "6":
			add_dict_argv(goodsId=other_config.otheritem)
			try_send_requests()
			print "发放杂物成功"
		elif select_type == "7":
			add_dict_argv(goodsId=other_config.fashusuipian)
			try_send_requests()
			print "发放法术碎片成功"
		del_dict_argv("goodsNum","goodsId","method")
		Alzheimer_disease(press)

	elif press == "7":
		for x in other_config.baowu:
			add_dict_argv(method="Treasure.wearDisTreasure",disId=x,comId=str(x)[2:4],positionId=str(x)[-1])
			try_send_requests()
			print str(x) + "已装备"
			del_dict_argv("method","disId","comId","positionId")

		for x in other_config.baowu:
			add_dict_argv(method="Treasure.activationComTreasure",comId=str(x)[2:4])
			try_send_requests()
			print str(x) + "已激活组合宝物"
			del_dict_argv("method","comId")

		temp_sendItems("41001")

		add_dict_argv(method="Treasure.promoteDisTreasure")
		for x in other_config.baowu:
			add_dict_argv(disId=x, comId=str(x)[2:4])
			for y in range(21):
				try_send_requests()
				print "第" + str(y) + "次进阶" + str(x)
		del_dict_argv("method","disId","comId")

		temp_addRes("starfrag")

		add_dict_argv(method="Treasure.upStar",num="10")
		for x in other_config.baowu:
			add_dict_argv(disId=x, comId=str(x)[2:4])
			for y in range(50):
				try_send_requests()
				print str(x) + "第" + str(y) + "次升星"
		del_dict_argv("method","num","disId","comId")

		add_dict_argv(method="Treasure.promoteComTreasure")
		for x in other_config.baowu:
			add_dict_argv(comId=str(x)[2:4])
			for y in range(21):
				try_send_requests()
				print "组合宝物" + str(x)[2:4] + "第" + str(y) + "次进阶"
		del_dict_argv("method","comId")
		Alzheimer_disease(press)
				
	elif press == "8":
		add_dict_argv(method="Tools.sendHero")
		for x in other_config.heroId:
			add_dict_argv(heroId=x)
			try_send_requests()
			print "已发送" + str(x)
		del_dict_argv("method","heroId")
		Alzheimer_disease(press)
	elif press == "9":
		add_dict_argv(method="Hero.upgradeStar")
		for x in other_config.heroId:
			add_dict_argv(heroId=x)
			for y in range(4):
				try_send_requests()
				print "英雄" + str(x) + "第" + str(y) + "次升星"
		del_dict_argv("method","heroId")

		add_dict_argv(method="Hero.initHeroSlot")
		for x in other_config.heroId:
			add_dict_argv(heroId=x)
			try_send_requests()
			print "英雄" + str(x) + "已激活刻印孔"
		del_dict_argv("method","heroId")
		Alzheimer_disease(press)

	elif press == "10":
		def refreshMastery(list_name):
			for x in list_name:
				add_dict_argv(method="Hero.refreshMastery",args='{"reduceType":0,"locks":{},"refreshNum":1}',heroId=x)
				try_send_requests()
				del_dict_argv("method","args","heroId")

				add_dict_argv(method="Hero.saveMastery",index="1",heroId=x)
				try_send_requests()
				print "英雄" + str(x) + "随机刷新专精成功"
				del_dict_argv("method","index","heroId")

		add_dict_argv(method="Hero.heroSkillUpgrade",exMode="1")
		for x in other_config.heroId:
			add_dict_argv(heroId=x)
			for y in other_config.skillposition:
				add_dict_argv(positionId=y)
				for z in range(22):
					try_send_requests()
					print "第" + str(z) + "次升级" + str(x) + " " + str(y) + "技能" 
		del_dict_argv("method","exMode","heroId","positionId")
		for x in range(5):
			refreshMastery(other_config.heroId)
		Alzheimer_disease(press)

	elif press == "11":
		add_dict_argv(method="Tools.createTeam")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			try_send_requests()
			print "已发放" + str(x)
		del_dict_argv("method","teamId")
		Alzheimer_disease(press)

	elif press == "12":
		temp_addRes("gold","texp")
		add_dict_argv(method="Team.upgradeTeam",level="90")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			try_send_requests()
			print "兵团" + str(x) + "已升级"
		del_dict_argv("method","level","teamId")

		add_dict_argv(method="Team.batchUpgradeEquip")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			try_send_requests()
			print "兵团" + str(x) + "装备已升级"
		del_dict_argv("method","teamId")

		add_dict_argv(method="Team.upgradeStageEquip")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			for y in other_config.skillposition:
				add_dict_argv(positionId=y)
				for z in range(14):
					try_send_requests()
					print "兵团" + str(x) + "装备" + str(y) + "正在第" + str(z) + "次升阶"
		del_dict_argv("method","teamId","positionId")

		add_dict_argv(method="Team.upgradeStageTeam")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			for y in range(13):
				try_send_requests()
				print "兵团" + str(x) + "第" + str(y) + "次进阶"
		del_dict_argv("method","teamId")
		Alzheimer_disease(press)
	
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
		elif dev_server == "4" or dev_server == "5":
			add_dict_argv(pGroup="aqq")
		else:
			add_dict_argv(pGroup="default")
		dev_server = other_config.debug_server_requests[int(dev_server) - 1]
		add_dict_argv(rid=user_rid, sec=user_rid[:4])
		Alzheimer_disease(press)

	elif press == "14":
		def update_small_star(list_name):
			add_dict_argv(method="Team.upgradeStar",batch="1")
			for x in list_name:
				add_dict_argv(teamId=x)
				try_send_requests()
				print "兵团" + str(x) + "小星升星完毕"
			del_dict_argv("method","batch","teamId")

		def update_big_star(list_name):
			add_dict_argv(method="Team.upgradeMaxStar")
			for x in list_name:
				add_dict_argv(teamId=x)
				try_send_requests()
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
			try_send_requests()
			print str(x) + "潜能激活完毕"
		del_dict_argv("method","teamId")

		add_dict_argv(method="Team.openSkill")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			for y in other_config.skillposition:
				add_dict_argv(positionId=y)
				try_send_requests()
				print str(x) + "已激活" + str(y) + "技能"
		del_dict_argv("method","teamId","positionId")

		temp_sendItems("3025")

		add_dict_argv(method="Team.upgradeSkill",args="{\"items\":[[3025,100]]}")
		for x in other_config.bingtuanId:
			add_dict_argv(teamId=x)
			for y in other_config.skillposition:
				add_dict_argv(positionId=y)
				try_send_requests()
				print str(x) + "技能" + str(y) + "已升级"
		del_dict_argv("method","args","teamId","positionId")
		Alzheimer_disease(press)


	elif press == "15":
		add_dict_argv(method="Tools.resetBoss")
		try_send_requests()
		print "pve次数清空完毕"
		del_dict_argv("method")
		Alzheimer_disease(press)

	elif press == "16":
		add_dict_argv(method="Hero.combineSpellBook")
		for x in other_config.skillId:
			add_dict_argv(sid=x)
			try_send_requests()
			print str(x) + "激活成功"
		del_dict_argv("method","sid")
		Alzheimer_disease(press)

		add_dict_argv(method="Hero.upLevelSpellBook")
		for x in other_config.skillId:
			add_dict_argv(sid=x)
			for y in range(5):
				try_send_requests()
				print str(x) + "第" + str(y) + "升级成功"
		del_dict_argv("method","sid")
		Alzheimer_disease(press)

	elif press == "17":
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

	elif press == "18":
		add_dict_argv(method="Tools.clearYac",actDev="0")
		try_send_requests()
		print "debug yac清除成功"
		del_dict_argv("method","actDev")
		Alzheimer_disease(press)

	elif press == "19":
		temp_addRes("starNum")

		add_dict_argv(method="Talent.upTalentChildLv")
		for x in other_config.magicTalent:
			add_dict_argv(tid=x,kind=str(x)[:2])
			for y in range(10):
				try_send_requests()
				print "天赋" + str(x) + "第" + str(y) + "次升级"
		del_dict_argv("method","tid","kind")
		Alzheimer_disease(press)

	elif press == "20":
		add_dict_argv(method="Tools.clearUserData",type="4")
		try_send_requests()
		print "清空背包成功"
		del_dict_argv("method","type")
		Alzheimer_disease(press)

	elif press == "21":
		add_dict_argv(method="Tools.activateAwaking")
		for x in other_config.activateAwaking:
			add_dict_argv(teamId=x)
			try_send_requests()
			print "兵团" + str(x) + "已觉醒"
		del_dict_argv("method","teamId")

		for x in other_config.activateAwaking:
			temp_sendItems("94"+str(x))

		for x in other_config.activateAwaking:
			add_dict_argv(method="Awaking.upAwakingLevel",teamId=x)
			for y in range(7):
				try_send_requests()
				print "兵团" + str(x) + "第" + str(y) + "次觉醒强化"	
		del_dict_argv("method","teamId")
		Alzheimer_disease(press)

	elif press == "22":
		def trainTalent_and_saveTalent(list_name):
			for x in list_name:
				add_dict_argv(method="Team.trainTalent",type="2",num="10",teamId=x)
				try_send_requests()
				del_dict_argv("method","type","num","teamId")

				add_dict_argv(method="Team.saveTalent",tId="[1,2,3,4,5,6,7,8,9,10]",teamId=x)
				try_send_requests()
				print "兵团" + str(x) + "已保存天赋"
				del_dict_argv("method","tId","teamId")

		temp_sendItems("3044,3045,3046,3047,3048")

		for x in range(input("please input times:\n")):
			trainTalent_and_saveTalent(other_config.bingtuanId)
		Alzheimer_disease(press)

	elif press == "23":
		# 需要判断userid后选择对应服务器的id的csv,当前写死为7服
		add_dict_argv(method="Tools.autoKeyCopy",rids=user_rid,rid="8001_884")
		try_send_requests()
		del_dict_argv("method","rids","rid")
		add_dict_argv(rid=user_rid)
		Alzheimer_disease(press)

	elif press == "24":
		print "清空背包中...."
		add_dict_argv(method="Tools.clearUserData",type="4")
		try_send_requests()
		del_dict_argv("method","type")
		print "背包清空完毕，请输入抽取次数并选择类型"
		number = input("please input number:\n")

		print '''
		1.祭坛抽卡钻石10连抽
		2.祭坛抽卡钻石单抽
		3.祭坛抽卡钥匙10连抽
		4.祭坛抽卡钥匙单抽
		5.法术祈愿钻石10连抽
		6.法术祈愿钻石单抽
		7.法术祈愿卷轴10连抽
		8.法术祈愿卷轴单抽
		9.宝物5连抽
		10.宝物单抽
		'''
		select_type = raw_input("please select num:\n")
		if select_type == "1":
			add_dict_argv(method="Tools.addRes",num=str(number * 2700),type="gem")
			try_send_requests()
			del_dict_argv("method","num","type")

			add_dict_argv(method="Team.drawAward",num="10",typeId="2")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","typeId")
			Alzheimer_disease(press)
		elif select_type == "2":
			add_dict_argv(method="Tools.addRes",num=str(number * 300),type="gem")
			try_send_requests()
			del_dict_argv("method","num","type")

			add_dict_argv(method="Team.drawAward",num="1",typeId="2")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","typeId")
			Alzheimer_disease(press)
		elif select_type == "3":
			add_dict_argv(method="Tools.sendItems",goodsId="3001",goodsNum=str(number * 10))
			try_send_requests()
			del_dict_argv("method","goodsId","goodsNum")

			add_dict_argv(method="Team.drawAward",num="10",typeId="1")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","typeId")
			Alzheimer_disease(press)
		elif select_type == "4":
			add_dict_argv(method="Tools.sendItems",goodsId="3001",goodsNum=str(number))
			try_send_requests()
			del_dict_argv("method","goodsId","goodsNum")

			add_dict_argv(method="Team.drawAward",num="1",typeId="1")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","typeId")
			Alzheimer_disease(press)
		elif select_type == "5":
			add_dict_argv(method="Tools.addRes",num=str(number * 880),type="gem")
			try_send_requests()
			del_dict_argv("method","num","type")

			add_dict_argv(method="Hero.drawSpeelBook",num="10",type="2")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","type")
			Alzheimer_disease(press)
		elif select_type == "6":
			add_dict_argv(method="Tools.addRes",num=str(number * 100),type="gem")
			try_send_requests()
			del_dict_argv("method","num","type")

			add_dict_argv(method="Hero.drawSpeelBook",num="1",type="2")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","type")
			Alzheimer_disease(press)
		elif select_type == "7":
			add_dict_argv(method="Tools.sendItems",goodsId="40005",goodsNum=str(number * 10))
			try_send_requests()
			del_dict_argv("method","goodsId","goodsNum")

			add_dict_argv(method="Hero.drawSpeelBook",num="10",type="1")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","type")
			Alzheimer_disease(press)
		elif select_type == "8":
			add_dict_argv(method="Tools.sendItems",goodsId="40005",goodsNum=str(number))
			try_send_requests()
			del_dict_argv("method","goodsId","goodsNum")

			add_dict_argv(method="Hero.drawSpeelBook",num="1",type="1")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num","type")
			Alzheimer_disease(press)
		elif select_type == "9":
			add_dict_argv(method="Tools.addRes",num=str(number * 880),type="gem")
			try_send_requests()
			del_dict_argv("method","num","type")

			add_dict_argv(method="Treasure.drewDisTreasure",num="5")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num")
			Alzheimer_disease(press)
		elif select_type == "10":
			add_dict_argv(method="Tools.addRes",num=str(number * 200),type="gem")
			try_send_requests()
			del_dict_argv("method","num","type")

			add_dict_argv(method="Treasure.drewDisTreasure",num="1")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num")
			Alzheimer_disease(press)

	elif press == "test":
		pass

	else:
		os.exit()