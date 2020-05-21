#coding:utf-8

import unittest
import time
from framework.logger import Logger
from framework.broswer_engine import BrowserEngine
from pageobject.jforumLoginPage import JforumLoginPage
from pageobject.jforumListPage import JforumListPage
from framework.deco import DependOn

class JforumHome(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = BrowserEngine.driver
		cls.logger = Logger('Jforum Home').getLogger()

	@classmethod
	def tearDownClass(cls):
		# cls.browser.quit_browser()
		pass

	def test_jforum_login(self):
		jforum = JforumLoginPage(self.driver)
		jforum.get_url()
		jforum.input_username_passwd('admin','admin')
		jforum.click_login_btn()
		try:
			assert 'list.page' in jforum.driver.current_url
			self.logger.info('login test success!')
		except Exception as e:
			self.logger.error('login test failed!')
			raise AssertionError('login test failed')

	# @DependOn('test_jforum_login')
	# def test_jforum_logout(self):
	# 	jforum = JforumListPage(self.driver)
	# 	jforum.logout()
	# 	try:
	# 		assert jforum.find_element('id=>login')
	# 		self.logger.info('logout test success!')
	# 	except Exception as e:
	# 		self.logger.error('logout test failed')
	# 		raise AssertionError('logout test failed')



if __name__ == '__main__':
	unittest.main(verbosity=2)
