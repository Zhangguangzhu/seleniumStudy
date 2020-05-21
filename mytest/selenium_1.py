# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyautogui,requests
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class JforumFuncTest():

	def __init__(self):
		self.homeUrl = 'http://127.0.0.1:8080/jforum-2.6.2/forums/list.page'
		self.loginUrl = 'http://localhost:8080/jforum-2.6.2/user/login.page'
		self.userinfo = {'username': 'admin', 'passwd': 'admin'}
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(5)

	def _highlight(self, element):
		self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
		                           element,"background: green;borader:2px solid red;")

	def loginTest(self):
		try:
			self.driver.get(self.loginUrl)
			user = self.driver.find_element_by_xpath('//input[@name="username"]').send_keys('admin')
			self.driver.find_element_by_xpath('//input[@name="password"]').send_keys("admin")
			self.driver.find_element_by_xpath('//input[@value="登入"]').click()
			loginStatus = self.driver.find_element_by_xpath('//a[@id="logout"]').is_displayed()
		# assert loginStatus
		except Exception  as e:
			print('login failed', e)

	def replyTest(self):
		try:
		# self.driver.find_element_by_partial_link_text("测试技术").click()
			self.driver.find_element_by_xpath('//a[contains(text(),"测试技术")]').click()
		except Exception as e:
			print(e)

	def funcTest(self):
		# print('refresh...............')
		# self.driver.refresh()
		# print(self.driver.capabilities)
		# self.driver.get('http://www.divcss5.com/yanshi/checkbox.html')

		# 切换标签及创建新标签页
		# self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL,'t')
		# # self.driver.execute_script("window.open('{}');".format(self.homeUrl))
		# window_before = self.driver.window_handles[0]
		# window_after = self.driver.window_handles[1]
		# time.sleep(1)
		# self.driver.switch_to.window(window_before)
		# time.sleep(1)
		# self.driver.switch_to.window(window_after)

		#遍历radio
		# radioList = self.driver.find_elements_by_xpath('//input[@name="Fruit"]')
		# for i in radioList:
		# 	i.click()
		# 	print(i.is_selected())
		# 	time.sleep(1)

		# 获取元素上的文字
		# self.driver.get(self.loginUrl)
		# self.driver.find_element_by_xpath('//input[@value="登入"]').click()
		# try:
		# 	errorMess = self.driver.find_element_by_xpath('//span[@id="invalidlogin"]')
		# 	assert '错误的密码' in errorMess.text
		# 	print('login success')
		# except Exception as e:
		# 	print('login failed',e)

		#鼠标操作
		# self.driver.get(self.homeUrl)
		# e = self.driver.find_element_by_xpath('//img[@alt="[Logo]"]')
		# e = self.driver.find_element_by_partial_link_text('测试技术')
		# self._highlight(e)
		# print(e)
		actionchains = ActionChains(self.driver)
		# actionchains.context_click(e).perform()
		# time.sleep(2)
		# pyautogui.typewrite(['down','down'])
		# time.sleep(2)
		# pyautogui.typewrite(['enter'])

		#处理弹窗
		# self.driver.get(self.homeUrl)
		# self.driver.execute_script("window.alert('测试');")
		# time.sleep(3)
		# self.driver.switch_to.alert.accept()
		# self.driver.save_screenshot('test.png')

		#下载图片
		self.driver.get(self.homeUrl)
		e = self.driver.find_element_by_xpath('//img[@alt="[Logo]"]')
		picUrl = e.get_attribute('src')
		response = requests.get(picUrl)
		img = response.content
		with open('./logo.png','wb') as f:
			f.write(img)
			print('download pic success')

if __name__ == '__main__':
	jforum = JforumFuncTest()
	jforum.loginTest()
	# jforum.replyTest()
	# jforum.funcTest()
	# jforum.driver.find_element_by_ta