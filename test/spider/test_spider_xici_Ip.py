import unittest

from src.spider.spider_xici_ip import SpiderXiciIp


class TestSpiderXiciIp(unittest.TestCase):

    def setUp(self) -> None:
        self._spider = SpiderXiciIp()

    def test_crawl(self):
        result = self._spider.crawl()
        assert result
        assert len(result) > 0
