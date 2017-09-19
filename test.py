#!/usr/bin/env python
# encoding: utf-8


from selenium.webdriver.support.ui import Select
from selenium import webdriver
from sgmllib import SGMLParser
import time
import os
import sys
import other_config
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')




# import urllib2
# response = urllib2.urlopen("http://192.168.5.207:8001/demo/ctrl.php")
# html = response.read()
# # print html.decode('utf-8').encode('gbk')
# print type(html)
# print html

file_for_path = open('D:/wyn/123.txt')
for (num, value) in enumerate(file_for_path):
    if '<ul id="menu">' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        first_num = num
    elif '[Tools]添加资源' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Tools]玩家升级' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Tools]设置Vip等级' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Team]升级潜能' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Tools]主线精英重置到某一副本补差删多' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Tools]个人物品发放' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Tools]个人物品发放' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Treasure]进阶散件宝物' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Treasure]进阶组合宝物' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Tools]发放英雄' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Hero]英雄升星' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Tools]个人物品发放' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Hero]技能升级' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Tools]发放兵团' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Team]怪兽方阵升级' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Team]符文批量升级（装备）' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Team]怪兽方阵符文升阶' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Team]怪兽方阵升大星' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Team]怪兽方阵升小星' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Team]激活潜能' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Tools]重置PVE玩法次数' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk')
        print (num - first_num)/2
    elif '[Team]怪兽方阵进阶' in value:
        print "line number", num, "is:", value.decode('utf-8').encode('gbk') 
        print (num - first_num)/2       
file_for_path.close()
