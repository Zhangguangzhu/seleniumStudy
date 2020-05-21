#coding:utf-8
import os
from selenium import webdriver
from configparser import ConfigParser
from framework.logger import Logger
from framework.config import Config

# rootDir = os.path.dirname(os.path.abspath('.'))
# configPath = os.path.join(rootDir,"config\\","config.ini")
logger = Logger("BrowserEngine").getLogger()
config = Config.getConfig()

class BrowserEngine(object):

	driver = ''

	def __init__(self):
		pass

	@classmethod
	def get_driver(cls):
		browserType = config.get("browserType", "browserName")
		logger.info('select {0}'.format(browserType))
		cls.driver = eval('webdriver.{0}'.format(browserType))()
		# url = config.get("testUrl","url")
		# logger.info('open url:{0}'.format(url))
		# self.driver.get(url)
		cls.driver.implicitly_wait(10)
		return cls.driver

	@classmethod
	def quit_browser(cls):
		logger.info('browser quit')
		cls.driver.quit()


if __name__ == '__main__':
	engine = BrowserEngine()
	engine.open_broswer()