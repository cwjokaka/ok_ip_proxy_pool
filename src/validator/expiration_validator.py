from src.database.sqlite_opt import sqlite_opt
from src.log.logger import logger


class ExpirationValidator(object):

    def run(self):
        logger.info('开始删除不可用代理')
        sqlite_opt.remove_all_zero_reliability()
        logger.info('不可用代理删除完毕')


expiration_validator = ExpirationValidator()
