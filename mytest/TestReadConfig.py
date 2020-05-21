#coding=utf-8

import configparser
import os

class TestReadConfig(object):

	def get_value(self):
		root_dir = os.path.abspath('..')
		print(root_dir)

		config = configparser.ConfigParser()
		file_path = root_dir + '\config\config.ini'
		config.read(file_path)

		url = config.get("testUrl","Url")
		browser = config.get("browserType","browserName")
		return (browser,url)

t = TestReadConfig()
print(t.get_value())
# print(os.path.abspath('.'))