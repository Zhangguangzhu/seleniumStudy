#coding:utf-8

import unittest
from cases.case2_test_str import StrFuncTest
from cases.test_case1_math import MathFuncTest
from cases import test_case1_math
from cases import case2_test_str

def suite():
	# suite = unittest.TestSuite()
	# suite.addTests([StrFuncTest('test_in'),MathFuncTest('test_add')])
	# cases = unittest.TestLoader().loadTestsFromModule(case2_test_str)
	# cases = unittest.TestLoader().loadTestsFromTestCase(MathFuncTest)
	suite = unittest.TestLoader().discover("cases",'*test*')
	# suite.addTest(cases)
	return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite())