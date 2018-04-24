#!/usr/bin/python
# _*_ coding:utf-8 _*_
import logging
import logging.config

logging.config.fileConfig('info.cnf')
logging.debug('debug logging')
logging.info('info logging')
logging.warn('warn logging')
logging.error('error logging')
logging.critical('critical logging')

