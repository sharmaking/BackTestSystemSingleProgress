#!/usr/bin/python
# -*- coding: utf-8 -*-
from DataApi_32 import CDataSaverProcess, CDataReaderProcess
import datetime

def main():
	#HOST = '192.168.1.186'
	HOST = '180.166.168.126'	#公网ip
	PORT = 18202
	subStock = ["999999"]

	ApiInstance = CDataSaverProcess(HOST,PORT,
		False, subStock,
		2,1,datetime.datetime(2014,1,2,0,0,0),datetime.datetime(2014,01,2,0,0,0)
		)

	DataReader = CDataReaderProcess(ApiInstance)
	DataReader.start()

	ApiInstance.run()
	pass

if __name__ == '__main__':
	main()