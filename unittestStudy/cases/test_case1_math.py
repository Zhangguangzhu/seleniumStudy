#coding:utf-8

import unittest

add = lambda x,y:x+y
div = lambda x,y:x-y

class MathFuncTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('Test start')

	@classmethod
	def tearDownClass(cls):
		print('Test complete')

	@unittest.skip
	def test_add(self):
		self.assertEqual(3,add(1,2))

	def test_div(self):
		assert 3 == div(5,2)

if __name__ == '__main__':
	unittest.main(verbosity=2)