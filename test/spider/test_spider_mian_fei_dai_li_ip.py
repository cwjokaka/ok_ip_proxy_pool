import asyncio
import unittest

from src.spider.spiders import SpiderMianFeiDaiLiIp


class TestSpiderMianFeiDaiLiIp(unittest.TestCase):

    def setUp(self) -> None:
        self._spider = SpiderMianFeiDaiLiIp()

    def test_crawl(self):
        result = asyncio.run(self._spider.crawl())
        assert result
        assert len(result) > 0
