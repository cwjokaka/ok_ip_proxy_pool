import asyncio
from typing import List, Iterable

import aiohttp

from setting import HEADERS
from src.entity.proxy_entity import ProxyEntity
from src.log.logger import logger


class AbsSpider(object):

    def __init__(self, name='unknown') -> None:
        self._name = name
        self._urls = self.get_urls()

    async def crawl(self):
        logger.info(f'{self._name}开始爬取...')
        res = []
        for url in self._urls:
            try:
                for page in self.get_page_range():
                    async with aiohttp.ClientSession() as session:
                        async with session.get(self.get_page_url(url, page), headers=HEADERS) as resp:
                            resp.encoding = self.get_encoding()
                            temp = self.do_crawl(await resp.text())
                            res.extend(temp)
                            await asyncio.sleep(self.get_interval())
            except Exception as e:
                logger.exception(f'{self._name}爬取失败url: {url}, :e:{e}')
        return res

    def do_crawl(self, resp: str) -> List[ProxyEntity]:
        """
        子类重写此方法解析网页内容
        :param resp: 返回内容字符串
        :return: 代理列表
        """
        raise NotImplementedError

    def get_urls(self) -> List[str]:
        """
        子类从写此方法返回获取
        :return:
        """
        raise NotImplementedError

    def get_page_range(self) -> Iterable:
        """
        默认只获取第一页内容
        :return:
        """
        return range(1, 2)

    def get_page_url(self, url, page) -> str:
        """
        格式化页数url
        :param url: url
        :param page:
        :return:
        """
        return f'{url}/{page}'

    def get_encoding(self):
        """
        默认页面编码
        :return:
        """
        return 'utf-8'

    def get_interval(self) -> int:
        """
        代理网站爬取间隔(秒)
        :return:
        """
        return 0
