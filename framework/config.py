from configparser import ConfigParser
import os


class Config(object):

	rootDir = os.path.dirname(os.path.abspath('.'))
	configPath = os.path.join(rootDir, 'config\\', 'config.ini')

	@classmethod
	def getConfig(cls):
		cls.config = ConfigParser()
		cls.config.read(cls.configPath)
		return cls.config

