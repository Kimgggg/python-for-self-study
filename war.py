#!/usr/bin/env python
#coding: utf-8

from __future__ import unicode_literals
import os
import webbrowser
import pwd_config

while True:
    print '''
    1.打开测试客户端
    2.更新脚本库
    3.svn更新(war)
    4.svn更新(war-art)
    5.上班套餐
    6.测试专用bat
    7.excel表
    8.workpath
    9.walle-ui-domestic
    10.gmtools
    11.一键更新
    12.svn检查提交
    13.add_new_bug
    14.install apk
    15.svn cleanup

        '''
    press = raw_input("select:\n")
    if press == "1":
        current_path = os.getcwd()
        os.chdir(pwd_config.War_svn_resources)
        os.startfile("war.exe")
        os.chdir(current_path)
    elif press == "2":
        execfile("allbranch_pull.py")
    elif press == "3":
        current_path = os.getcwd()
        os.chdir(pwd_config.War_svn)
        os.system("svn cleanup")
        os.system("svn update")
        os.chdir(current_path)
    elif press == "4":
        current_path = os.getcwd()
        os.chdir(pwd_config.War_svn_art)
        os.system("svn cleanup")
        os.system("svn update")
        os.chdir(current_path)
    elif press == "5":
        execfile("allbranch_pull.py")
        execfile("svn_windows_test.py")
        current_path = os.getcwd()
        os.chdir(pwd_config.War_svn_art)
        os.system("svn cleanup")
        os.system("svn update")
        os.chdir(pwd_config.War_svn_resources)
        os.system("QA_script.bat")
        os.chdir(current_path)
        webbrowser.open("http://120.26.4.254/projects/war")
        webbrowser.open("http://walleui.wartest.com/version/list")
        webbrowser.open("http://gmtools.playcrab.com/war/sendprop/send-prop")        
        os.startfile(pwd_config.War_svn)
        os.startfile(pwd_config.War_svn_design)
        os.startfile(pwd_config.War_svn_configfile)
    elif press == "6":
        current_path = os.getcwd()
        os.chdir(pwd_config.War_svn_resources)
        os.system("QA_script.bat")
        os.chdir(current_path)
    elif press == "7":
        os.startfile(pwd_config.War_svn_design)
    elif press == "8":
        os.startfile(pwd_config.War_svn)
    elif press == "9":
        webbrowser.open("http://walleui.wartest.com/version/list")
    elif press == "10":
        webbrowser.open("http://gmtools.playcrab.com/war/sendprop/send-prop")
    elif press == "11":
        execfile("allbranch_pull.py")
        execfile("svn_windows_test.py")
        current_path = os.getcwd()
        # os.chdir(pwd_config.War_svn)
        # os.system("svn cleanup")
        # os.system("svn update")
        os.chdir(pwd_config.War_svn_art)
        os.system("svn cleanup")
        os.system("svn update")
        os.chdir(current_path)
    elif press == "12":
        execfile("svn_windows_test.py")
    elif press == "13":
        webbrowser.open("http://120.26.4.254/projects/war/issues/new")
    elif press == "14":
        execfile("install_apk_Windows.py")
    elif press == "15":
        current_path = os.getcwd()
        os.chdir(pwd_config.War_svn)
        os.system("svn cleanup")
        os.chdir(current_path)
    elif press == "q":
        os.exit()
    else:
        print "输入错误"