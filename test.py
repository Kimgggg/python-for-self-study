#!/usr/bin/env python
# encoding: utf-8


from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import os
import sys
import other_config
reload(sys)
sys.setdefaultencoding('utf-8')

# user_rid = raw_input("please input rid:\n")
# print '''
# 1.开发机1
# 2.开发机2
# 3.开发机3
# 4.dev3
# 5.dev4
# '''
def translate_xpath(xpath):
    xpath = xpath.replace('"', "'")
    return driver.find_element_by_xpath(xpath)

# if sys.platform == 'win32':
# 	filePath = filePath.decode('gbk')
# 	test = u"".join(atext.decode("gbk"))
# 	test = u"".join(atext.decode("gbk"))


driver = webdriver.Firefox()
driver.get("http://120.26.4.254/projects/war/issues/new")
translate_xpath("//*[@id='username']").send_keys("wuyinan")
translate_xpath("//*[@id='password']").send_keys("12345678")
translate_xpath("//*[@id='login-form']/form/table/tbody/tr[4]/td[2]/input").click()
time.sleep(1)
select = Select(driver.find_element_by_name("issue[tracker_id]"))
select.select_by_value('2')

atext = raw_input("please input project name:\n")
test = u"".join(atext.decode("gbk"))
translate_xpath("//*[@id='issue_subject']").send_keys(test)




time.sleep(1)

# drop_down.find_element_by_xpath("//*[@id='menu'][contains(text(),'添加资源')]").click()
# # select = Select(driver.find_element_by_xpath("//*[@id='left']"))
# # print select

# # select.select_by_value("[Tools]添加资源")