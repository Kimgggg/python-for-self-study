#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
from selenium import webdriver
import selenium
import time
import fuck_gbk

user_rid = raw_input("please input rid:\n")
bingtuanId = [101,102,103,104,105,106,107,201,202,203,204,205,206,207,301,302,303,304,305,306,307,401,402,403,404,405,406,407,501,502,503,504,505,506,507,601,602,603,604,605,606,607,901,902,903,904,905,906,907]
potentialId = [1,2,3]
resource = ['gem','gold','texp','physcal']
stageId = ["7102215","7202205"]
bingtuansuipianId = "3101,3102,3103,3104,3105,3106,3107,3201,3202,3203,3204,3205,3206,3207,3301,3302,3303,3304,3305,3306,3307,3401,3402,3403,3404,3405,3406,3407,3501,3502,3503,3504,3505,3506,3507,3601,3602,3603,3604,3605,3606,3607,3901,3902,3903,3904,3905,3906,3907"
jinjiecailiaoId = "301101,301102,301103,301104,301105,301106,301201,301202,301203,301204,301205,301206,301301,301302,301303,301304,301305,301306,301307,301401,301402,301403,301404,301405,301406,301407,301501,301502,301503,301504,301505,301506,301507,301601,301602,301603,301604,301605,301606,301607,301701,301702,301703,301704,301705,301706,301707,301801,301802,301803,301804,301805,301806,301807,301901,301902,301903,301904,301905,301906,301907,302001,302002,302003,302004,302005,302006,302007,302101,302102,302103,302104,302105,302106,302107,302201,302202,302203,302204,302205,302206,302207,302301,302302,302303,302304,302305,302306,302307,302401,302402,302403,302404,302405,302406,302407"
herosuipianId = "360001,360101,360102,360103,360301,360302,360303,360401,360502,360601,360602,360603,360604,360701,360802,360901,361201,361202"
baowustr = "40111,40112,40113,40121,40122,40123,40211,40212,40213,40221,40222,40223,40231,40232,40233,40301,40302,40303,40304,40311,40312,40313,40314,40101,40102,40103,40321,40322,40323,40421,40422,40423,40424,40401,40402,40403,40404,40405,40406"
baowu = [40111,40112,40113,40121,40122,40123,40211,40212,40213,40221,40222,40223,40231,40232,40233,40301,40302,40303,40304,40311,40312,40313,40314,40101,40102,40103,40321,40322,40323,40421,40422,40423,40424,40401,40402,40403,40404,40405,40406]
otheritem = "41001,41002,3026,3027,3028,3029,3030,3036,3037,3038,3039,3040,3043,3044,3045,3046,3047,3048"
heroId = [60001,60101,60102,60103,60301,60302,60303,60401,60502,60601,60602,60603,60604,60701,60802,60901,61201,61202]
skillposition = [1,2,3,4]
bingtuanId1star = [101,102,105,106,301,401,403,501,601,901]
bingtuanId2star = [104,201,202,203,204,302,402,404,502,504,506,602,603,902,903]
bingtuanId3star = [103,107,205,206,207,303,304,305,306,307,405,406,407,503,505,507,604,605,606,607,904,905,906,907]

def translate_xpath(xpath):
	xpath = xpath.replace('"',"'")
	return driver.find_element_by_xpath(xpath)


while True:
	print """
	1.添加金币、钻石、兵团经验
	2.玩家升级
	3.设置vip等级
	4.提升全部兵团潜力
	5.调整副本进度
	6.发全部材料
	7.全部宝物进阶
	8.发放全部英雄
	9.全部英雄升星
	10.全部英雄技能升级
	11.发放全部兵团
	12.全部兵团升级 +全部兵团装备升级

	14.全部兵团升星+激活潜能
	"""
	press = raw_input("select:")
	if press == "1":
		num = input("please input num:")
		# 添加金币、钻石、兵团经验
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		translate_xpath('//*[@id="l580"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		for x in resource:
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="type"]').clear() #清空资源类型
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="type"]').send_keys(x) #输入资源类型
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="num"]').clear() #清空数量
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="num"]').send_keys(num) #输入数量
			print "已添加" + str(x)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click() #点击
		num = 0
		time.sleep(1)
		driver.quit()
	elif press == "2":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		#玩家升级
		translate_xpath('//*[@id="l584"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="level"]').send_keys("89")
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click
		print "玩家等级提升成功"
		time.sleep(10)
		driver.quit()
	elif press == "3":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		#设置vip等级
		translate_xpath('//*[@id="l581"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="level"]').send_keys("15")
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
		print "vip等级调整为15"
		time.sleep(1)
		driver.quit()
	elif press == "4":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		#提升潜力
		translate_xpath("//*[@id='l571']").click()
		time.sleep(1)
		translate_xpath("//*[@id='req']/form/table/tbody/tr[1]/td[2]//*[@name='rid']").send_keys(user_rid)
		for x in bingtuanId:
			translate_xpath("//*[@id='req']/form/table/tbody/tr[2]/td[2]//*[@name='teamId']").clear() #清空兵团id
			translate_xpath("//*[@id='req']/form/table/tbody/tr[2]/td[2]//*[@name='teamId']").send_keys(x) #输入兵团id
			for y in potentialId:
				translate_xpath("//*[@id='req']/form/table/tbody/tr[3]/td[2]//*[@name='potentialId']").clear() #清空潜力类型
				translate_xpath("//*[@id='req']/form/table/tbody/tr[3]/td[2]//*[@name='potentialId']").send_keys(y) #输入潜力类型
				for z in range(41):
					print "第" + str(z) + "次升级" + str(x) + "的" + str(y) + "潜力"
					translate_xpath("//*[@id='req']/form/table/tbody/tr[4]/td[2]//*[@name='uploadFrom']").click() #点击
		time.sleep(1)
		driver.quit()
	elif press == "5":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		#调整副本进度
		translate_xpath('//*[@id="l607"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		for x in stageId:
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="stageId"]').clear() #清空副本进度
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="stageId"]').send_keys(x) #输入副本id
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click() #点击
			print "调整关卡为" + x
		time.sleep(1)
		driver.quit()
	elif press == "6":
		num = input("please input num:")
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		#发材料
		translate_xpath('//*[@id="l582"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys(bingtuansuipianId) 
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="goodsNum"]').send_keys(num) #输入数量，需注意，后续添加时数量不会更新,不能被注释
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click() #点击
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').clear() #清空类型
		print "发放兵团碎片成功"
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys(jinjiecailiaoId)
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').clear()
		print "发放进阶材料成功"
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys(herosuipianId)
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').clear()
		print "发放英雄碎片成功"
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys(baowustr)
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').clear()
		print "发放宝物成功"

		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys(otheritem)
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').clear()
		print "发放杂物成功"
		num = 0
		time.sleep(1)
		driver.quit()
	elif press == "7":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		#宝物进阶
		translate_xpath('//*[@id="l582"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys("41001")#额外发送材料
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="goodsNum"]').send_keys("999999")
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
		translate_xpath('//*[@id="l749"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		big_id = []
		for Treasure_small_temp in baowu:
			Treasure_small = Treasure_small_temp#取大小ID
			Treasure_big_temp = str(Treasure_small_temp)[2:4]
			Treasure_big = int(Treasure_big_temp)
			big_id.append(Treasure_big)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="comId"]').clear() #散件宝物大id
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="comId"]').send_keys(Treasure_big)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="disId"]').clear()#散件宝物小id
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="disId"]').send_keys(Treasure_small)
			for count in range(23):
				translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
				print "宝物" + str(Treasure_small_temp) + "第" + str(count) + "次进阶"
		big_id = list(set(big_id))
		big_id.sort()
		translate_xpath('//*[@id="l748"]').click()#开始进阶整件宝物
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		for x in big_id:
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="comId"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="comId"]').send_keys(x)
			for y in range(23):
				translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
				print "宝物" + str(x) + "进阶" + str(y) + "次"
		time.sleep(1)
		driver.quit()
	elif press == "8":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		# 发放英雄
		translate_xpath('//*[@id="l586"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		for x in heroId:
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="heroId"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="heroId"]').send_keys(x)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
			print "发放英雄" + str(x) + "成功"
		time.sleep(1)
		driver.quit()
	elif press == "9":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		#英雄升星
		translate_xpath('//*[@id="l315"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		for x in heroId:
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="heroId"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="heroId"]').send_keys(x)
			for y in range(4):
				translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
				print "英雄" + str(x) + "升星第" + str(y) + "次"
		time.sleep(1)
		driver.quit()
	elif press == "10":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		#英雄技能升级
		translate_xpath('//*[@id="l582"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys("3004")#额外发送材料
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="goodsNum"]').send_keys("9999999")
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()

		translate_xpath('//*[@id="l313"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="exMode"]').send_keys("1")#是否十连突
		for hero in heroId:
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="heroId"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="heroId"]').send_keys(hero)#输入英雄id
			for skill_position in skillposition:
				translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="positionId"]').clear()
				translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="positionId"]').send_keys(skill_position)#输入技能位置
				for x in range(30):
					translate_xpath('//*[@id="req"]/form/table/tbody/tr[5]/td[2]//*[@name="uploadFrom"]').click()
					print "英雄" + str(hero) + "技能" + str(skill_position) + "第" + str(x) + "次十连突"
		time.sleep(1)
		driver.quit()
	elif press == "11":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		#发放兵团
		translate_xpath('//*[@id="l583"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		for x in bingtuanId:
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(x)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
			print "已发放兵团" + str(x)
		driver.quit()
	elif press == "12":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		#所有兵团升级
		translate_xpath('//*[@id="l561"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="level"]').send_keys("90")#要提升的等级
		for x in bingtuanId:
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(x)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
			print "兵团" + str(x) + "已升级"
		time.sleep(0.5)
		driver.refresh()
		time.sleep(1)
		#所有兵团装备升级
		translate_xpath('//*[@id="l563"]').click()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		for x in bingtuanId:
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(x)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
			print "兵团" + str(x) + "装备已升级"
		driver.quit()

	elif press == "13":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)






	elif press == "14":
		driver = webdriver.Firefox()
		driver.get("http://192.168.5.207:8001/demo/ctrl.php")
		time.sleep(1)
		#所有兵团升星+激活潜能
		def bigStar(argv_id):
			driver.refresh()
			time.sleep(1)
			translate_xpath('//*[@id="l567"]').click()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(argv_id)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
			print "大星" + str(argv_id)
			time.sleep(0.5)
		def smallStar(argv_id):
			driver.refresh()
			time.sleep(1)
			translate_xpath('//*[@id="l566"]').click()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(argv_id)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="batch"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="batch"]').send_keys("1")
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
			time.sleep(0.5)
		for x in range(1):
			for y in bingtuanId1star:
				smallStar(y)
				bigStar(y)
		new_bingtuansuipian2star = bingtuanId1star + bingtuanId2star
		print "全部1星兵团已升至2星"
		for x in range(1):
			for y in new_bingtuansuipian2star:
				smallStar(y)
				bigStar(y)
		new_bingtuansuipian3star = new_bingtuansuipian2star + bingtuanId3star
		print "全部1星兵团与2星兵团已全部3星"
		for x in range(3):
			print "第" + str((x+1)) + "次集体升星"
			for y in new_bingtuansuipian3star:
				smallStar(y)
				bigStar(y)
		driver.refresh()
		time.sleep(1)
		translate_xpath('//*[@id="l570"]').click()	
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
		translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
		for z in bingtuanId:
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(z)
			translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
			print "兵团" + str(z) + "激活潜能"
		driver.quit()























		