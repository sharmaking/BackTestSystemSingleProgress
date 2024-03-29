#!/usr/bin/python
# -*- coding: utf-8 -*-
#dataSaverProcess
import multiprocessing
import dataApi

class CDataSaverProcess(object):
	def __init__(self, HOST, PORT, isAllMarket, subStocks, requestType, flag, startTime, endTime):
		super(CDataSaverProcess, self).__init__()
		self.name = "Socket Data Saver Process"
		self.bufferStack = {	#每个合约一个堆栈
			"data"				: multiprocessing.Queue(),	#数据
			"__SystemMessage__"	: multiprocessing.Queue()	#系统信息
			}	
		self.isAllMarket, self.subStocks, self.requestType, self.flag, self.startTime, self.endTime \
			= isAllMarket, subStocks, requestType, flag, startTime, endTime
		self.dataSocketServerApi = dataApi.CDataApi(HOST, PORT, self.bufferStack)	
		self.creatBufferStack()
	#创建缓存对象
	def creatBufferStack(self):
		for stock in self.subStocks:
			self.bufferStack[stock] = multiprocessing.Queue()
	#开始接收数据
	def run(self):
		self.dataSocketServerApi.connectServer()
		#订阅股票
		self.dataSocketServerApi.subscibeStock(self.isAllMarket, self.subStocks)
		#请求数据参数
		self.dataSocketServerApi.requestData(self.requestType, self.flag, self.startTime, self.endTime)
		#开始接收数据
		self.dataSocketServerApi.run()