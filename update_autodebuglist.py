#!/usr/bin/env python
# encoding: utf-8

from collections import OrderedDict
import os
import other_config
import json
import csv
import codecs

filenamelist = ['develop1.txt', 'develop2.txt', 'develop3.txt', 'dev3.txt', 'dev4.txt']
new_dict_file = ['update_develop1_file.txt', 'update_develop2_file.txt', 'update_develop3_file.txt', 'update_dev3_file.txt', 'update_dev4_file.txt']
new_dict_develop1 = {}
new_dict_develop2 = {}
new_dict_develop3 = {}
new_dict_dev3 = {}
new_dict_dev4 = {}
new_dict_list = [new_dict_develop1, new_dict_develop2, new_dict_develop3, new_dict_dev3, new_dict_dev4]
menulist = ['[Tools]添加资源', '[Tools]玩家升级', '[Tools]设置Vip等级', '[Team]升级潜能', '[Tools]主线精英重置到某一副本补差删多', '[Tools]个人物品发放', '[Tools]个人物品发放', '[Treasure]进阶散件宝物', '[Treasure]进阶组合宝物', '[Tools]发放英雄', '[Hero]英雄升星', '[Tools]个人物品发放', '[Hero]技能升级', '[Tools]发放兵团', '[Team]怪兽方阵升级', '[Team]符文批量升级（装备）', '[Team]怪兽方阵符文升阶', '[Team]怪兽方阵升大星', '[Team]怪兽方阵升小星', '[Team]激活潜能', '[Tools]重置PVE玩法次数', '[Hero]合成法术书', '[Hero]升级法术书', '[Team]怪兽方阵进阶', '[Tools]清除yac缓存', '[Treasure]宝物升星']
xpahtid_develop1 = []
xpahtid_develop2 = []
xpahtid_develop3 = []
xpahtid_dev3 = []
xpahtid_dev4 = []
xpahtid_set = [xpahtid_develop1, xpahtid_develop2, xpahtid_develop3, xpahtid_dev3, xpahtid_dev4]


def creat_new_dict(new_dict_file_name, dict_name):
    # 将字典写入update文件
    dict_json = json.dumps(dict_name, ensure_ascii=False)
    fileobject = open(new_dict_file_name, 'w')
    fileobject.write(json.dumps(dict_json, ensure_ascii=False))
    fileobject.close()


def modify(filepath, need_to_replace, be_replace):
    # 去除字典内多余的字符
    with open(filepath, "r") as f:
        lines = f.readlines() 
    with open(filepath, "w") as f_w:
        for line in lines:
            if need_to_replace in line:
                line = line.replace(need_to_replace, be_replace)
            f_w.write(line)


def write_list(filename, argv, listname):
    # 通过查找html文件，推断出xpathid并写入list
    global xpahtid_develop1
    global xpahtid_develop2
    global xpahtid_develop3
    global xpahtid_dev3
    global xpahtid_dev4
    global xpahtid_set

    file_for_path = open(filename)
    for (num, value) in enumerate(file_for_path):
        if '<ul id="menu">' in value:
            first_num = num
        elif argv in value:
            xpahtid_num = (num - first_num) / 2
            listname.append(xpahtid_num)
    file_for_path.close()


for x in range(5):
    os.system('python html_file.py "' + str(other_config.debug_server[x - 1]) + '" -> ' + str(filenamelist[x - 1]))
    # print ('python html_file.py "' + str(other_config.debug_server[x-1]) + '" -> ' + str(filenamelist[x-1])) 


for x in menulist:
    # 将菜单类型与对应的xpathid写入list
    for y in range(1, 6):
        write_list(filenamelist[y - 1], x, xpahtid_set[y - 1])
        # print filenamelist[y-1]

menulen = len(menulist)
xpahtlen = len(xpahtid_set)

for x in range(1, int(xpahtlen) + 1):
    # 添加xpathid独有的“l”
    for y in range(1, int(menulen) + 1):
        xpahtid_set[int(x) - 1][int(y) - 1] = "l" + str(xpahtid_set[x -1][y - 1])

# for x in range(1,6):
#     print xpahtid_set[x-1]

new_dict_list[0] = OrderedDict()
new_dict_list[1] = OrderedDict()
new_dict_list[2] = OrderedDict()
new_dict_list[3] = OrderedDict()
new_dict_list[4] = OrderedDict()
# 初始化字典，按照写入顺序排序（menulist）

for x in range(1, int(menulen) + 1):
    # 将菜单类型与对应id写入字典
    for y in range(1, 6):
        new_dict_list[y - 1][menulist[x - 1]] = xpahtid_set[y - 1][x - 1]


# for x in new_dict_list:
#     print json.dumps(x, ensure_ascii=False, encoding='UTF-8')


for x in range(5):
    creat_new_dict(new_dict_file[x], new_dict_list[x])
    #  将字典写入文件
    #  写进文件已经没用了，留着手动检查用 date 2017/9/28


for x in range(5):
    modify(new_dict_file[x], "\\", "")
    modify(new_dict_file[x], "\"", "")
    modify(new_dict_file[x], ",", "\n")
    modify(new_dict_file[x], "{", "")
    modify(new_dict_file[x], "}", "")

print "更新文件已生成".decode('utf-8').encode('gbk')

# 自动获取最新的xpathId
csvfile = file('xpathId_file.csv', 'wb')
csvfile.write(codecs.BOM_UTF8)
writer = csv.writer(csvfile)
writer.writerow(['name', 'develop1_id', 'develop2_id', 'develop3_id', 'dev3_id', 'dev4_id'])
date = []
for x in range(len(menulist)):
    date.append((menulist[x], xpahtid_develop1[x], xpahtid_develop2[x], xpahtid_develop3[x], xpahtid_dev3[x], xpahtid_dev4[x]))
    print (menulist[x] + "数据更新成功").decode('utf-8').encode('gbk')
writer.writerows(date)
csvfile.close()
