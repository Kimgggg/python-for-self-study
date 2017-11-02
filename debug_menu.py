#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import sys
from prettytable import PrettyTable

def main_menu():
	main_menu = PrettyTable(['id', "选项"], encoding=sys.stdout.encoding)  
	main_menu.align["id"] = "c"# Left align city names
	main_menu.align["选项"] = "l"
	main_menu.padding_width = 1# One space between column edges and contents (default)
	main_menu.add_row(["1.","添加金币、钻石、兵团经验、体力、角色经验"])  
	main_menu.add_row(["2.","玩家升级"])  
	main_menu.add_row(["3.","设置vip等级"])  
	main_menu.add_row(["4.","提升全部兵团潜力"])  
	main_menu.add_row(["5.","调整副本进度"])  
	main_menu.add_row(["6.","发送道具"])  
	main_menu.add_row(["7.","全部宝物进阶+升星"])
	main_menu.add_row(["8.","发送全部英雄"])
	main_menu.add_row(["9.","英雄升星+开启法术槽"])  
	main_menu.add_row(["10.","全部英雄技能升级+随机刷新5次专精"])  
	main_menu.add_row(["11.","发送全部兵团"])  
	main_menu.add_row(["12.","所有兵团升级+兵团装备升级+兵团装备进阶"])  
	main_menu.add_row(["13.","更换user_rid与服务器"])  
	main_menu.add_row(["14.","所有兵团升星+激活潜能+解锁技能+技能升级"])  
	main_menu.add_row(["15.","重置pve玩法次数"])
	main_menu.add_row(["16.","法术激活升级"])
	main_menu.add_row(["17.","图鉴解锁+图鉴升级"])  
	main_menu.add_row(["18.","清除yac"])  
	main_menu.add_row(["19.","英雄天赋升级"])  
	main_menu.add_row(["20.","清空背包"])  
	main_menu.add_row(["21.","觉醒兵团+觉醒强化"])  
	main_menu.add_row(["22.","全部兵团指定次数随机增加兵团天赋"])  
	main_menu.add_row(["24.","抽卡测试"])
	main_menu.add_row(["q.","退出"])
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
	res_menu.add_row(["6.","角色经验"])
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
	print reward_menu  