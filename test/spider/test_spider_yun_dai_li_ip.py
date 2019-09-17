import asyncio
import unittest

from src.spider.spiders import SpiderYunDaiLiIp


class TestSpiderXiciIp(unittest.TestCase):

    def setUp(self) -> None:
        self._spider = SpiderYunDaiLiIp()

    def test_crawl(self):
        result = asyncio.run(self._spider.crawl())
        assert result
        assert len(result) > 0
