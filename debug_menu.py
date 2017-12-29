#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import sys
from prettytable import PrettyTable

def main_menu():
	main_menu = PrettyTable(['id', "选项","id ","选项 "], encoding=sys.stdout.encoding)  
	main_menu.align["id"] = "c"
	main_menu.align["id "] = "c"# Left align city names
	main_menu.align["选项"] = "l"
	main_menu.align["选项 "] = "l"
	main_menu.padding_width = 1# One space between column edges and contents (default)
	main_menu.add_row(["1.","添加金币、钻石、兵团经验、体力","14.","英雄天赋升级"])  
	main_menu.add_row(["2.","玩家升级","15.","清空各类数据"])  
	main_menu.add_row(["3.","设置vip等级","16.","觉醒兵团+觉醒强化"])  
	main_menu.add_row(["4.","调整副本进度","17.","全部兵团指定次数随机增加兵团天赋"])  
	main_menu.add_row(["5.","发送道具","18.","抽卡测试"])  
	main_menu.add_row(["6.","宝物调整","19.","兵营建造+兵营升级(国内)"])  
	main_menu.add_row(["7.","发送全部英雄","20.","xxxxxxxxxxx"])
	main_menu.add_row(["8.","英雄调整","21.","xxxxxxxxxxx"])
	main_menu.add_row(["9.","发送全部兵团","22.","xxxxxxxxxx"])  
	main_menu.add_row(["10.","兵团调整","23.","xxxxxxxxxxxx"])  
	main_menu.add_row(["11.","更换user_rid与服务器","24.","xxxxxxxxxxx"])  
	main_menu.add_row(["12.","法术激活升级","25.","xxxxxxxxxxxxxxxxxxxx"])
	main_menu.add_row(["13.","图鉴解锁+图鉴升级","q.","退出"])
	print main_menu  

def server_menu():
	server_menu = PrettyTable(['id', "服务器列表"], encoding=sys.stdout.encoding)  
	server_menu.align["id"] = "c"# Left align city names
	server_menu.align["服务器列表"] = "l"
	server_menu.padding_width = 1# One space between column edges and contents (default)
	server_menu.add_row(["1.","开发机1"])  
	server_menu.add_row(["2.","开发机2"])  
	server_menu.add_row(["3.","开发机3"])  
	server_menu.add_row(["4.","dev3"])  
	server_menu.add_row(["5.","dev4"])  
	server_menu.add_row(["6.","台湾104"])
	server_menu.add_row(["7.","dev5"])
	server_menu.add_row(["8.","台湾105"])
	server_menu.add_row(["9.","棒子.58"])
	print server_menu  

def res_menu():
	res_menu = PrettyTable(['id', "资源类型"], encoding=sys.stdout.encoding)  
	res_menu.align["id"] = "c"# Left align city names
	res_menu.align["资源类型"] = "l"
	res_menu.padding_width = 1# One space between column edges and contents (default)
	res_menu.add_row(["1.","全部"])  
	res_menu.add_row(["2.","钻石"])  
	res_menu.add_row(["3.","金币"])  
	res_menu.add_row(["4.","体力"])  
	res_menu.add_row(["5.","兵团经验"])   
	res_menu.add_row(["6.","手动输入资源类型"])
	print res_menu 

def item_menu():
	item_menu = PrettyTable(['id', "道具列表"], encoding=sys.stdout.encoding)  
	item_menu.align["id"] = "c"# Left align city names
	item_menu.align["道具列表"] = "l"
	item_menu.padding_width = 1# One space between column edges and contents (default)
	item_menu.add_row(["1.","发送全部"])  
	item_menu.add_row(["2.","发送全部兵团碎片"])  
	item_menu.add_row(["3.","发送全部进阶材料"])  
	item_menu.add_row(["4.","发送全部英雄碎片"])  
	item_menu.add_row(["5.","发送全部宝物"])  
	item_menu.add_row(["6.","发送其他道具"])
	item_menu.add_row(["7.","发送全部法术碎片"])
	item_menu.add_row(["8.","手动输入道具ID"])
	print item_menu  
	
def reward_menu():
	reward_menu = PrettyTable(['id', "类型"], encoding=sys.stdout.encoding)  
	reward_menu.align["id"] = "c"# Left align city names
	reward_menu.align["类型"] = "l"
	reward_menu.padding_width = 1# One space between column edges and contents (default)
	reward_menu.add_row(["1.","祭坛抽卡钻石10连抽"])  
	reward_menu.add_row(["2.","祭坛抽卡钻石单抽"])  
	reward_menu.add_row(["3.","祭坛抽卡钥匙10连抽"])  
	reward_menu.add_row(["4.","祭坛抽卡钥匙单抽"])  
	reward_menu.add_row(["5.","法术祈愿钻石10连抽"])  
	reward_menu.add_row(["6.","法术祈愿钻石单抽"])
	reward_menu.add_row(["7.","法术祈愿卷轴10连抽"])
	reward_menu.add_row(["8.","法术祈愿卷轴单抽"])
	reward_menu.add_row(["9.","宝物5连抽"])
	reward_menu.add_row(["10.","宝物单抽"])
	reward_menu.add_row(["11.","器械钻石5连抽"])
	print reward_menu  

def set_level():
	set_level = PrettyTable(['id', "类型"], encoding=sys.stdout.encoding)  
	set_level.align["id"] = "c"# Left align city names
	set_level.align["类型"] = "l"
	set_level.padding_width = 1# One space between column edges and contents (default)
	set_level.add_row(["1.","设置等级"])  
	set_level.add_row(["2.","设置经验"])
	print set_level

def clear_data():
	clear_data = PrettyTable(['id', "类型"], encoding=sys.stdout.encoding)  
	clear_data.align["id"] = "c"# Left align city names
	clear_data.align["类型"] = "l"
	clear_data.padding_width = 1# One space between column edges and contents (default)
	clear_data.add_row(["1.","清空背包"])  
	clear_data.add_row(["2.","每日重置"])
	clear_data.add_row(["3.","重置账号"])
	clear_data.add_row(["4.","重置pve玩法次数"])
	clear_data.add_row(["5.","清除yac"])
	clear_data.add_row(["6.","清除退工会cd"])
	clear_data.add_row(["7.","初始化跨服竞技场数据"])
	print clear_data

def team_choose():
	team_choose = PrettyTable(['id', "类型"], encoding=sys.stdout.encoding)  
	team_choose.align["id"] = "c"# Left align city names
	team_choose.align["类型"] = "l"
	team_choose.padding_width = 1# One space between column edges and contents (default)
	team_choose.add_row(["1.","修改全部兵团"])  
	team_choose.add_row(["2.","修改单独兵团"])
	print team_choose
	
def team_type_choose1():
	team_type_choose1 = PrettyTable(['id', "类型"], encoding=sys.stdout.encoding)  
	team_type_choose1.align["id"] = "c"# Left align city names
	team_type_choose1.align["类型"] = "l"
	team_type_choose1.padding_width = 1# One space between column edges and contents (default)
	team_type_choose1.add_row(["1.","兵团升级"])  
	team_type_choose1.add_row(["2.","兵团装备升级"])
	team_type_choose1.add_row(["3.","兵团装备进阶"])
	team_type_choose1.add_row(["4.","兵团进阶"])
	team_type_choose1.add_row(["5.","兵团升星"])  
	team_type_choose1.add_row(["6.","激活潜能"])
	team_type_choose1.add_row(["7.","激活技能"])
	team_type_choose1.add_row(["8.","技能升级"])
	team_type_choose1.add_row(["9.","潜能升级"])
	team_type_choose1.add_row(["10.","以上全部"])
	print team_type_choose1

def hero_choose():
	hero_choose = PrettyTable(['id', "类型"], encoding=sys.stdout.encoding)  
	hero_choose.align["id"] = "c"# Left align city names
	hero_choose.align["类型"] = "l"
	hero_choose.padding_width = 1# One space between column edges and contents (default)
	hero_choose.add_row(["1.","修改全部英雄"])  
	hero_choose.add_row(["2.","修改单独英雄"])
	print hero_choose

def hero_type_choose():
	hero_type_choose = PrettyTable(['id', "类型"], encoding=sys.stdout.encoding)  
	hero_type_choose.align["id"] = "c"# Left align city names
	hero_type_choose.align["类型"] = "l"
	hero_type_choose.padding_width = 1# One space between column edges and contents (default)
	hero_type_choose.add_row(["1.","英雄升星"])  
	hero_type_choose.add_row(["2.","激活刻印孔"])
	hero_type_choose.add_row(["3.","刷新专精"])
	hero_type_choose.add_row(["4.","技能升级"])
	hero_type_choose.add_row(["5.","以上全部"])
	print hero_type_choose

def activateAwaking():
	activateAwaking = PrettyTable(['id', "类型"], encoding=sys.stdout.encoding)  
	activateAwaking.align["id"] = "c"# Left align city names
	activateAwaking.align["类型"] = "l"
	activateAwaking.padding_width = 1# One space between column edges and contents (default)
	activateAwaking.add_row(["1.","兵团觉醒"])  
	activateAwaking.add_row(["2.","觉醒强化"])
	print activateAwaking

def Treasure():
	Treasure = PrettyTable(['id', "类型"], encoding=sys.stdout.encoding)  
	Treasure.align["id"] = "c"# Left align city names
	Treasure.align["类型"] = "l"
	Treasure.padding_width = 1# One space between column edges and contents (default)
	Treasure.add_row(["1.","装备宝物"])  
	Treasure.add_row(["2.","激活组合宝物"])
	Treasure.add_row(["3.","散件宝物进阶"])
	Treasure.add_row(["4.","组合宝物进阶"])
	Treasure.add_row(["5.","宝物升星"])
	print Treasure

def Treasure_menu():
	Treasure_menu = PrettyTable(['id', "类型"], encoding=sys.stdout.encoding)  
	Treasure_menu.align["id"] = "c"# Left align city names
	Treasure_menu.align["类型"] = "l"
	Treasure_menu.padding_width = 1# One space between column edges and contents (default)
	Treasure_menu.add_row(["1.","修改全部宝物"])  
	Treasure_menu.add_row(["2.","修改单独宝物"])
	print Treasure_menu


