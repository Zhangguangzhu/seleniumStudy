#coding:utf-8

import logging, os, time


rq = time.strftime('%Y-%m-%d', time.localtime())
log_path = os.path.abspath('..') + '\log\\'
log_name = log_path + rq + '.log'
logger = logging.getLogger('hehe')
fmt = '%(levelname)s - %(name)s - %(asctime)s - %(message)s'
formatter = logging.Formatter(fmt)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.NOTSET)
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(log_name,'a')
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.debug('1')
logger.warning('2')
logger.critical('3')
logger.error('4')
logger.info('5')