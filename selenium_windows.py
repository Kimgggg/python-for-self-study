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