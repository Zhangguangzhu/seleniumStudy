#coding:utf-8

import unittest

class StrFuncTest(unittest.TestCase):


	@classmethod
	def setUpClass(cls) -> None:
		print('str test start')

	@classmethod
	def tearDown(self) -> None:
		print('str test oomplete')

	def test_in(self):
		self.assertIn('a','abc')

