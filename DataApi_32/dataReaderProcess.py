#!/usr/bin/python
# -*- coding: utf-8 -*-
#dataReaderProcess
import multiprocessing, datetime

class CDataReaderProcess(multiprocessing.Process):
	def __init__(self, dataSaverObj):
		super(CDataReaderProcess, self).__init__()
		self.name = "Data Reader Process"
		self.dataBufferStack = dataSaverObj.bufferStack["data"]
		self.sysMessageBufferStack = dataSaverObj.bufferStack["__SystemMessage__"]
		print datetime.datetime.now()

	#开始接收数据
	def run(self):
		while True:
			#取出数据数据
			while not self.dataBufferStack.empty():
				stockCode, dataType, data = self.dataBufferStack.get()
				self.onRtnData(stockCode, dataType, data)
			#监视系统信息
			if not self.sysMessageBufferStack.empty():
				systemMessage = self.sysMessageBufferStack.get()
				if systemMessage == "DayEnd":
					self.onDayEnd()
				if systemMessage == "DataEnd":
					self.onDataEnd()
					print datetime.datetime.now()
	#数据接收
	def onRtnData(self, stockCode, dataType, data):
		pass
	#当日结束
	def onDayEnd(self):
		pass
	#全部数据结束
	def onDataEnd(self):
		pass
