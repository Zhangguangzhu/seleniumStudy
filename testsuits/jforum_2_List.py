#coding:utf-8

import unittest
from framework.logger import Logger
from framework.deco import DependOn
from framework.broswer_engine import BrowserEngine
from pageobject.jforumListPage import JforumListPage

class JforumList(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = BrowserEngine.driver
		# cls.browser = BrowserEngine()
		# cls.driver = cls.browser.open_broswer()
		cls.logger = Logger('Jforum List').getLogger()

	@DependOn('test_jforum_login')
	def test_jforum_logout(self):
		jforum = JforumListPage(self.driver)
		jforum.logout()
		try:
			assert jforum.find_element('id=>login')
			self.logger.info('logout test success!')
		except Exception as e:
			self.logger.error('logout test failed')