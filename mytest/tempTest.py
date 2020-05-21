#coding:utf-8
import os
import time


class PropertyTest():

	Score = 100
	Name = 'zz'
	@property
	def score(self):
		return self._value

	@score.setter
	def score(self, value):
		if not isinstance(value,int):
			raise ValueError("value must be int type")
		if value < 0 and value > 100:
			raise ValueError("value must between 0~100")
		else:
			self._value = value

	@staticmethod
	def getsocre():
		a = 1
		print(a)

	@classmethod
	def getName(cls):
		print(cls.Name)

	def echoName(self, zz):
		print(zz)
if __name__=='__main__':
	test = PropertyTest()
	test.getsocre()
	PropertyTest.getsocre()
