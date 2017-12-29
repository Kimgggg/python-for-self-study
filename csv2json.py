#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import os
import shutil
import string
import sys
import json
import types


src_dir = os.path.dirname( os.path.realpath(__file__) )
src_path = os.path.join(src_dir, "D:\QA\csvdata\\")

def  lua_exporter(data_list, file_name):
	toPath = os.path.join(src_dir,"D:\QA\jsondata\\",file_name + '.json')
	with open(toPath, 'wb') as luafile:
		luafile.write(json.dumps(data_list, ensure_ascii=False).encode('utf8'))
	return lua_exporter;

def _data_desc_from_sheet(csvReader):

	dic = []
	dump_var = 0
	fnames = []
	ftypes = []
	while 1:
		try:
			row = csvReader.next()
			if csvReader.line_num == 2:
				fnames = row
			elif csvReader.line_num == 3:
				ftypes = row
			elif csvReader.line_num > 3:
				break
		except StopIteration:
			break
	for i, name_type in enumerate(zip(fnames, ftypes)):
		fname, ftype = name_type
		var_name = fname
		var_type = ftype
		var_type_name = ftype
		var_extra = None
		if i == 0 and var_name != 'id':
			#print 'first column must be id auto fixed'
			var_name = 'id'
			if var_type != 'int32' and var_type != 'string':
				var_type_name = 'int32'
				var_type = 'int32'
		elif 'enum' in ftype:
			if ftype.find('enum') != -1:
				name_start = ftype.find('enum')
				var_type = 'enum'
				if name_start == -1:
					print 'parser enum for ', var_name , 'error'
					continue
				name_start += 4
				name_end = ftype.find('{')
				if name_end == -1:
					#print 'parser enum for ', var_name ,"doesn't have body"
					name_end = len(ftype)
				else:
					var_extra = ftype[name_end:]
				var_type_name = ftype[name_start:name_end]
				var_type_name = var_type_name.strip()
		elif var_name == '':
			# 空标题以后的列全部忽略
			break

		var_def = {}
		var_def['seq_num'] = i
		var_def['type'] = var_type or 'int32'
		var_def['name'] = var_type_name or 'int32'
		var_def['var_name'] = var_name;
		if var_extra != None:
			var_def['extra'] = var_extra
		dic.append(var_def)

	return dic

def convert_json_to_table(data):
	data_dic = None
	try:
		data_dic = json.loads(data)
	except Exception, e:
		data_dic =[]
	else:
		pass
	finally:
		pass
	return data_dic

def get_data_dic(row,dbdesc):

	data_dic = {}
	for i, data_row_and_desc in enumerate(zip(row, dbdesc)):
		data, data_desc = data_row_and_desc

		if data_desc['type'] == 'string':
			data = data.decode('utf8').strip()
		elif data_desc['type'] == 'json':
			data = convert_json_to_table(data)
		elif data_desc['type'] == 'bool':
			if data == '0' or data == '' or data == 'false' or data == 'False':
				data = False
			else:
				data = True
		elif data_desc['type'] == 'float':
			try:
				data = float(data)
			except Exception, e:
				print "convert to float failed for", i, data, data_desc
				print "row", row
				raise e
		elif data_desc['type'] == 'comment':
			continue
		else:
			if data == '':
				data = 0
			data = int(data)

		data_dic[data_desc['var_name']] = data
	return data_dic

def export_json(csvReader,dbdesc,dbName):
	data_list = []
	while True:
		try:
			row = csvReader.next()
			if csvReader.line_num <= 3:
				continue
			if len(row[0].strip()) < 1:
				continue
			rowdesc = get_data_dic(row,dbdesc)
			data_list.append(rowdesc)
		except StopIteration:
			break
	return data_list


def _visit_csv_sheet_with_data(di):
	for root,dirs,files in os.walk(di):
		for filepath in files:
			tablePath = os.path.join(root,filepath)
			excel_file_name = os.path.split(tablePath)[1];
			filess = excel_file_name.split('.');
			if filess == None or len(filess) <2 or filess[1] != 'csv' or  filess[0].find('~$') != -1 or filess[0] == "ResName" :
				print 'ignore file', tablePath
				continue
			file_name = filess[0];
			file_exten = filess[1];

			print ' open file', tablePath
			dbdesc = _data_desc_from_sheet(csv.reader(file(tablePath, 'rb')))
			if dbdesc:
				data_list = export_json(csv.reader(file(tablePath, 'rb')),dbdesc,file_name)
				lua_exporter(data_list,file_name)
			else:
				print('export db ',file_name,'error')

_visit_csv_sheet_with_data(src_path)