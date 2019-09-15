import unittest

from src.database.sqlite_opt import SqliteOpt
from src.entity.proxy_entity import ProxyEntity
from src.enum.common import ProxyTypeEnum


class TestSqliteOpt(unittest.TestCase):

    def setUp(self) -> None:
        self._opt = SqliteOpt()

    def test_init_db(self):
        self._opt.init_db()

    def test_add_proxy(self):
        proxy = ProxyEntity('127.0.0.1', '8080', source='66ip网', supplier='中国电信', proxy_type=ProxyTypeEnum.HTTPS.value)
        result = self._opt.set(proxy)
