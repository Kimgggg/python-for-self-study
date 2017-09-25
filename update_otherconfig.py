#!/usr/bin/env python
# encoding: utf-8

import os
import other_config
import json

dict_test = {}
dict_develop1 = {}
dict_develop2 = {}
dict_develop3 = {}
dict_dev3 = {}
dict_dev4 = {}
filenamelist = ['develop1.txt', 'develop2.txt', 'develop3.txt', 'dev3.txt', 'dev4.txt']
dict_list = [dict_develop1, dict_develop2, dict_develop3, dict_dev3, dict_dev4]
new_dict_file = ['update_develop1_file.txt', 'update_develop2_file.txt', 'update_develop3_file.txt', 'update_dev3_file.txt', 'update_dev4_file.txt']
new_dict_develop1 = {}
new_dict_develop2 = {}
new_dict_develop3 = {}
new_dict_dev3 = {}
new_dict_dev4 = {}


for x in range(5):
    os.system('python html_file.py "' + str(other_config.debug_server[x-1]) + '" -> ' + str(filenamelist[x-1]))
    # print ('python html_file.py "' + str(other_config.debug_server[x-1]) + '" -> ' + str(filenamelist[x-1]))


def creat_dict(filename, dictname):
    global dict_develop1
    global dict_develop2
    global dict_develop3
    global dict_dev3
    global dict_dev4

    file_for_path = open(filename)
    for (num, value) in enumerate(file_for_path):
        if '<ul id="menu">' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            first_num = num
        elif '[Tools]添加资源' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Tools]添加资源'] = (num - first_num) / 2

        elif '[Tools]玩家升级' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Tools]玩家升级'] = (num - first_num) / 2

        elif '[Tools]设置Vip等级' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Tools]设置Vip等级'] = (num - first_num) / 2

        elif '[Team]升级潜能' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Team]升级潜能'] = (num - first_num) / 2

        elif '[Tools]主线精英重置到某一副本补差删多' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Tools]主线精英重置到某一副本补差删多'] = (num - first_num) / 2

        elif '[Tools]个人物品发放' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Tools]个人物品发放'] = (num - first_num) / 2

        elif '[Tools]个人物品发放' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Tools]个人物品发放'] = (num - first_num) / 2

        elif '[Treasure]进阶散件宝物' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Treasure]进阶散件宝物'] = (num - first_num) / 2

        elif '[Treasure]进阶组合宝物' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Treasure]进阶组合宝物'] = (num - first_num) / 2

        elif '[Tools]发放英雄' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Tools]发放英雄'] = (num - first_num) / 2

        elif '[Hero]英雄升星' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Hero]英雄升星'] = (num - first_num) / 2

        elif '[Tools]个人物品发放' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Tools]个人物品发放'] = (num - first_num) / 2

        elif '[Hero]技能升级' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Hero]技能升级'] = (num - first_num) / 2

        elif '[Tools]发放兵团' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Tools]发放兵团'] = (num - first_num) / 2

        elif '[Team]怪兽方阵升级' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Team]怪兽方阵升级'] = (num - first_num) / 2

        elif '[Team]符文批量升级（装备）' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Team]符文批量升级（装备）'] = (num - first_num) / 2

        elif '[Team]怪兽方阵符文升阶' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Team]怪兽方阵符文升阶'] = (num - first_num) / 2

        elif '[Team]怪兽方阵升大星' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Team]怪兽方阵升大星'] = (num - first_num) / 2

        elif '[Team]怪兽方阵升小星' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Team]怪兽方阵升小星'] = (num - first_num) / 2

        elif '[Team]激活潜能' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Team]激活潜能'] = (num - first_num) / 2

        elif '[Tools]重置PVE玩法次数' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk')
            # print (num - first_num)/2
            dictname['[Tools]重置PVE玩法次数'] = (num - first_num) / 2

        elif '[Team]怪兽方阵进阶' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk') 
            # print (num - first_num)/2
            dictname['[Team]怪兽方阵进阶'] = (num - first_num) / 2
        elif '[Tools]清除yac缓存' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk') 
            # print (num - first_num)/2
            dictname['[Tools]清除yac缓存'] = (num - first_num) / 2
        elif '[Treasure]宝物升星' in value:
            # print "line number", num, "is:", value.decode('utf-8').encode('gbk') 
            # print (num - first_num)/2
            dictname['[Treasure]宝物升星'] = (num - first_num) / 2
    file_for_path.close()    


def creat_new_dict(new_dict_file_name, dict_name):
    dict_json = json.dumps(dict_name, ensure_ascii=False)
    fileobject = open(new_dict_file_name, 'w')
    fileobject.write(json.dumps(dict_json, ensure_ascii=False))
    fileobject.close()


def modify(filepath, need_to_replace, be_replace):
    with open(filepath, "r") as f:
        lines = f.readlines() 
    with open(filepath, "w") as f_w:
        for line in lines:
            if need_to_replace in line:
                line = line.replace(need_to_replace, be_replace)
            f_w.write(line)



for x in range(5):
    creat_dict(filenamelist[x], dict_list[x])

# for x in range(5):
#     print json.dumps(dict_list[x], ensure_ascii=False, encoding='UTF-8')
    
for x in range(5):
    creat_new_dict(new_dict_file[x], dict_list[x])

for x in range(5):
    modify(new_dict_file[x], "\\", "")
    modify(new_dict_file[x], "\"", "")
    modify(new_dict_file[x], ",", "\n")
    modify(new_dict_file[x], ": ", " : l")
    modify(new_dict_file[x], "{", "")
    modify(new_dict_file[x], "}", "")