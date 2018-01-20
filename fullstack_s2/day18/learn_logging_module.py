#__author:  "Jing Xu"
#date:  2018/1/20

import logging
# --------------------------------------------------------------
# logging.basicConfig(level=logging.DEBUG,
# 					format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
# 					datefmt='%a, %d %b %Y %H:%M:%S',
# 					filename='test.log',
# 					filemode='a')
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')
# --------------------------------------------------------------
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('test02.log')
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
fh.setFormatter( formatter )
ch.setFormatter( formatter )
logger.addHandler(fh)
logger.addHandler(ch)
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
# --------------------------------------------------------------
# import os
# import time
# import logging
# from config import settings
#
# def get_logger(card_num, struct_time):
#
# 	if struct_time.tm_mday < 23:
# 		file_name = "%s_%s_%d" %(struct_time.tm_year, struct_time.tm_mon, 22)
# 	else:
# 		file_name = "%s_%s_%d" %(struct_time.tm_year, struct_time.tm_mon+1, 22)
#
# 	file_handler = logging.FileHandler(
# 		os.path.join(setting.USER_DIR_FOLDER, card_num, "record", file_name),
# 		encoding="utf-8"
# 	)
#
# 	fmt = logging.Formatter( fmt="%(asctime)s :	   %(message)s")
# 	file_handler.setFormatter(fmt)
#
# 	logger1 = logging.Logger("user_logger", level=logging.INFO)
# 	logger1.addHandler(file_handler)
# 	return logger1
# --------------------------------------------------------------