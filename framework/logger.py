#coding:utf-8

import logging, os, time
from configparser import ConfigParser
from framework.config import Config

config = Config.getConfig()

class Logger(object):

	def __init__(self, name):
		rootDir = os.path.dirname(os.path.abspath('.'))
		self.logger = logging.getLogger(name)
		self.logger.setLevel(logging.DEBUG)
		#读取配置文件中日志路径
		self.logPath = config.get("log","logPath")
		rq = time.strftime('%Y%d%m', time.localtime()) + '.log'
		self.logName = os.path.join(self.logPath, rq)

		#创建filehandler和streamhandler以及设置日志格式
		fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
		self.formatter = logging.Formatter(fmt)
		self.streamHandler = logging.StreamHandler()
		self.streamHandler.setFormatter(self.formatter)
		self.streamHandler.setLevel(logging.INFO)
		self.fileHandler = logging.FileHandler(self.logName, 'a')
		self.fileHandler.setFormatter(self.formatter)
		self.fileHandler.setLevel(logging.INFO)
		self.logger.addHandler(self.fileHandler)
		self.logger.addHandler(self.streamHandler)

	def getLogger(self):
		return self.logger