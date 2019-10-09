import unittest

from src.database.sqlite_opt import sqlite_opt
from src.entity.proxy_entity import ProxyEntity
from src.enum.common import ProxyTypeEnum


class TestSqliteOpt(unittest.TestCase):

    def setUp(self) -> None:
        self._opt = sqlite_opt
        self._opt.init_db()
        # self._opt.clean()

    def test_add_proxy(self):
        proxy = ProxyEntity('127.0.0.1', '8080', source='66ip网', supplier='中国电信', proxy_type=ProxyTypeEnum.HTTPS.value)
        assert self._opt.add_proxy(proxy) == 1, '插入proxy表失败'
        proxy = ProxyEntity('127.0.0.2', '8081', source='66ip网', supplier='中国电信', proxy_type=ProxyTypeEnum.HTTPS.value)
        assert self._opt.add_proxy(proxy) == 1, '插入proxy表失败'

    def test_get_all_proxies(self):
        proxy_list = self._opt.get_all_proxies()
        assert len(proxy_list) > 0

    def test_remove_all_zero_reliability(self):
        self._opt.remove_all_zero_reliability()
