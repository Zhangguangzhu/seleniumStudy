#coding:utf-8
import os
import unittest
from testsuits import jforum_1_Home, jforum_2_List
from framework.broswer_engine import BrowserEngine

driver = BrowserEngine.get_driver()
# print('runtestid:%s',id(driver))



if __name__ == '__main__':
	runner = unittest.TextTestRunner(verbosity=2)
	# suite1 = unittest.TestLoader().loadTestsFromModule(jforumHome)
	# suite2 = unittest.TestLoader().loadTestsFromModule(jforumList)
	# suite = unittest.TestSuite([suite1,suite2])
	suite = unittest.defaultTestLoader.discover(os.path.abspath('.'),'jforum*')
	runner.run(suite)