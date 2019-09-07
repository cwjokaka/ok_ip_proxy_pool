import unittest

from src.spider.spider_quan_wang_ip import SpiderQuanWangIp


class TestSpiderQuanWangIp(unittest.TestCase):

    def setUp(self) -> None:
        self._spider = SpiderQuanWangIp()

    def test_crawl(self):
        result = self._spider.crawl()
        # assert result
        # assert len(result) > 0
