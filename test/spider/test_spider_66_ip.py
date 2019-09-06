import unittest

from src.spider.spider_66_ip import Spider66Ip


class TestSpider77Ip(unittest.TestCase):

    def setUp(self) -> None:
        self._spider = Spider66Ip()

    def test_crawl(self):
        result = self._spider.crawl()
        assert result
        assert len(result) > 0
