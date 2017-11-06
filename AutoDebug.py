#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
from collections import OrderedDict
import requests
import other_config
import other_config_taiwan
import os
import sys
import random
import debug_menu

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

def Alzheimer_disease(select_number):
	print select_number + " done"
	print "user_rid : %s,\ndev_select : %s,\ndev_server : %s,\n" %(user_rid,dev_select,dev_server)

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
		# print "返回信息>>>>>>>>>>>>>>>>>>>\n" + r.text + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
		pass

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
		send_requests()
	except Exception as e:
		print e

user_rid = raw_input("输入rid:\n".decode('utf-8').encode('gbk'))
debug_menu.server_menu()
dev_select = raw_input("选择服务器:\n".decode('utf-8').encode('gbk'))
if dev_select == "6" or dev_select == "8":
	add_dict_argv(pGroup="test")
	PLATFROM = other_config_taiwan
elif dev_select == "4" or dev_select == "5" or dev_select == "7":
	add_dict_argv(pGroup="aqq")
	PLATFROM = other_config
else:
	add_dict_argv(pGroup="default")
	PLATFROM = other_config
dev_server = PLATFROM.debug_server_requests[int(dev_select) - 1]
add_dict_argv(rid=user_rid, sec=user_rid[:4])

while True:
	debug_menu.main_menu()

	press = raw_input("select:")
	if press == "1":
		#发送资源
		add_dict_argv(method="Tools.addRes",num=raw_input("输入资源数量:\n".decode('utf-8').encode('gbk')))
		debug_menu.res_menu()
		select_type = raw_input("选择资源类型:\n".decode('utf-8').encode('gbk'))
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
		potentialId = [1,2,3]
		temp_addRes("gold",999999999)
		add_dict_argv(method="Team.upPotential")
		for x in PLATFROM.bingtuanId:
			add_dict_argv(teamId=x)
			for y in potentialId:
				add_dict_argv(potentialId=y)
				for z in range(40):
					try_send_requests()
					print "兵团" + str(x) + "潜能" + str(y) + "第" + str(z) + "次提升"
		del_dict_argv("method","teamId","potentialId")
		Alzheimer_disease(press)

	elif press == "5":
		temp_stageId = ["710","720"]
		print "第15章第5小关 则输入 1505\n"
		stage = raw_input("请输入关卡id:\n".decode('utf-8').encode('gbk'))
		if int(stage[-2:]) > 15 or int(stage[:2]) > 26:
			print "关卡id输入错误"
		else:
			add_dict_argv(method="Tools.batchPassStage",stageId=(temp_stageId[0] + stage))
			# print temp_stageId[0] + stage
			try_send_requests()
			add_dict_argv(stageId=temp_stageId[1] + str((int(stage[:2]) - 1)) + "05")
			# print str(temp_stageId[1] + str((int(stage[:2]) - 1)) + "05")
			try_send_requests()
			del_dict_argv("method","stageId")
			Alzheimer_disease(press)

	elif press == "6":
		add_dict_argv(goodsNum=raw_input("输入道具数量:\n".decode('utf-8').encode('gbk')), method="Tools.sendItems")
		new_list = 	PLATFROM.bingtuansuipianId + "," + PLATFROM.jinjiecailiaoId + "," + PLATFROM.herosuipianId + "," + PLATFROM.baowustr + "," + PLATFROM.otheritem + "," + PLATFROM.fashusuipian
		debug_menu.item_menu()
		select_type = raw_input("选择道具类型:\n".decode('utf-8').encode('gbk'))
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
		del_dict_argv("goodsNum","goodsId","method")
		Alzheimer_disease(press)

	elif press == "7":
		for x in PLATFROM.baowu:
			add_dict_argv(method="Treasure.wearDisTreasure",disId=x,comId=str(x)[2:4],positionId=str(x)[-1])
			try_send_requests()
			print str(x) + "已装备"
			del_dict_argv("method","disId","comId","positionId")

		for x in PLATFROM.baowu:
			add_dict_argv(method="Treasure.activationComTreasure",comId=str(x)[2:4])
			try_send_requests()
			print str(x) + "已激活组合宝物"
			del_dict_argv("method","comId")

		temp_sendItems("41001",9999999)

		temp_addRes("gold",999999999)
		add_dict_argv(method="Treasure.promoteDisTreasure")
		for x in PLATFROM.baowu:
			add_dict_argv(disId=x, comId=str(x)[2:4])
			for y in range(21):
				try_send_requests()
				print "第" + str(y) + "次进阶" + str(x)
		del_dict_argv("method","disId","comId")

		temp_addRes("starfrag",9999999)
		temp_addRes("gold",999999999)
		add_dict_argv(method="Treasure.upStar",num="10")
		for x in PLATFROM.baowu:
			add_dict_argv(disId=x, comId=str(x)[2:4])
			for y in range(50):
				try_send_requests()
				print str(x) + "第" + str(y) + "次升星"
		del_dict_argv("method","num","disId","comId")

		temp_addRes("gold",999999999)
		add_dict_argv(method="Treasure.promoteComTreasure")
		for x in PLATFROM.baowu:
			add_dict_argv(comId=str(x)[2:4])
			for y in range(21):
				try_send_requests()
				print "组合宝物" + str(x)[2:4] + "第" + str(y) + "次进阶"
		del_dict_argv("method","comId")
		Alzheimer_disease(press)
				
	elif press == "8":
		add_dict_argv(method="Tools.sendHero")
		for x in PLATFROM.heroId:
			add_dict_argv(heroId=x)
			try_send_requests()
			print "已发送" + str(x)
		del_dict_argv("method","heroId")
		Alzheimer_disease(press)

	elif press == "9":
		add_dict_argv(method="Hero.upgradeStar")
		for x in PLATFROM.heroId:
			add_dict_argv(heroId=x)
			for y in range(4):
				try_send_requests()
				print "英雄" + str(x) + "第" + str(y) + "次升星"
		del_dict_argv("method","heroId")

		add_dict_argv(method="Hero.initHeroSlot")
		for x in PLATFROM.heroId:
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

		temp_sendItems("3004",5000000)
		add_dict_argv(method="Hero.heroSkillUpgrade",exMode="1")
		for x in PLATFROM.heroId:
			add_dict_argv(heroId=x)
			for y in PLATFROM.skillposition:
				add_dict_argv(positionId=y)
				for z in range(22):
					try_send_requests()
					print "第" + str(z) + "次升级" + str(x) + " " + str(y) + "技能" 
		del_dict_argv("method","exMode","heroId","positionId")
		for x in range(5):
			refreshMastery(PLATFROM.heroId)
		Alzheimer_disease(press)

	elif press == "11":
		add_dict_argv(method="Tools.createTeam")
		for x in PLATFROM.bingtuanId:
			add_dict_argv(teamId=x)
			try_send_requests()
			print "已发放" + str(x)
		del_dict_argv("method","teamId")
		Alzheimer_disease(press)

	elif press == "12":

		temp_addRes("texp",999999999)
		add_dict_argv(method="Team.upgradeTeam",level="90")
		for x in PLATFROM.bingtuanId:
			add_dict_argv(teamId=x)
			try_send_requests()
			print "兵团" + str(x) + "已升级"
		del_dict_argv("method","level","teamId")

		temp_addRes("gold",999999999)
		temp_addRes("gold",999999999)
		add_dict_argv(method="Team.batchUpgradeEquip")
		for x in PLATFROM.bingtuanId:
			add_dict_argv(teamId=x)
			try_send_requests()
			print "兵团" + str(x) + "装备已升级"
		del_dict_argv("method","teamId")

		temp_addRes("gold",999999999)
		temp_addRes("gold",999999999)
		add_dict_argv(method="Team.upgradeStageEquip")
		for x in PLATFROM.bingtuanId:
			add_dict_argv(teamId=x)
			for y in PLATFROM.skillposition:
				add_dict_argv(positionId=y)
				for z in range(14):
					try_send_requests()
					print "兵团" + str(x) + "装备" + str(y) + "正在第" + str(z) + "次升阶"
		del_dict_argv("method","teamId","positionId")

		temp_addRes("gold",999999999)
		temp_addRes("gold",999999999)
		add_dict_argv(method="Team.upgradeStageTeam")
		for x in PLATFROM.bingtuanId:
			add_dict_argv(teamId=x)
			for y in range(13):
				try_send_requests()
				print "兵团" + str(x) + "第" + str(y) + "次进阶"
		del_dict_argv("method","teamId")
		Alzheimer_disease(press)
	
	elif press == "13":
		user_rid = raw_input("输入rid:\n".decode('utf-8').encode('gbk'))
		debug_menu.server_menu()
		dev_select = raw_input("选择服务器:\n".decode('utf-8').encode('gbk'))
		if dev_select == "6" or dev_select == "8":
			add_dict_argv(pGroup="test")
			PLATFROM = other_config_taiwan
		elif dev_select == "4" or dev_select == "5" or dev_select == "7":
			add_dict_argv(pGroup="aqq")
			PLATFROM = other_config
		else:
			add_dict_argv(pGroup="default")
			PLATFROM = other_config
		dev_server = PLATFROM.debug_server_requests[int(dev_select) - 1]
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


		temp_addRes("gold",999999999)
		update_small_star(PLATFROM.bingtuanId1star)
		update_big_star(PLATFROM.bingtuanId1star)
		new_bingtuansuipian2star = PLATFROM.bingtuanId1star + PLATFROM.bingtuanId2star
		update_small_star(new_bingtuansuipian2star)
		update_big_star(new_bingtuansuipian2star)
		temp_addRes("gold",999999999)
		new_bingtuansuipian3star = new_bingtuansuipian2star + PLATFROM.bingtuanId3star
		for x in range(3):
			update_small_star(new_bingtuansuipian3star)
			update_big_star(new_bingtuansuipian3star)

		add_dict_argv(method="Team.activationPotential")
		for x in PLATFROM.bingtuanId:
			add_dict_argv(teamId=x)
			try_send_requests()
			print str(x) + "潜能激活完毕"
		del_dict_argv("method","teamId")

		add_dict_argv(method="Team.openSkill")
		for x in PLATFROM.bingtuanId:
			add_dict_argv(teamId=x)
			for y in PLATFROM.skillposition:
				add_dict_argv(positionId=y)
				try_send_requests()
				print str(x) + "已激活" + str(y) + "技能"
		del_dict_argv("method","teamId","positionId")

		temp_sendItems("3025",5000000)

		add_dict_argv(method="Team.upgradeSkill",args="{\"items\":[[3025,100]]}")
		for x in PLATFROM.bingtuanId:
			add_dict_argv(teamId=x)
			for y in PLATFROM.skillposition:
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
		temp_addRes("starNum",200000)

		add_dict_argv(method="Talent.upTalentChildLv")
		for x in PLATFROM.magicTalent:
			add_dict_argv(tid=x,kind=str(x)[:2])
			for y in range(10):
				try_send_requests()
				print "天赋" + str(x) + "第" + str(y) + "次升级"
		del_dict_argv("method","tid","kind")
		Alzheimer_disease(press)

	elif press == "20":
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

	elif press == "21":
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

	elif press == "22":
		def trainTalent_and_saveTalent(list_name):
			for x in list_name:
				add_dict_argv(method="Team.trainTalent",type="2",num="10",teamId=x)
				try_send_requests()
				del_dict_argv("method","type","num","teamId")

				temp_list = [1,2,3,4,5,6,7,8,9,10]
				temp_tId = random.sample(temp_list,random.randint(4,7))
				temp_tId.sort()
				add_dict_argv(method="Team.saveTalent",tId=str(temp_tId),teamId=x)
				try_send_requests()
				print "兵团" + str(x) + "已保存天赋" + str(temp_tId)
				del_dict_argv("method","tId","teamId")

		temp_addRes("gem",99999999)
		temp_addRes("gold",999999999)
		temp_sendItems("3044,3045,3046,3047,3048",2000000)

		for x in range(input("输入循环次数:\n".decode('utf-8').encode('gbk'))):
			trainTalent_and_saveTalent(PLATFROM.bingtuanId)
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
		number = input("输入抽卡次数:\n".decode('utf-8').encode('gbk'))

		debug_menu.reward_menu()
		select_type = raw_input("选择抽卡类型:\n".decode('utf-8').encode('gbk'))
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
			add_dict_argv(method="Treasure.drewDisTreasure",num="5")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num")
			Alzheimer_disease(press)
		elif select_type == "10":
			temp_addRes("gem",number*200)
			add_dict_argv(method="Treasure.drewDisTreasure",num="1")
			for x in range(number):
				try_send_requests()
				print "第" + str(x) + "抽卡成功"
			del_dict_argv("method","num")
			Alzheimer_disease(press)

	elif press == "test":
		add_dict_argv(method="chat.sendMessage",message='{"typeCell":"all","text":"1111111"}',type="all")
		for x in range(10):
			try_send_requests()
		del_dict_argv("method","message")

	else:
		os.exit()

