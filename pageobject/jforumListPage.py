#coding:utf-8

from framework.base_page import BasePage

class JforumListPage(BasePage):

	def logout(self):
		self.click('id=>logout')

if __name__=='__main__':
	unittest.main()