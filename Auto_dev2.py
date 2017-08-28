#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains 
import selenium
import time
import pwd_config
import no_upload


profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 1)
profile.set_preference('browser.download.manager.showWhenStarting', True)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/x-tar')


driver = webdriver.Firefox(firefox_profile = profile)#干你娘的safari不兼容selenium处理下拉菜单的方法，尝试过13种方法才他娘的发现，操
driver.get("http://deploy2.kof.playcrab-inc.com/gm/?r=site/index")


driver.find_element_by_name("LoginForm[username]").send_keys(no_upload.username)
driver.find_element_by_name("LoginForm[password]").send_keys(no_upload.password)
driver.find_element_by_name("yt0").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/nav/ul[1]/li[3]/a").click()
time.sleep(1)

select = Select(driver.find_element_by_name("platform"))
select.select_by_value('dev2')
select = Select(driver.find_element_by_name("numericScope"))
select.select_by_value('normal')
select = Select(driver.find_element_by_name("numericDir"))
select.select_by_value('数值开发')

driver.find_element_by_xpath("//*[@id='mail_conditon']/div[3]/div[3]/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='mail_conditon']/div[4]/div[2]/button").click()
time.sleep(1)
driver.find_element_by_css_selector("button.btn.btn-default").click()#html里空格用“.“代替就好了，不知道为啥
time.sleep(2)


updata_done = driver.switch_to_alert()
time.sleep(1)
updata_done.accept()
time.sleep(1)

time.sleep(600)
driver.refresh()
try:
	driver.find_element_by_xpath("//*[@id='yw0']/table/tbody/tr[74]/td[10]/a[4]").click()
	time.sleep(5)
	print "下载导表结果成功"
	os.chdir(pwd_config.python_Script)
	execfile("AutoMoveAndRemove.py")
except Exception as e:
	print "下载导表结果失败,未搜寻到dev2_all.tar文件"
finally:
	print "脚本运行结束"
	driver.quit()



