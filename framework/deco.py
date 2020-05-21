#coding:utf-8
from functools import wraps
import unittest

class DependOn(object):

	def __init__(self, dependfunc):
		self.dependfunc = dependfunc

	def __call__(self, func):
		@wraps(func)
		def wrapper(case):
			if self.dependfunc == func.__name__:
				raise ValueError('can\'t denpend on itself')
			failures = str([ fail[0] for fail in case._outcome.result.failures ])
			if self.dependfunc in failures:
				return unittest.skip('depend case run failed')(func)(case)
			else:
				return func(case)
		return wrapper
