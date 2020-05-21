#coding:utf-8

def _init():
	print('init')
	global _global_dict
	_global_dict = {}

def setValue(key,value):
	print('setvalue!!!!!!!!!')
	_global_dict[key] = value

def getValue(key):
	try:
		return _global_dict[key]
	except KeyError:
		return None

