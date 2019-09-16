import unittest

from src.database.sqlite_opt import sqlite_opt
from src.entity.proxy_entity import ProxyEntity
from src.enum.common import ProxyTypeEnum
from src.validator.validator import validator


class TestValidator(unittest.TestCase):

    def setUp(self) -> None:
        self._opt = sqlite_opt
        self._validator = validator
        # self._opt.init_db()
        # proxy = ProxyEntity('127.0.0.1', '8080', source='66ip网', supplier='中国电信', proxy_type=ProxyTypeEnum.HTTPS.value)
        # assert self._opt.add_proxy(proxy) == 1, '插入proxy表失败'
        # proxy = ProxyEntity('127.0.0.2', '8081', source='66ip网', supplier='中国电信', proxy_type=ProxyTypeEnum.HTTPS.value)
        # assert self._opt.add_proxy(proxy) == 1, '插入proxy表失败'

        # self._opt.clean()

    def test_valid_proxy(self):
        self._validator.run()
        pass

