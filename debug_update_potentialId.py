#!/usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
from selenium import webdriver
import selenium
import time
import fuck_gbk

driver = webdriver.Firefox()#干你娘的safari不兼容selenium处理下拉菜单的方法，尝试过13种方法才他娘的发现，操
driver.get("http://192.168.5.207:8001/demo/ctrl.php")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='l571']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='req']/form/table/tbody/tr[1]/td[2]//*[@name='rid']").send_keys("8001_738")
heroid = [101,102,103,104,105,106,107,201,202,203,204,205,206,207,301,302,303,304,305,306,307,401,402,403,404,405,406,407,501,502,503,504,505,506,507,601,602,603,604,605,606,607,901,902,903,904,905,906,907]
potentialId = [1,2,3]

for x in heroid:
	driver.find_element_by_xpath("//*[@id='req']/form/table/tbody/tr[2]/td[2]//*[@name='teamId']").clear()
	driver.find_element_by_xpath("//*[@id='req']/form/table/tbody/tr[2]/td[2]//*[@name='teamId']").send_keys(x)
	for y in potentialId:
		driver.find_element_by_xpath("//*[@id='req']/form/table/tbody/tr[3]/td[2]//*[@name='potentialId']").clear()
		driver.find_element_by_xpath("//*[@id='req']/form/table/tbody/tr[3]/td[2]//*[@name='potentialId']").send_keys(y)
		for z in range(45):
			print "第" + str(z) + "次升级" + str(x) + "的" + str(y) + "潜力"
			driver.find_element_by_xpath("//*[@id='req']/form/table/tbody/tr[4]/td[2]//*[@name='uploadFrom']").click()