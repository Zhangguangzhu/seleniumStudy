#coding:utf-8

from framework.logger import Logger
from framework.config import Config
from framework.broswer_engine import BrowserEngine
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

config = Config.getConfig()
rq = time.strftime('%Y%m%d_%H%M%S',time.localtime())

class BasePage(object):


	def __init__(self, driver):
		self.driver = driver
		self.logger = Logger(self.__class__.__name__).getLogger()

	def get(self, url):
		try:
			self.driver.get(url)
			self.logger.info('open url:{0}'.format(url))
		except Exception as e:
			self.logger.error('open url:{0} failed'.format(url))


	def get_window_img(self):
		imgpath = config.get("img","imgPath")
		imgName = imgpath + rq + '.png'
		try:
			self.driver.get_screenshot_as_file(imgName)
			self.logger.info('save screenshot succeed')
		except Exception as e:
			self.logger.error('save screenshot failed {0}'.format(e))

	def find_element(self, locator):
		#切割传入的字符串分离出查找类型和表达式
		el = ''
		if '=>' not in locator:
			raise ValueError('locator must split by =>')
		locator_by_str = locator.split('=>')[0]
		locator_value = locator.split('=>')[1]
		locator_by = eval("self.driver.find_element_by_{0}".format(locator_by_str))
		try:
			el = locator_by(locator_value)
			self.logger.info('find element {0}:{1}'.format(locator_by_str, locator_value))
		except NoSuchElementException:
			self.logger.error('no such element {0}:{1}'.format(locator_by_str, locator_value))
			self.get_window_img()
		except AttributeError as e:
			self.logger.error('incorrect locator type')
		return el

	def type(self, locator, text):
		el = self.find_element(locator)
		# el.clear()
		try:
			el.send_keys(text)
			self.logger.info('input value:{0}'.format(text))
		except Exception as e:
			self.logger.error('input value:{0} failed'.format(text))
			self.get_window_img()

	def click(self, locator):
		el = self.find_element(locator)
		try:
			el.click()
			self.logger.info('click element:{0}'.format(locator))
		except Exception as e:
			self.logger.error('click element:{0} failed'.format(locator))

	def refresh(self):
		self.driver.refresh()
		self.logger.info('page refresh')

	def get_page_title(self):
		self.logger.info('current page title is {0}'.format(self.driver.title))
		return self.driver.title

if __name__ == "__main__":
	base = BasePage()
	# el = base.find_element('xpath=>//[input[@name="username"]')
	base.type('xpath=>//input[@name="username"]',"admin")
	base.type('xpath=>//input[@name="password"]',"admin")
	base.click('xpath=>//input[@name="login"]')
	# base.get_window_img()