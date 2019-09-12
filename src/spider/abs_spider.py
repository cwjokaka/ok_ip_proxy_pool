import asyncio
from asyncio import AbstractEventLoop
from collections import Coroutine
from typing import List, Iterable

from src.entity.proxy_entity import ProxyEntity


class AbsSpider(object):

    def __init__(self, name='unknown') -> None:
        self._name = name

    def crawl(self, event_loop: AbstractEventLoop):
        print(f'{self._name}开始爬取...')
        # self.do_crawl()
        # print(type(self.do_crawl()))
        # print(isinstance(self.do_crawl(), Coroutine))
        self.do_crawl(event_loop)
        # print(f'{self._name}爬取完毕!共:{len(res)}个代理')
        # todo 持久化到数据库

        # return ful.result()

    def do_crawl(self, event_loop) -> Iterable[ProxyEntity]:
        raise NotImplementedError

