#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import pandas as pd
import json
import csv
import requests
import os
import sys

DEBUG = False
reload(sys)
sys.setdefaultencoding('utf-8')

base_parameter_dict = {
	'mod':'http',
	'__noauth__':'1',
	'pGroup':'default',
	'MAX_FILE_SIZE':'9900000',
	'uploadFrom':'提交'
}
result = []
filelist = ['csvdata/checklistwyn.csv','csvdata/checklist.csv','csvdata/result.csv']
for x in filelist:
	if os.path.exists(x):
		os.remove(x)
		if DEBUG:
			print "已删除" + str(x)

data_xlsx = pd.read_excel('exceldata/checklist.xlsx',index_col=1)
data_xlsx.to_csv('csvdata/checklist.csv',encoding='utf-8')
data_xlsx.to_csv('csvdata/checklistwyn.csv',encoding='utf-8')

with open('csvdata/checklist.csv','rb') as csvfile:
	dict_reader = csv.DictReader(csvfile)
	with open('csvdata/checklistwyn.csv','rb') as csvfilewyn:
		rows = csv.reader(csvfilewyn)
		for i in dict_reader:
			for x in i.keys():
				if i[x] == '':
					del i[x]
			i.update(base_parameter_dict)
			r = requests.get("http://172.16.42.102:8001/", params = i)
			str_result = r.text
			if DEBUG:
				if '[error] => Array' in str(str_result):
					print "错误"
					print r.text
				elif '[error] => \n' in str(str_result):
					print "正确"
			result.append(r.text.decode('utf-8').encode('gbk'))
		with open('csvdata/result.csv','wb') as f:
			writer = csv.writer(f)
			time_count = 0
			for row in rows:
				row.append(result[time_count])
				writer.writerow(row)
				time_count += 1
