#!/usr/bin/env python
# encoding: utf-8
# from __future__ import unicode_literals
import csv
import json


def get_csvValue(filename,x,y):
	#读取指定单元格：行、列
	with open(filename,'rb') as csvFile:
		reader = csv.reader(csvFile)
		column1 = [row[y] for row in reader]
		return column1[x]


def get_csv(filename):
	typelist = []
	with open(filename, 'r') as csvfile:
		read = csv.reader(csvfile)
		for i in read:
			# typedict[i[0]] = i[1]
			typelist.append(i[0] + " : " + i[1])
	csvfile.close()
	return typelist

def csv2dict(filename):
	temp_dict = []
	with open(filename,'r') as csvFile:
		dict_reader = csv.DictReader(csvFile)
		for i in dict_reader:
			for x in i.keys():
				if i[x] == '':
					del i[x]
			temp_dict.append(i)
	return temp_dict
