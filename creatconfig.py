#!/usr/bin/env python
# encoding: utf-8


import xlrd
from collections import OrderedDict
import os
filesname = ['other_config','other_config_taiwan','other_config_kor']

for filename in filesname:
	if os.path.exists(filename + ".py"):
		os.remove(filename + ".py")


for creat in filesname:
	fConfig = open(creat + ".py", 'w')
	fConfig.writelines('#!/usr/bin/env python \n')
	fConfig.writelines('# encoding: utf-8 \n\n')

	wb = xlrd.open_workbook('exceldata/' + creat + ".xlsx")

	convert_list = []
	sheet_names = wb.sheet_names()
	for sheet_name in sheet_names:
		tempData = sheet_name + "="
		sheet = wb.sheet_by_name(sheet_name)
		cols = sheet.col_values(0)
		sheet_type = cols[0]
		cell_type = cols[1]
		if sheet_type == 'Array':
			tempData = tempData + "["
		elif sheet_type == 'String':
			tempData = tempData + '"'

		for colnum in range(2, len(cols)):
			if cell_type == 'String':
				tempData = tempData + '"' + str(cols[colnum]) + '"'
			else:
				tempData = tempData + str(int(cols[colnum]))
			if colnum < len(cols) - 1:
				tempData = tempData + ","

		if sheet_type == 'Array':
			tempData = tempData + "]"
		elif sheet_type == 'String':
			tempData = tempData + '"'

		tempData = tempData + "\n"
		fConfig.writelines(tempData)

	fConfig.close()
	
