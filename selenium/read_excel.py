#-*- coding: UTF-8 -*-
import xlrd
import os

PATH = "C:/Users/nihao/Desktop/test.xlsx"
class ExcelOperation(object):
	table = ''
	cell = ''
	nrows = ''
	start = 0
	end = 0
	locate_type = []
	locate_value = []
	locate_action = []
	test_value = []
	def __init__(self):
		__date = xlrd.open_workbook(PATH)
		self.table = __date.sheets()[0]
		self.nrows = self.table.nrows
		
	def read_sheet(self):
		pass

	def find_case_rows(self,case_name):
		for i in range(1,self.nrows):
			 cell = self.table.col(0)[i].value
			 if cell == case_name :
			 	self.start = i
			 	for g in range(i+1,self.nrows):
			 		cell = self.table.col(0)[g].value
			 		if cell != '':
			 			self.end = g
			 			return

	def get_locate_info(self):
		len = self.end-self.start
		for i in range(self.start+1,self.end):
			cell = self.table.col(3)[i].value
			cell1 = self.table.col(4)[i].value
			cell2 = self.table.col(5)[i].value
			cell3 = self.table.col(6)[i].value
			if cell == '':
				self.locate_type.append(None)
			else:
				self.locate_type.append(cell)
			if cell1 == '':
				self.locate_value.append(None)
			else:
				self.locate_value.append(cell1)
			if cell2 == '':
				self.locate_action.append(None)
			else:
				self.locate_action.append(cell2)
			if cell3 == '':
				self.test_value.append(None)
			else:
				self.test_value.append(cell3)


RE = ExcelOperation()
RE.find_case_rows(u'中文')
RE.get_locate_info()
print RE.locate_type,RE.locate_action,RE.locate_value,RE.test_value
