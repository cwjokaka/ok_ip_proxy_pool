import asyncio
import unittest

from src.spider.spiders import Spider66Ip


class TestSpider66Ip(unittest.TestCase):

    def setUp(self) -> None:
        self._spider = Spider66Ip()

    def test_crawl(self):
        # async def dodo():
        #     return await
        result = asyncio.run(self._spider.crawl())
        assert result
        assert len(result) > 0
