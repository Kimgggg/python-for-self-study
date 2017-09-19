# encoding: utf-8


from __future__ import unicode_literals
from selenium import webdriver
import time
import os
import sys
import other_config

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
dev_server = other_config.debug_server[int(dev_server) - 1]


def xpath_group(xpath_id):
    first_str = '//*[@id="'
    finish_str = '"]'
    return first_str + xpath_id + finish_str



def translate_xpath(xpath):
    xpath = xpath.replace('"', "'")
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
    11.发放全部兵团
    13.更换user_rid与服务器
    15.重置pve玩法次数
    q.退出
    """

    press = raw_input("select:")
    if press == "1":
        num = input("please input num:")
        # 添加金币、钻石、兵团经验
        # 添加资源
        if debug:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.PhantomJS()
        driver.get(dev_server)
        # driver.set_window_size(480, 320)
        time.sleep(1)
        translate_xpath(xpath_group(other_config.autodebug1[int(dev_select) - 1])).click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
        for x in other_config.resource:
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="type"]').clear()  # 清空资源类型
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="type"]').send_keys(x)  # 输入资源类型
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="num"]').clear()  # 清空数量
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="num"]').send_keys(num)  # 输入数量
            print "已添加" + str(x)
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()  # 点击
        num = 0
        time.sleep(1)
        driver.quit()

    elif press == "2":
        if debug:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.PhantomJS()        
        driver.get(dev_server)
        # driver.set_window_size(480, 320)
        time.sleep(1)
        # 玩家升级
        translate_xpath(xpath_group(other_config.autodebug2[int(dev_select) - 1])).click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="level"]').send_keys("89")
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
        print "玩家等级提升成功"
        driver.quit()

    elif press == "3":
        if debug:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.PhantomJS()
        driver.get(dev_server)
        # driver.set_window_size(480, 320)
        time.sleep(1)
        # 设置vip等级
        translate_xpath(xpath_group(other_config.autodebug3[int(dev_select) - 1])).click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="level"]').send_keys("15")
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
        print "vip等级调整为15"
        time.sleep(1)
        driver.quit()

    elif press == "4":
        if debug:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.PhantomJS()
        driver.get(dev_server)
        # driver.set_window_size(480, 320)
        time.sleep(1)
        # 升级潜能
        translate_xpath(xpath_group(other_config.autodebug4[int(dev_select) - 1])).click()
        time.sleep(1)
        translate_xpath("//*[@id='req']/form/table/tbody/tr[1]/td[2]//*[@name='rid']").send_keys(user_rid)
        for x in other_config.bingtuanId:
            translate_xpath("//*[@id='req']/form/table/tbody/tr[2]/td[2]//*[@name='teamId']").clear()  # 清空兵团id
            translate_xpath("//*[@id='req']/form/table/tbody/tr[2]/td[2]//*[@name='teamId']").send_keys(x)  # 输入兵团id
            for y in other_config.potentialId:
                translate_xpath("//*[@id='req']/form/table/tbody/tr[3]/td[2]//*[@name='potentialId']").clear()
                # 清空潜力类型
                translate_xpath("//*[@id='req']/form/table/tbody/tr[3]/td[2]//*[@name='potentialId']").send_keys(
                    y)  # 输入潜力类型
                for z in range(41):
                    print "第" + str(z) + "次升级" + str(x) + "的" + str(y) + "潜力"
                    translate_xpath("//*[@id='req']/form/table/tbody/tr[4]/td[2]//*[@name='uploadFrom']").click()  # 点击
        driver.quit()

    elif press == "5":
        if debug:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.PhantomJS()
        driver.get(dev_server)
        # driver.set_window_size(480, 320)
        time.sleep(1)
        # 主线精英重置到某一副本补差删多
        translate_xpath(xpath_group(other_config.autodebug5[int(dev_select) - 1])).click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
        for x in other_config.stageId:
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="stageId"]').clear()  # 清空副本进度
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="stageId"]').send_keys(x)  # 输入副本id
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()  # 点击
            print "调整关卡为" + x
            time.sleep(1.5)
        driver.quit()

    elif press == "6":
        num = input("please input num:")
        if debug:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.PhantomJS()
        driver.get(dev_server)
        # driver.set_window_size(480, 320)
        time.sleep(1)
        # 个人物品发放
        translate_xpath(xpath_group(other_config.autodebug6[int(dev_select) - 1])).click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys(other_config.bingtuansuipianId)
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="goodsNum"]').send_keys(num)  # 输入数量，需注意，后续添加时数量不会更新,不能被注释
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()  # 点击
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').clear()  # 清空类型
        print "发放兵团碎片成功"
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys(other_config.jinjiecailiaoId)
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').clear()
        print "发放进阶材料成功"
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys(other_config.herosuipianId)
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').clear()
        print "发放英雄碎片成功"
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys(other_config.baowustr)
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').clear()
        print "发放宝物成功"

        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys(other_config.otheritem)
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').clear()
        print "发放杂物成功"

        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys(other_config.fashusuipian)
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').clear()
        print "发放法术碎片成功"
        num = 0
        driver.quit()

    elif press == "7":
        if debug:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.PhantomJS()
        driver.get(dev_server)
        # driver.set_window_size(480, 320)
        time.sleep(1)
        # 宝物进阶
        translate_xpath(xpath_group(other_config.autodebug7_1[int(dev_select) - 1])).click() # 个人物品发放
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys("41001")  # 额外发送材料
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="goodsNum"]').send_keys("999999")
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
        time.sleep(0.5)
        driver.refresh()
        time.sleep(1)
        translate_xpath(xpath_group(other_config.autodebug7_2[int(dev_select) - 1])).click()  # 进阶散件宝物
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
        big_id = []
        for Treasure_small_temp in other_config.baowu:
            Treasure_small = Treasure_small_temp  # 取大小ID
            Treasure_big_temp = str(Treasure_small_temp)[2:4]
            Treasure_big = int(Treasure_big_temp)
            big_id.append(Treasure_big)
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="comId"]').clear()  # 散件宝物大id
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="comId"]').send_keys(Treasure_big)
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="disId"]').clear()  # 散件宝物小id
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="disId"]').send_keys(Treasure_small)
            for count in range(37):
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
                print "宝物" + str(Treasure_small_temp) + "第" + str(count) + "次进阶"
        big_id = list(set(big_id))
        big_id.sort()
        translate_xpath(xpath_group(other_config.autodebug7_3[int(dev_select) - 1])).click()  # 进阶组合宝物
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
        for x in big_id:
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="comId"]').clear()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="comId"]').send_keys(x)
            for y in range(37):
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
                print "宝物" + str(x) + "进阶" + str(y) + "次"
        driver.quit()

    elif press == "8":
        if debug:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.PhantomJS()
        driver.get(dev_server)
        # driver.set_window_size(480, 320)
        time.sleep(1)
        # 发放英雄
        translate_xpath(xpath_group(other_config.autodebug8[int(dev_select) - 1])).click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
        for x in other_config.heroId:
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="heroId"]').clear()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="heroId"]').send_keys(x)
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
            print "发放英雄" + str(x) + "成功"
        driver.quit()

    elif press == "9":
        # 英雄升星
        Continue_sql = raw_input("数据库方式修改更快速，是否继续？\n1继续2取消\n".decode('utf-8').encode('gbk'))
        if Continue_sql == "1":
            if debug:
                driver = webdriver.Firefox()
            else:
                driver = webdriver.PhantomJS()
            driver.get(dev_server)
            time.sleep(1)
            # 英雄升星
            translate_xpath(xpath_group(other_config.autodebug9[int(dev_select) - 1])).click()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
            for x in other_config.heroId:
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="heroId"]').clear()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="heroId"]').send_keys(x)
                for y in range(4):
                    translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
                    print "英雄" + str(x) + "升星第" + str(y) + "次"
            time.sleep(1)
            driver.quit()
        else:
            pass

    elif press == "10":
        Continue_sql = raw_input("数据库方式修改更快速，是否继续？\n1继续2取消\n".decode('utf-8').encode('gbk'))
        if Continue_sql == "1":
            if debug:
                driver = webdriver.Firefox()
            else:
                driver = webdriver.PhantomJS()
            driver.get(dev_server)
            time.sleep(1)
            # [hero]技能升级
            translate_xpath(xpath_group(other_config.autodebug10_1[int(dev_select) - 1])).click()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="goodsId"]').send_keys("3004")
            # 额外发送材料
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="goodsNum"]').send_keys("9999999")
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
            time.sleep(0.5)
            driver.refresh()
            time.sleep(1)
            translate_xpath(xpath_group(other_config.autodebug10_2[int(dev_select) - 1])).click()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="exMode"]').send_keys("1")  # 是否十连突
            for hero in other_config.heroId:
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="heroId"]').clear()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="heroId"]').send_keys(hero)
            # 输入英雄id
                for skill_position in other_config.skillposition:
                    translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="positionId"]').clear()
                    translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="positionId"]').send_keys(skill_position)  # 输入技能位置
                    for x in range(30):
                        translate_xpath('//*[@id="req"]/form/table/tbody/tr[5]/td[2]//*[@name="uploadFrom"]').click()
                        print "英雄" + str(hero) + "技能" + str(skill_position) + "第" + str(x) + "次十连突"
            time.sleep(1)
            driver.quit()
        else:
            pass

    elif press == "11":
        if debug:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.PhantomJS()
        driver.get(dev_server)
        # driver.set_window_size(480, 320)
        time.sleep(1)
        # 发放兵团
        translate_xpath(xpath_group(other_config.autodebug11[int(dev_select) - 1])).click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
        for x in other_config.bingtuanId:
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(x)
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
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
            if debug:
                driver = webdriver.Firefox()
            else:
                driver = webdriver.PhantomJS()
            driver.get(dev_server)
            time.sleep(1)
            # 所有兵团升级
            translate_xpath(xpath_group(other_config.autodebug12_1[int(dev_select) - 1])).click()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="level"]').send_keys("90")  # 要提升的等级
            for x in other_config.bingtuanId:
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(x)
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
                print "兵团" + str(x) + "已升级"
            time.sleep(0.5)
            driver.refresh()
            time.sleep(1)
            # 所有兵团装备升级
            translate_xpath(xpath_group(other_config.autodebug12_2[int(dev_select) - 1])).click()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
            for x in other_config.bingtuanId:
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(x)
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
                print "兵团" + str(x) + "装备已升级"
            driver.quit()
        else:
            pass



    elif press == "13":
        user_rid = raw_input("please input new user_rid:\n")
        print '''
        1.开发机1
        2.开发机2
        3.开发机3
        4.dev3(暂时无法使用)
        5.dev4(暂时无法使用)
        '''
        dev_server = raw_input("please input debug server:\n")
        dev_select = dev_server
        dev_server = other_config.debug_server[int(dev_server) - 1]

    elif press == "14":
        Continue_sql = raw_input("数据库方式修改更快速，是否继续？\n1继续2取消\n".decode('utf-8').encode('gbk'))
        if Continue_sql == "1":
            if debug:
                driver = webdriver.Firefox()
            else:
                driver = webdriver.PhantomJS()
            driver.get(dev_server)
            time.sleep(1)
            # 所有兵团升星+激活潜能
            # [Team]怪兽方阵升大星
            def bigStar(argv_id):
                driver.refresh()
                time.sleep(1)
                translate_xpath(xpath_group(other_config.autodebug14_1[int(dev_select) - 1])).click()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(argv_id)
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
                print "大星" + str(argv_id) + "done"
                time.sleep(0.5)


            def smallStar(argv_id):
                driver.refresh()
                time.sleep(1)
                # [Team]怪兽方阵升小星
                translate_xpath(xpath_group(other_config.autodebug14_2[int(dev_select) - 1])).click()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(argv_id)
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="batch"]').clear()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="batch"]').send_keys("1")
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[4]/td[2]//*[@name="uploadFrom"]').click()
                time.sleep(0.5)
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
            time.sleep(1)
            # 激活潜能
            translate_xpath(xpath_group(other_config.autodebug14_3[int(dev_select) - 1])).click()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
            translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
            for z in other_config.bingtuanId:
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').clear()
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="teamId"]').send_keys(z)
                translate_xpath('//*[@id="req"]/form/table/tbody/tr[3]/td[2]//*[@name="uploadFrom"]').click()
                print "兵团" + str(z) + "激活潜能"
            driver.quit()
        else:
            pass

    elif press == "15":
        if debug:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.PhantomJS()
        driver.get(dev_server)
        time.sleep(1)
        # [Tools]重置PVE玩法次数
        translate_xpath(xpath_group(other_config.autodebug15[int(dev_select) - 1])).click()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').clear()
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[1]/td[2]//*[@name="rid"]').send_keys(user_rid)
        translate_xpath('//*[@id="req"]/form/table/tbody/tr[2]/td[2]//*[@name="uploadFrom"]').click()
        time.sleep(0.5)
        print "重置成功"
        driver.quit()

    elif press == "q":
        os.exit()

    else:
        print "input error!"
