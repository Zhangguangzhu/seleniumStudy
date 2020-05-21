#coding: utf-8

from framework.base_page import BasePage
import time
from framework.config import Config

config = Config().getConfig()

class JforumLoginPage(BasePage):

	def get_url(self):
		loginUrl = config.get("testUrl", "loginUrl")
		self.get(loginUrl)

	def input_username_passwd(self, username, passwd):
		self.type('xpath=>//input[@name="username"]', username)
		self.type('xpath=>//input[@name="password"]', passwd)

	def click_login_btn(self):
		self.click('xpath=>//input[@name="login"]')

if __name__ == "__main__":
	jforum = JforumPage()
	jforum.login()