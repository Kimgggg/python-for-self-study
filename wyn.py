#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains 
import selenium
import time

driver = webdriver.Firefox()#safari不兼容selenium处理下拉菜单的方法，尝试过13种方法
driver.get("http://deploy2.kof.playcrab-inc.com/gm/?r=site/index")


driver.find_element_by_name("LoginForm[username]").send_keys("wuyinan")
driver.find_element_by_name("LoginForm[password]").send_keys("qIrXRiFw")
driver.find_element_by_name("yt0").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/nav/ul[1]/li[3]/a").click()#浏览器可直接导出Xpath
time.sleep(3)

select = Select(driver.find_element_by_name("platform"))
select.select_by_value('dev2')
time.sleep(3)

select = Select(driver.find_element_by_name("numericScope"))
select.select_by_value('normal')
time.sleep(3)

select = Select(driver.find_element_by_name("numericDir"))
select.select_by_value('数值开发')
time.sleep(3)


driver.find_element_by_xpath("//*[@id='mail_conditon']/div[3]/div[3]/button").click()
time.sleep(3)


driver.find_element_by_xpath("//*[@id='mail_conditon']/div[4]/div[2]/button").click()
time.sleep(3)


test = find_element_by_class_name("modal-content")#no
test.find_element_by_class_name("btn btn-default").click()#no
time.sleep(3)

print "fuck"
driver.quit()

# driver.quit()


