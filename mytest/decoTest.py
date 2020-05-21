#coding:utf-8

import logging, time

class MyLogger(object):

	logger = logging.getLogger()
	fmt = "%(asctime)s-%(levelname)s - %(name)s - %(message)s"
	Formatter = logging.Formatter(fmt)
	logger.setLevel(logging.DEBUG)
	logName = time.strftime("%Y_%m_%d",time.localtime()) + '.log'

	@classmethod
	def Handler(cls, level, handlerType):
		if handlerType == logging.StreamHandler:
			Handler = logging.StreamHandler()
		else:
			Handler = logging.FileHandler(cls.logName, 'a')

		Handler.setFormatter(cls.Formatter)
		Handler.setLevel(level)

		cls.logger.addHandler(Handler)
		def _deco(func):
			def __deco(*args, **kwargs):
				cls.logger.info('{0} start....'.format(func.__name__))
				return func(*args, **kwargs)
			return __deco
		return _deco


class TempTest(object):

	@MyLogger.Handler(logging.DEBUG, logging.FileHandler)
	def mytest(self,name):
		print('called from %s' % name)

test = TempTest()
test.mytest('zz')