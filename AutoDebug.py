# encoding: utf-8


from __future__ import unicode_literals
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
import csv
import os
import sys
import other_config



develop1 = []
develop2 = []
develop3 = []
dev3 = []
dev4 = []
csv_row = ['develop1_id','develop2_id', 'develop3_id','dev3_id','dev4_id']
dev_list = [develop1,develop2,develop3,dev3,dev4]

reload(sys)
sys.setdefaultencoding('utf-8')
debug = False
user_rid = raw_input("please input rid:\n")
print '''
1.开发机1
2.开发机2
3.开发机3
4.dev3
5.dev4
'''
dev_server = raw_input("please input debug server:\n")
dev_select = dev_server
devserver_number = int(dev_server) - 1
dev_server = other_config.debug_server[int(dev_server) - 1]

if dev_select in ['1', '2', '3']:
    delay = 0.1
else:
    delay = 0.3

def convert_xpath_tr(tr_num, argv):
    # 输入位置参数与类型，返回标准xpath
    first_str = '//*[@id="req"]/form/table/tbody/tr['
    tr = tr_num
    middle_str = ']/td[2]//*[@name="'
    xpath_argv = argv
    finish_str = '"]'
    return first_str + str(tr) + middle_str + str(xpath_argv) + finish_str



def clear_debug_yac():
    # 自动清空yac缓存，可在其他步骤调用
    driver.refresh()
    time.sleep(0.1)
    translate_xpath(xpathID_group(dev_list[devserver_number][24])).click()
    translate_xpath(convert_xpath_tr(1, 'actDev')).clear()
    translate_xpath(convert_xpath_tr(1, 'actDev')).send_keys("0")
    translate_xpath(convert_xpath_tr(2, 'uploadFrom')).click()
    print "debug_yac缓存已清除"
    driver.refresh()
    time.sleep(0.1)
    

def input_user_rid(user_rid):
    # 符合大部分debug功能输入id的规则
    translate_xpath(convert_xpath_tr(1, 'rid')).clear()
    translate_xpath(convert_xpath_tr(1, 'rid')).send_keys(user_rid)
    print "已输入user_rid : " + user_rid


def select_server(user_rid):
    # 根据id自动选择右上角服务器
    sel = driver.find_element_by_xpath("/html/body/div[1]/form/select")
    Select(sel).select_by_value(user_rid[:4])
    print "服务器：" + user_rid[:4]
    

def xpathID_group(xpath_id):
    # 组合xpath id
    first_str = '//*[@id="'
    finish_str = '"]'
    return first_str + xpath_id + finish_str



def translate_xpath(xpath):
    # 当时不知道为什么脑残要封装
    xpath = xpath.replace('"', "'")
    return driver.find_element_by_xpath(xpath)

def loadcsv(list_len):
    with open('xpathId_file.csv','rb') as csvfile:
        reader = csv.DictReader(csvfile)
        dev_list[list_len] = [row[csv_row[list_len]] for row in reader]

for x in range(5):
    loadcsv(x)

def Firefox_or_PhantomJS():
    global debug
    if debug:
        return webdriver.Firefox()
    else:
        return webdriver.PhantomJS()

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
        num = input("please input num:")
        # 添加金币、钻石、兵团经验
        # 添加资源
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)
        translate_xpath(xpathID_group(dev_list[devserver_number][0])).click()
        input_user_rid(user_rid)
        for x in other_config.resource:
            translate_xpath(convert_xpath_tr(2, 'type')).clear()  # 清空资源类型
            translate_xpath(convert_xpath_tr(2, 'type')).send_keys(x)  # 输入资源类型
            translate_xpath(convert_xpath_tr(3, 'num')).clear()  # 清空数量
            translate_xpath(convert_xpath_tr(3, 'num')).send_keys(num)  # 输入数量
            print "已添加" + str(x)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()  # 点击
        num = 0
        time.sleep(delay)
        driver.quit()

    elif press == "2":
        driver = Firefox_or_PhantomJS()       
        driver.get(dev_server)
        select_server(user_rid)
        # 玩家升级
        translate_xpath(xpathID_group(dev_list[devserver_number][1])).click()
        input_user_rid(user_rid)
        translate_xpath(convert_xpath_tr(2, 'level')).send_keys("89")
        translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
        print "玩家等级提升成功"
        driver.quit()

    elif press == "3":
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)
        # 设置vip等级
        translate_xpath(xpathID_group(dev_list[devserver_number][2])).click()
        input_user_rid(user_rid)
        translate_xpath(convert_xpath_tr(2, 'level')).send_keys("15")
        translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
        print "vip等级调整为15"
        time.sleep(delay)
        driver.quit()

    elif press == "4":
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)
        # 升级潜能
        translate_xpath(xpathID_group(dev_list[devserver_number][3])).click()
        time.sleep(delay)
        input_user_rid(user_rid)
        for x in other_config.bingtuanId:
            translate_xpath(convert_xpath_tr(2, 'teamId')).clear()  # 清空兵团id
            translate_xpath(convert_xpath_tr(2, 'teamId')).send_keys(x)  # 输入兵团id
            for y in other_config.potentialId:
                translate_xpath(convert_xpath_tr(3, 'potentialId')).clear()
                # 清空潜力类型
                translate_xpath(convert_xpath_tr(3, 'potentialId')).send_keys(
                    y)  # 输入潜力类型
                for z in range(41):
                    # print "第" + str(z) + "次升级" + str(x) + "的" + str(y) + "潜力"
                    print "%s%s%s%s%s%s%s" %("第",z,"次升级",x,"的",y,"潜力")
                    translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
                    time.sleep(delay)
        driver.quit()
        
    elif press == "5":
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)
        # 主线精英重置到某一副本补差删多
        translate_xpath(xpathID_group(dev_list[devserver_number][4])).click()
        input_user_rid(user_rid)
        for x in other_config.stageId:
            translate_xpath(convert_xpath_tr(2, 'stageId')).clear()  # 清空副本进度
            translate_xpath(convert_xpath_tr(2, 'stageId')).send_keys(x)  # 输入副本id
            translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()  # 点击
            print "调整关卡为" + x
            time.sleep(1)
        driver.quit()

    elif press == "6":
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)
        # 个人物品发放
        print '''
        1.发送全部
        2.发送全部兵团碎片
        3.发送全部进阶材料
        4.发送全部英雄碎片
        5.发送全部宝物
        6.发送全部其他道具
        7.发送全部法术碎片
        '''
        select_type = raw_input("please input num:\n")
        num = input("please input number:")
        if select_type == "1":
            translate_xpath(xpathID_group(dev_list[devserver_number][5])).click()
            input_user_rid(user_rid)
            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.bingtuansuipianId)
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).send_keys(num) # 输入数量
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()  # 点击
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            time.sleep(delay)  # 清空类型
            print "发放兵团碎片成功"
            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.jinjiecailiaoId)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            time.sleep(delay)
            print "发放进阶材料成功"
            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.herosuipianId)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            time.sleep(delay)
            print "发放英雄碎片成功"
            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.baowustr)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            time.sleep(delay)
            print "发放宝物成功"

            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.otheritem)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            time.sleep(delay)
            print "发放杂物成功"

            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.fashusuipian)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            time.sleep(delay)
            print "发放法术碎片成功"
            driver.quit()
        elif select_type == "2":
            translate_xpath(xpathID_group(dev_list[devserver_number][5])).click()
            input_user_rid(user_rid)
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.bingtuansuipianId)
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).clear()
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).send_keys(num)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()  # 点击
            driver.quit()
        elif select_type == "3":
            translate_xpath(xpathID_group(dev_list[devserver_number][5])).click()
            input_user_rid(user_rid)
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.jinjiecailiaoId)
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).clear()
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).send_keys(num)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()  
            driver.quit()  # 点击
        elif select_type == "4":
            translate_xpath(xpathID_group(dev_list[devserver_number][5])).click()
            input_user_rid(user_rid)
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.herosuipianId)
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).clear()
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).send_keys(num)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
            driver.quit()  # 点击
        elif select_type == "5":
            translate_xpath(xpathID_group(dev_list[devserver_number][5])).click()
            input_user_rid(user_rid)
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.baowustr)
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).clear()
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).send_keys(num)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
            driver.quit()  # 点击
        elif select_type == "6":
            translate_xpath(xpathID_group(dev_list[devserver_number][5])).click()
            input_user_rid(user_rid)
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.otheritem)
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).clear()
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).send_keys(num)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
            driver.quit()  # 点击
        elif select_type == "7":
            translate_xpath(xpathID_group(dev_list[devserver_number][5])).click()
            input_user_rid(user_rid)
            translate_xpath(convert_xpath_tr(2, 'goodsId')).clear()
            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys(other_config.fashusuipian)
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).clear()
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).send_keys(num)
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
            driver.quit()  # 点击
        else:
            pass
        num = 0

    elif press == "7":
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)
        # 宝物进阶
        translate_xpath(xpathID_group(dev_list[devserver_number][6])).click()  # 个人物品发放
        input_user_rid(user_rid)
        translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys("41001")  # 额外发送材料
        translate_xpath(convert_xpath_tr(3, 'goodsNum')).send_keys("999999")
        translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
        time.sleep(delay)
        driver.refresh()
        time.sleep(delay)
        translate_xpath(xpathID_group(dev_list[devserver_number][7])).click()  # 进阶散件宝物
        input_user_rid(user_rid)
        big_id = []
        for Treasure_small_temp in other_config.baowu:
            Treasure_small = Treasure_small_temp  # 取大小ID
            Treasure_big_temp = str(Treasure_small_temp)[2:4]
            Treasure_big = int(Treasure_big_temp)
            big_id.append(Treasure_big)
            translate_xpath(convert_xpath_tr(2, 'comId')).clear()  # 散件宝物大id
            translate_xpath(convert_xpath_tr(2, 'comId')).send_keys(Treasure_big)
            translate_xpath(convert_xpath_tr(3, 'disId')).clear()  # 散件宝物小id
            translate_xpath(convert_xpath_tr(3, 'disId')).send_keys(Treasure_small)
            for count in range(30):
                translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
                time.sleep(delay)
                print "宝物" + str(Treasure_small_temp) + "第" + str(count) + "次进阶"
        big_id = list(set(big_id))
        big_id.sort()
        translate_xpath(xpathID_group(dev_list[devserver_number][8])).click()  # 进阶组合宝物
        input_user_rid(user_rid)
        for x in big_id:
            translate_xpath(convert_xpath_tr(2, 'comId')).clear()
            translate_xpath(convert_xpath_tr(2, 'comId')).send_keys(x)
            for y in range(30):
                translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
                time.sleep(delay)
                print "宝物" + str(x) + "进阶" + str(y) + "次"
        driver.quit()

    elif press == "8":
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)
        # 发放英雄
        translate_xpath(xpathID_group(dev_list[devserver_number][9])).click()
        input_user_rid(user_rid)
        for x in other_config.heroId:
            translate_xpath(convert_xpath_tr(2, 'heroId')).clear()
            translate_xpath(convert_xpath_tr(2, 'heroId')).send_keys(x)
            translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
            time.sleep(0.1)
            print "发放英雄" + str(x) + "成功"
        driver.quit()

    elif press == "9":
        # 英雄升星
        Continue_sql = raw_input("数据库方式修改更快速，是否继续？\n1继续2取消\n".decode('utf-8').encode('gbk'))
        if Continue_sql == "1":
            driver = Firefox_or_PhantomJS()
            driver.get(dev_server)
            select_server(user_rid)
            # 英雄升星
            translate_xpath(xpathID_group(dev_list[devserver_number][10])).click()
            input_user_rid(user_rid)
            for x in other_config.heroId:
                translate_xpath(convert_xpath_tr(2, 'heroId')).clear()
                translate_xpath(convert_xpath_tr(2, 'heroId')).send_keys(x)
                for y in range(4):
                    translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
                    time.sleep(0.1)
                    print "英雄" + str(x) + "升星第" + str(y) + "次"
            time.sleep(delay)
            driver.quit()
        else:
            pass

    elif press == "10":
        Continue_sql = raw_input("数据库方式修改更快速，是否继续？\n1继续2取消\n".decode('utf-8').encode('gbk'))
        if Continue_sql == "1":
            driver = Firefox_or_PhantomJS()
            driver.get(dev_server)
            select_server(user_rid)
            # [hero]技能升级
            translate_xpath(xpathID_group(dev_list[devserver_number][11])).click()
            input_user_rid(user_rid)
            translate_xpath(convert_xpath_tr(2, 'goodsId')).send_keys("3004")
            # 额外发送材料
            translate_xpath(convert_xpath_tr(3, 'goodsNum')).send_keys("9999999")
            translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
            time.sleep(delay)
            driver.refresh()
            time.sleep(delay)
            translate_xpath(xpathID_group(dev_list[devserver_number][12])).click()
            input_user_rid(user_rid)
            translate_xpath(convert_xpath_tr(4, 'exMode')).send_keys("1")  # 是否十连突
            for hero in other_config.heroId:
                translate_xpath(convert_xpath_tr(3, 'heroId')).clear()
                translate_xpath(convert_xpath_tr(3, 'heroId')).send_keys(hero)
            # 输入英雄id
                for skill_position in other_config.skillposition:
                    translate_xpath(convert_xpath_tr(2, 'positionId')).clear()
                    translate_xpath(convert_xpath_tr(2, 'positionId')).send_keys(skill_position)  # 输入技能位置
                    for x in range(30):
                        translate_xpath(convert_xpath_tr(5, 'uploadFrom')).click()
                        time.sleep(delay)
                        print "英雄" + str(hero) + "技能" + str(skill_position) + "第" + str(x) + "次十连突"
            driver.quit()
        else:
            pass

    elif press == "11":
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)
        # 发放兵团
        translate_xpath(xpathID_group(dev_list[devserver_number][13])).click()
        input_user_rid(user_rid)
        for x in other_config.bingtuanId:
            translate_xpath(convert_xpath_tr(2, 'teamId')).clear()
            translate_xpath(convert_xpath_tr(2, 'teamId')).send_keys(x)
            translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
            time.sleep(0.1)
            print "已发放兵团" + str(x)
        driver.quit()

    elif press == "12":
        print '''
        配合数据库快速修改兵团属性说明:
        建议使用脚本发放全部兵团与英雄
        数据库只搜索teams数组 (db.game_users.find({_id:8001_853},{teams:1})
        选择json格式
        右键->edit json,全部复制粘贴至txt文件内并保存至D:/,修改名称为'mongo.txt', 例:(D:/mongo.txt)
        执行modify_mongo脚本并传入参数，参数为mongo.txt绝对路径，如：python modify_mongo.py 'D:/wyn/mongo.txt'
        '''
        Continue_sql = raw_input("数据库方式修改更快速，是否继续？\n1继续2取消\n".decode('utf-8').encode('gbk'))
        if Continue_sql == "1":
            driver = Firefox_or_PhantomJS()
            driver.get(dev_server)
            select_server(user_rid)
            #  [Team]怪兽方阵升级
            translate_xpath(xpathID_group(dev_list[devserver_number][14])).click()
            input_user_rid(user_rid)
            translate_xpath(convert_xpath_tr(3, 'level')).send_keys("90")  # 要提升的等级
            for x in other_config.bingtuanId:
                translate_xpath(convert_xpath_tr(2, 'teamId')).clear()
                translate_xpath(convert_xpath_tr(2, 'teamId')).send_keys(x)
                translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
                time.sleep(0.1)
                print "兵团" + str(x) + "已升级"
            time.sleep(delay)
            driver.refresh()
            time.sleep(delay)
            # 符文批量升级（装备）
            translate_xpath(xpathID_group(dev_list[devserver_number][15])).click()
            input_user_rid(user_rid)
            for x in other_config.bingtuanId:
                translate_xpath(convert_xpath_tr(2, 'teamId')).clear()
                translate_xpath(convert_xpath_tr(2, 'teamId')).send_keys(x)
                translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
                time.sleep(delay)
                print "兵团" + str(x) + "装备已升级"

            time.sleep(delay)
            driver.refresh()
            time.sleep(delay)
            translate_xpath(xpathID_group(dev_list[devserver_number][16])).click()
            # [Team]怪兽方阵符文升阶
            input_user_rid(user_rid)
            for x in other_config.bingtuanId:
                translate_xpath(convert_xpath_tr(2, 'teamId')).clear()
                translate_xpath(convert_xpath_tr(2, 'teamId')).send_keys(x)
                for y in other_config.skillposition:   # 用技能位置代替装备位置
                    translate_xpath(convert_xpath_tr(3, 'positionId')).clear()
                    translate_xpath(convert_xpath_tr(3, 'positionId')).send_keys(y)
                    for z in range(15):
                        translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
                        time.sleep(delay)
                        print "兵团" + str(x) + "装备" + str(y) + "正在第" + str(z) + "次升阶"
            driver.quit()
        else:
            pass

    elif press == "13":
        user_rid = raw_input("please input new user_rid:\n")
        print '''
        1.开发机1
        2.开发机2
        3.开发机3
        4.dev3
        5.dev4
        '''
        dev_server = raw_input("please input debug server:\n")
        dev_select = dev_server
        devserver_number = int(dev_server) - 1
        dev_server = other_config.debug_server[int(dev_server) - 1]

    elif press == "14":
        Continue_sql = raw_input("数据库方式修改更快速，是否继续？\n1继续2取消\n".decode('utf-8').encode('gbk'))
        if Continue_sql == "1":
            driver = Firefox_or_PhantomJS()
            driver.get(dev_server)
            select_server(user_rid)
            # 所有兵团升星+激活潜能
            # [Team]怪兽方阵升大星

            def bigStar(argv_id):
                driver.refresh()
                time.sleep(delay)
                translate_xpath(xpathID_group(dev_list[devserver_number][17])).click()
                input_user_rid(user_rid)
                translate_xpath(convert_xpath_tr(2, 'teamId')).clear()
                translate_xpath(convert_xpath_tr(2, 'teamId')).send_keys(argv_id)
                translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
                print "大星" + str(argv_id) + "done"
                time.sleep(delay)


            def smallStar(argv_id):
                driver.refresh()
                time.sleep(delay)
                # [Team]怪兽方阵升小星
                translate_xpath(xpathID_group(dev_list[devserver_number][18])).click()
                input_user_rid(user_rid)
                translate_xpath(convert_xpath_tr(2, 'teamId')).clear()
                translate_xpath(convert_xpath_tr(2, 'teamId')).send_keys(argv_id)
                translate_xpath(convert_xpath_tr(3, 'batch')).clear()
                translate_xpath(convert_xpath_tr(3, 'batch')).send_keys("1")
                translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()
                time.sleep(delay)
                print "小星" + str(argv_id) + "done"


            for x in range(1):
                for y in other_config.bingtuanId1star:
                    smallStar(y)
                    bigStar(y)
            new_bingtuansuipian2star = other_config.bingtuanId1star + other_config.bingtuanId2star
            print "全部1星兵团已升至2星"
            for x in range(1):
                for y in new_bingtuansuipian2star:
                    smallStar(y)
                    bigStar(y)
            new_bingtuansuipian3star = new_bingtuansuipian2star + other_config.bingtuanId3star
            print "全部1星兵团与2星兵团已全部3星"
            for x in range(3):
                print "第" + str((x + 1)) + "次集体升星"
                for y in new_bingtuansuipian3star:
                    smallStar(y)
                    bigStar(y)
            driver.refresh()
            time.sleep(delay)
            # 激活潜能
            translate_xpath(xpathID_group(dev_list[devserver_number][19])).click()
            input_user_rid(user_rid)
            for z in other_config.bingtuanId:
                translate_xpath(convert_xpath_tr(2, 'teamId')).clear()
                translate_xpath(convert_xpath_tr(2, 'teamId')).send_keys(z)
                translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
                time.sleep(delay)
                print "兵团" + str(z) + "激活潜能"
            driver.quit()
        else:
            pass

    elif press == "15":
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)        # [Tools]重置PVE玩法次数
        translate_xpath(xpathID_group(dev_list[devserver_number][20])).click()
        input_user_rid(user_rid)
        translate_xpath(convert_xpath_tr(2, 'uploadFrom')).click()
        time.sleep(delay)
        print "重置成功"
        driver.quit()

    elif press == "16":
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)
        translate_xpath(xpathID_group(dev_list[devserver_number][21])).click()
        # [Hero]合成法术书
        input_user_rid(user_rid)
        for x in other_config.skillId:
            translate_xpath(convert_xpath_tr(2, 'sid')).clear()
            translate_xpath(convert_xpath_tr(2, 'sid')).send_keys(x)
            translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
            time.sleep(0.1)
            print "法术" + str(x) + "已激活"
        time.sleep(delay)
        driver.refresh()
        time.sleep(delay)

        translate_xpath(xpathID_group(dev_list[devserver_number][22])).click()
        # [Hero]升级法术书
        input_user_rid(user_rid)
        for x in other_config.skillId:
            translate_xpath(convert_xpath_tr(2, 'sid')).clear()
            translate_xpath(convert_xpath_tr(2, 'sid')).send_keys(x)
            for y in range(10):
                translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
                time.sleep(0.1)
                print "法术" + str(x) + "第" + str(y) + "次升级"

        driver.quit()

    elif press == "17":
        Continue_sql = raw_input("数据库方式修改更快速，是否继续？\n1继续2取消\n".decode('utf-8').encode('gbk'))
        if Continue_sql == "1":
            driver = Firefox_or_PhantomJS()
            driver.get(dev_server)
            select_server(user_rid)
            translate_xpath(xpathID_group(dev_list[devserver_number][23])).click()
            # [Team]怪兽方阵进阶
            input_user_rid(user_rid)
            for x in other_config.bingtuanId:
                translate_xpath(convert_xpath_tr(2, 'teamId')).clear()
                translate_xpath(convert_xpath_tr(2, 'teamId')).send_keys(x)
                for y in range(15):
                    translate_xpath(convert_xpath_tr(3, 'uploadFrom')).click()
                    time.sleep(delay)
                    print "兵团" + str(x) + "进阶第" + str(y) + "次"
            driver.quit()

    elif press == "18":
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)
        translate_xpath(xpathID_group(dev_list[devserver_number][24])).click()
        # [Tools]清除yac缓存
        translate_xpath(convert_xpath_tr(1, 'actDev')).clear()
        translate_xpath(convert_xpath_tr(1, 'actDev')).send_keys("0")
        translate_xpath(convert_xpath_tr(2, 'uploadFrom')).click()
        driver.quit()

    elif press == "19":
        driver = Firefox_or_PhantomJS()
        driver.get(dev_server)
        select_server(user_rid)

        translate_xpath(xpathID_group(dev_list[devserver_number][0])).click()
        # [Tools]添加资源
        input_user_rid(user_rid)
        translate_xpath(convert_xpath_tr(2, 'type')).clear()  # 清空资源类型
        translate_xpath(convert_xpath_tr(2, 'type')).send_keys("starfrag")  # 输入资源类型
        translate_xpath(convert_xpath_tr(3, 'num')).clear()  # 清空数量
        translate_xpath(convert_xpath_tr(3, 'num')).send_keys("9999999")  # 输入数量
        translate_xpath(convert_xpath_tr(4, 'uploadFrom')).click()  # 点击
        time.sleep(delay)

        driver.refresh()
        time.sleep(delay)
        translate_xpath(xpathID_group(dev_list[devserver_number][25])).click()
        # [Treasure]宝物升星
        input_user_rid(user_rid)
        translate_xpath(convert_xpath_tr(4, 'num')).clear()
        translate_xpath(convert_xpath_tr(4, 'num')).send_keys("10")
        for x in other_config.baowu:
            translate_xpath(convert_xpath_tr(3, 'disId')).clear()
            translate_xpath(convert_xpath_tr(3, 'disId')).send_keys(x)
            x = str(x)
            big_id = x[2:4]
            translate_xpath(convert_xpath_tr(2, 'comId')).clear()
            translate_xpath(convert_xpath_tr(2, 'comId')).send_keys(big_id)
            for y in range(60):
                time.sleep(delay)
                translate_xpath(convert_xpath_tr(5, 'uploadFrom')).click()
                print "宝物" + str(x) + "第" + str(y) + "次升星"
        driver.quit()


    elif press == "test":
        driver = webdriver.Firefox()
        driver.get(dev_server)
        select_server(user_rid)
        clear_debug_yac()
        driver.quit()

    elif press == "q":
        os.exit()

    else:
        print "input error!"