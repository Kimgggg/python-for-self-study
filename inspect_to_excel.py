#!/usr/bin/env python
# encoding: utf-8

import os,sys,inspect,re
import xdrlib,xlrd
import csv
import pprint
import svn.local

reload(sys)
sys.setdefaultencoding("utf-8")
C_SPACE = ","
C_END = "\n"
SVN_VERSION = ""
TARGET = ""
SOURCE = ""
TXT_SVN = '''
    ==============================================================
    常用:      /data/work/svn/数据表/数值开发
    常用:      /data/work/svn/数据表/Release
    ==============================================================
'''
TXT_LOCAL = '''
    ==============================================================
    数值开发本地git:       /Users/playcrab/Documents/csv_debug/
    release本地git:       /Users/playcrab/Documents/csv_release/
    ==============================================================
'''


def cur_file_dir():
    # path = os.path.realpath(sys.path[0])
    # print path
    # if os.path.isfile(path):
    #     print "exe"
    #     path = os.path.dirname(path)
    #     return os.path.abspath(path)
    # else:
    #     print "文件"
    #     caller_file = inspect.stack()[1][1]
    #     return os.path.abspath(os.path.dirname(caller_file))
    global SVN_VERSION
    global SOURCE
    global TXT_SVN
    current_Path = os.getcwd()
    print TXT_SVN
    source_path = raw_input('请输入源目录:\n')
    while source_path[-1] == ' ':
        source_path = raw_input('路径末尾包含空格,需重新输入\n')
    os.chdir(source_path)
    #os.system('svn update')
    # print os.getcwd() + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    os.chdir(source_path)
    svn_text = svn.local.LocalClient(source_path)
    svn_info = svn_text.info()
    SVN_VERSION = svn_info["commit_revision"]
    os.chdir(current_Path)    # print SVN_VERSION
    # pprint.pprint(info)
    # print type(info)
    # print os.getcwd() + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    # print svn_info["commit_revision"]
    SOURCE = source_path
    return source_path

def find_file_by_pattern(pattern = '.*', base = ".", circle = True):  
    re_file = re.compile(pattern)
    if base == ".":
        base = cur_file_dir()
    print "开始搜索...：",base

    final_file_list = []
    cur_list = os.listdir(base)  
    for item in cur_list:
        if item == ".svn" :
            continue
        if item == ".git":
            continue
        if item == ".DS_Store":
            continue
        if item == ".gitignore":
            continue
          
        full_path = os.path.join(base, item)

        if full_path.startswith("~"):
            continue

        if full_path.endswith(".xlsx") or full_path.endswith(".xls"):
            print "in:" + full_path
            bfile = os.path.isfile(item)
            if os.path.isfile(full_path):
                if re_file.search(full_path):
                    final_file_list.append(full_path)  
            else:
                final_file_list += find_file_by_pattern(pattern, full_path)
    return final_file_list

def open_excel(file = 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def excel_table_byindex(file = 'file.xls', colnameindex = 0, by_index = 0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows 
    ncols = table.ncols 
    rowlist = []
    for rownum in range(colnameindex, nrows):
        rowdata = table.row_values(rownum)
        if rowdata:
            collist = []
            for i in range(ncols):
                collist.append(rowdata[i])
            rowlist.append(collist)
    return rowlist

def savaToCSV(_file, _list, _path):
    filename = ""
    content = ""
    for collist in _list:
        for i in range(len(collist)):
            v = collist[i]
            vstr = ""
            if isinstance(v, float) or isinstance(v, int):
                vstr = str(int(v))
            else:
                vstr = v
            if i > 0:
                content = content + C_SPACE
            content = content + vstr
        content = content + C_END

    fileName_old = _file.split("/")[-1]
    fname = fileName_old.split(".")[0]
    fileName_new = fname + ".csv"

    if len(fileName_new) > 0 and len(content) > 0:
        filename = _path + "/" + fileName_new
        print "out:" + filename
        file_object = open(filename, 'w')
        file_object.write(content)
        file_object.close()


def excel2csv(excel_file, _path):
    workbook = xlrd.open_workbook(excel_file)  
    all_worksheets = workbook.sheet_names()  
    for worksheet_name in all_worksheets:  
        worksheet = workbook.sheet_by_name(worksheet_name)
        fileName_old = excel_file.split("/")[-1]
        fname = fileName_old.split(".")[0]
        fileName = _path + fname + '_' + worksheet_name + '.csv'
        print "正在导出->fileName:" + fileName
        new_csv = open(fileName, 'wb')  
        wr = csv.writer(new_csv, quoting = csv.QUOTE_ALL)  
  
        for rownum in xrange(worksheet.nrows):  
            wr.writerow([unicode(entry).encode("utf-8") for entry in worksheet.row_values(rownum)])  
        new_csv.close() 

def main():
    global TXT_LOCAL
    filelist = find_file_by_pattern()
    if len(filelist) > 0:
        # path = "/Users/playcrab/Desktop/config/"
        #\033[1;35m test \033[0m!
        print TXT_LOCAL
        target_path = raw_input('请输入目标目录(结尾需要有"/"):\n')
        for file in filelist:
            datalist = excel_table_byindex(file, 0)
            if len(datalist) > 0:
                excel2csv(file, target_path)
        current_Path = os.getcwd()
        os.chdir(target_path)
        print "=" * 25
        os.system("git status")
        print "=" * 25
        os.system('git add . && git commit -m "svn v.' + str(SVN_VERSION) + '"')
        os.chdir(current_Path)
        global TARGET
        TARGET = target_path
        print ">>>>从" + SOURCE + "导出到" + TARGET + "成功<<<<"
        if os.path.exists("/Applications/SourceTree.app"):
            os.system("open /Applications/SourceTree.app")
    else:
        print "源目录输入错误"

if __name__ == "__main__":
    main()
